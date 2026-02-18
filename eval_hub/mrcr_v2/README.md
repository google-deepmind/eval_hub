## MRCR V2 ##
Google DeepMind is open-sourcing its internal version of the MRCR task, as well
as providing code to generate alternate versions of the task.
Please cite https://arxiv.org/abs/2409.12640v2 if you use this evaluation.

MRCR stands for "multi-round coreference resolution" and is a minimally simple
long-context reasoning evaluation testing the length generalization capabilities
of the model to follow a simple reasoning task with a fixed complexity:
count instances of a body of text and reproduce the correct instance. The model
is presented with a sequence of user-assistant turns where the user requests a
piece of writing satisfying a format/style/topic tuple, and the assistant
responds with a piece of writing. At the end of this sequence, the model is
asked to reproduce the i<sup>th</sup> instance of the assistant output for one
of the user queries (all responses to the same query are distinct). The model is
also asked to certify that it will produce that output by first outputting a
specialized and unique random string beforehand.

The MRCR task is described in the Michelangelo paper in more detail
(https://arxiv.org/abs/2409.12640v2) and has been reported by GDM on subsequent
model releases. At the time of this release, we currently report the 8-needle
version of the task on the "upto_128K" (cumulative) and "at_1M" pointwise
variants. This release includes evaluation scales up to 8M, and sufficient
resolution at multiple context lengths to produce total context vs. performance
curves (for instance, as https://contextarena.ai demonstrates.)

### NOISE RATES ###
We have estimated the noise rate for this task under two noise model assumptions
(code available in this repository).

If we assume the model simply reproduces any of the assistant responses
uniformly at random, the resulting noise rate under the MRCR metric is ~1%.
This estimate holds across contexts and number of needles.

If we assume the model reproduces one of the **relevant** assistant responses
uniformly at random, the resulting noise rate under the MRCR metric is
~(1/num_relevant_needles) (typically, a couple percent more), again holding
across context lengths and the number of needles. The noise rate for 2-needle is
around 51%, for 4-needle around 27%, and for 8-needle around 15%.

Of course, it is possible for a model to underperform these noise models by not
outputting something from the context or by not following the correct formatting
specified in the instructions.

### USAGE ###

MRCR can be used to evaluate the ability of LLMs to solve simple relatively
simple reasoning tasks over long context inputs. It should be noted, however,
that if the model is given access to code tools, the task becomes
considerably simpler. Any report of MRCR should explicitly state whether or not
tools were provided to the model, as otherwise the comparison is not meaningful
(it tests a completely different capability).

### INSTRUCTIONS ###

1. Download the desired data-subset via download.sh. You can select by
num_needles and maximum context length.

2. The run_evaluation.py function has an example setup for evaluating the model.
We provide a default evaluation mode identical to the setup we use to report
MRCR numbers, as well as a more lenient version of the metric.

3. We also support generating your own versions of MRCR. We have provided the
code to generate your own MRCR instance, as well as test (see run_mrcr_tests in
analysis_utils.py) and visualization utilities to test and check the
distributions of the contexts and needle positions so that they are relatively
uniform across the context.

### FEATURES ###

1. Prefix-cache friendly: The dataset supports prefix-caching, so that model
providers which support prefix-caching will enjoy speed-ups when running evals
on this dataset.

2. Difficulty: The keys consist of a triplet - each writing sample has a writing
format, a topic, and a style as well.
