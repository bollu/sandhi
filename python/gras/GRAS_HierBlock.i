//
// Copyright 2012 Josh Blum
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU Lesser General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU Lesser General Public License for more details.
//
// You should have received a copy of the GNU Lesser General Public License
// along with this program.  If not, see <http://www.gnu.org/licenses/>.

#define GRAS_API

////////////////////////////////////////////////////////////////////////
// http://www.swig.org/Doc2.0/Library.html#Library_stl_exceptions
////////////////////////////////////////////////////////////////////////
%include "exception.i"

%exception
{
    try
    {
        $action
    }
    catch (const std::exception& e)
    {
        SWIG_exception(SWIG_RuntimeError, e.what());
    }
}

%{
#include <gras/hier_block.hpp>
#include <gras/top_block.hpp>
%}

%include <gras/element.i>
%include <gras/io_signature.i>

////////////////////////////////////////////////////////////////////////
// pull in hier and top interface
////////////////////////////////////////////////////////////////////////
%include <gras/hier_block.hpp>
%include <gras/top_block.hpp>

////////////////////////////////////////////////////////////////////////
// Make a special top block with python safe unlocking wait
////////////////////////////////////////////////////////////////////////

%inline %{

namespace gras
{

struct TopBlockPython : TopBlock
{
    TopBlockPython(const std::string &name = "Top"):
        TopBlock(name)
    {
        //NOP
    }

    void wait(void)
    {
        PyThreadState *s = PyEval_SaveThread();
        TopBlock::wait();
        PyEval_RestoreThread(s);
    }

    bool wait(const double timeout)
    {
        PyThreadState *s = PyEval_SaveThread();
        const bool ret = TopBlock::wait(timeout);
        PyEval_RestoreThread(s);
        return ret;
    }
};

struct HierBlockPython : HierBlock
{
    HierBlockPython(const std::string &name = "Hier"):
        HierBlock(name)
    {
        //NOP
    }

    HierBlockPython(
        const std::string &name,
        const IOSignature &input_signature,
        const IOSignature &output_signature
    ):
        HierBlock(name)
    {
        this->set_input_signature(input_signature);
        this->set_output_signature(output_signature);
    }
};

}

%}

////////////////////////////////////////////////////////////////////////
// Remake top block and hier block for multi-arg connnect
////////////////////////////////////////////////////////////////////////
%pythoncode %{

def to_element(obj):
    if isinstance(obj, Element): return obj
    try: return obj.shared_to_element()
    except: raise Exception('cant coerce obj %s to element'%(obj))

def internal_connect__(fcn, obj, refs, action, *args):

    if len(args) == 1:
        elem = (args[0])
        fcn(obj, elem)
        if elem != to_element(obj): action(refs, elem)
        return

    for src, sink in zip(args, args[1:]):

        try: src, src_index = src
        except: src_index = 0
        src = to_element(src)

        try: sink, sink_index = sink
        except: sink_index = 0
        sink = to_element(sink)

        fcn(obj, src, src_index, sink, sink_index)

        #incr/decr the python obj ref counts
        if src != to_element(obj): action(refs, src)
        if sink != to_element(obj): action(refs, sink)

class TopBlock(TopBlockPython):
    def __init__(self, *args, **kwargs):
        TopBlockPython.__init__(self, *args, **kwargs)
        self.__refs = list()

    def connect(self, *args):
        return internal_connect__(TopBlockPython.connect, self, self.__refs, list.append, *args)

    def disconnect(self, *args):
        return internal_connect__(TopBlockPython.disconnect, self, self.__refs, list.remove, *args)

class HierBlock(HierBlockPython):
    def __init__(self, *args, **kwargs):
        HierBlockPython.__init__(self, *args, **kwargs)
        self.__refs = list()

    def connect(self, *args):
        return internal_connect__(HierBlockPython.connect, self, self.__refs, list.append, *args)

    def disconnect(self, *args):
        return internal_connect__(HierBlockPython.disconnect, self, self.__refs, list.remove, *args)

%}
