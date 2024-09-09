# Copyright (c) OpenMMLab. All rights reserved.
from .configurable import (DAFLDataFreeDistillation, DataFreeDistillation,
                           FpnTeacherDistill, OverhaulFeatureDistillation,
                           SelfDistill, SingleTeacherDistill)
#from .configurable import (base, crosskd_gfl, crosskd_single_stage, single_stage
#)

__all__ = [
    'SingleTeacherDistill', 'FpnTeacherDistill', 'SelfDistill',
    'DataFreeDistillation', 'DAFLDataFreeDistillation',
    'OverhaulFeatureDistillation',
    'base', 'crosskd_gfl', 'crosskd_single_stage', 'single_stage'
]
