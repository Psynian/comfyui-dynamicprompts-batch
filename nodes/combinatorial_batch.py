from functools import lru_cache

from dynamicprompts.enums import SamplingMethod
from dynamicprompts.sampling_context import SamplingContext

from .sampler_batch import DPAbstractSamplerBatchNode

class DPCombinatorialGeneratorBatch(DPAbstractSamplerBatchNode):
    @property
    @lru_cache(maxsize=1)
    def context(self) -> SamplingContext:
        return SamplingContext(
            wildcard_manager=self._wildcard_manager,
            default_sampling_method=SamplingMethod.COMBINATORIAL,
        )
