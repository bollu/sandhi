#!/usr/bin/env python
#
# Copyright 2004,2007,2010,2011 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#

from gnuradio import gr, gr_unittest
import math


class test_pll_carriertracking (gr_unittest.TestCase):

    def setUp(self):
        self.tb = gr.top_block()

    def tearDown(self):
        self.tb = None

    def test_pll_carriertracking(self):
        expected_result = ((1.00000238419 + 7.21919457547e-09j),
                           (0.998025715351 + 0.062790453434j),
                           (0.992777824402 + 0.119947694242j),
                           (0.985192835331 + 0.171441286802j),
                           (0.976061582565 + 0.217501848936j),
                           (0.966034710407 + 0.258409559727j),
                           (0.95565611124 + 0.294477283955j),
                           (0.945357382298 + 0.326030552387j),
                           (0.935475051403 + 0.353395611048j),
                           (0.926258146763 + 0.376889169216j),
                           (0.917895197868 + 0.39681750536j),
                           (0.910515546799 + 0.413470208645j),
                           (0.904196679592 + 0.427117019892j),
                           (0.898972511292 + 0.438006043434j),
                           (0.894769787788 + 0.446523308754j),
                           (0.891652584076 + 0.452715367079j),
                           (0.8895829916 + 0.456773489714j),
                           (0.888502895832 + 0.458873122931j),
                           (0.888343691826 + 0.459175437689j),
                           (0.889035582542 + 0.457833081484j),
                           (0.890497922897 + 0.454985737801j),
                           (0.892645597458 + 0.450762689114j),
                           (0.895388305187 + 0.445282936096j),
                           (0.898648142815 + 0.438664674759j),
                           (0.902342617512 + 0.431016951799j),
                           (0.906392872334 + 0.422441422939j),
                           (0.910642921925 + 0.413191765547j),
                           (0.915039420128 + 0.403358519077j),
                           (0.919594764709 + 0.392864197493j),
                           (0.92425006628 + 0.381792247295j),
                           (0.928944349289 + 0.370217680931j),
                           (0.933634519577 + 0.358220815659j),
                           (0.938279032707 + 0.345874190331j),
                           (0.942840516567 + 0.333247303963j),
                           (0.947280526161 + 0.32040438056j),
                           (0.951574921608 + 0.307409763336j),
                           (0.955703914165 + 0.294323593378j),
                           (0.959648966789 + 0.281201630831j),
                           (0.963392794132 + 0.268095195293j),
                           (0.966880619526 + 0.255221515894j),
                           (0.970162451267 + 0.242447137833j),
                           (0.973235487938 + 0.229809194803j),
                           (0.97609680891 + 0.217341512442j),
                           (0.978744983673 + 0.20507311821j),
                           (0.981189727783 + 0.193033605814j),
                           (0.983436584473 + 0.181248426437j),
                           (0.985490739346 + 0.169738590717j),
                           (0.987353682518 + 0.158523857594j),
                           (0.989041447639 + 0.147622272372j),
                           (0.990563035011 + 0.137049794197j),
                           (0.991928339005 + 0.126818582416j),
                           (0.993117690086 + 0.117111675441j),
                           (0.994156062603 + 0.107930034399j),
                           (0.995076179504 + 0.0990980416536j),
                           (0.995887458324 + 0.0906178802252j),
                           (0.996591091156 + 0.0824909061193j),
                           (0.997202515602 + 0.0747182965279j),
                           (0.997730851173 + 0.0672992765903j),
                           (0.998185396194 + 0.0602316558361j),
                           (0.99856698513 + 0.0535135567188j),
                           (0.998885989189 + 0.0471420884132j),
                           (0.99915266037 + 0.0411129891872j),
                           (0.999372899532 + 0.0354214012623j),
                           (0.999548316002 + 0.0300626158714j),
                           (0.999680638313 + 0.0252036750317j),
                           (0.999784469604 + 0.020652115345j),
                           (0.999865531921 + 0.0163950324059j),
                           (0.999923825264 + 0.0124222636223j),
                           (0.999960243702 + 0.00872156023979j),
                           (0.999983668327 + 0.00528120994568j),
                           (0.999997138977 + 0.00209015607834j),
                           (1.00000119209 - 0.00086285173893j),
                           (0.999992132187 - 0.00358882546425j),
                           (0.999979138374 - 0.00609711557627j),
                           (0.999963641167 - 0.00839691981673j),
                           (0.999947249889 - 0.0104993218556j),
                           (0.999924004078 - 0.0122378543019j),
                           (0.999904811382 - 0.0136305987835j),
                           (0.999888062477 - 0.0148707330227j),
                           (0.9998742342 - 0.0159679055214j),
                           (0.999856114388 - 0.0169314742088j),
                           (0.999839782715 - 0.0177700817585j),
                           (0.999826967716 - 0.0184917747974j),
                           (0.999818325043 - 0.0191045701504j),
                           (0.999807476997 - 0.0196143388748j),
                           (0.999797284603 - 0.0200265944004j),
                           (0.999791204929 - 0.0203481912613j),
                           (0.99978852272 - 0.0205836892128j),
                           (0.99978530407 - 0.0207380950451j),
                           (0.999785065651 - 0.0206423997879j),
                           (0.999787807465 - 0.0204866230488j),
                           (0.999794304371 - 0.0202808082104j),
                           (0.999800384045 - 0.0200312435627j),
                           (0.999803245068 - 0.0197458267212j),
                           (0.9998087883 - 0.0194311738014j),
                           (0.999816894531 - 0.0190933048725j),
                           (0.999825954437 - 0.0187371373177j),
                           (0.999829888344 - 0.0183679759502j),
                           (0.999835848808 - 0.017987690866j),
                           (0.999844014645 - 0.0176006518304j))

        sampling_freq = 10e3
        freq = sampling_freq / 100

        loop_bw = math.pi / 100.0
        maxf = 1
        minf = -1

        src = gr.sig_source_c(sampling_freq, gr.GR_COS_WAVE, freq, 1.0)
        pll = gr.pll_carriertracking_cc(loop_bw, maxf, minf)
        head = gr.head(gr.sizeof_gr_complex, int(freq))
        dst = gr.vector_sink_c()

        self.tb.connect(src, pll, head)
        self.tb.connect(head, dst)

        self.tb.run()
        dst_data = dst.data()
        self.assertComplexTuplesAlmostEqual(expected_result, dst_data, 5)

if __name__ == '__main__':
    gr_unittest.run(test_pll_carriertracking, "test_pll_carriertracking.xml")
