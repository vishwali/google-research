# coding=utf-8
# Copyright 2024 The Google Research Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Script for computing ellipse plot."""

import matplotlib.pyplot as plt

from k_norm import ellipse_norm_compare


max_d = 1000
k_range = range(1, int(max_d / 2))

# The following code computes the mean squared l_2 norms of samples from the
# minimal ellipsoid and l_2 ball for the problems of Count and Vote. For Count,
# the ambient dimension is d = 1000, an dthe l_0 bound k varies from 1 to 499.
# For Vote, the ambient dimension d varies from 2 to 999.

count_results = [
    ellipse_norm_compare.compare_count_ball_ellipse_norms(max_d, k)
    for k in k_range
]
plt.plot(
    k_range,
    count_results,
    label="Count",
    linestyle="dotted",
    color="olive",
    linewidth=2,
)
d_range = range(2, max_d)
vote_results = [
    ellipse_norm_compare.compare_vote_ball_ellipse_norms(d) for d in d_range
]

# The following code plots the data generated by the two experiments above, on a
# single plot.

plt.plot(
    d_range,
    vote_results,
    label="Vote",
    linestyle="dashed",
    color="teal",
    linewidth=2,
)
plt.xlabel("$k$ or $d$", fontsize=12)
plt.ylabel("expected squared $\ell_2$ norm ratio",  # pylint: disable=anomalous-backslash-in-string
           fontsize=12)
plt.legend(fontsize=12)
plt.title("Ellipse vs. $\ell_2$ Ball",  # pylint: disable=anomalous-backslash-in-string
          fontsize=12)
title = "ellipse_plot"
plt.savefig(title + ".pdf", bbox_inches="tight")