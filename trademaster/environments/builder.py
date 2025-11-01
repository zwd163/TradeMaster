from mmcv.utils import Registry
from trademaster.utils import build_from_cfg
import copy

# Import environment modules to register them
try:
    from . import custom
except ImportError:
    pass

try:
    from .portfolio_management import eiie_environment
except ImportError:
    pass

try:
    from .portfolio_management import deeptrader_environment
except ImportError:
    pass

try:
    from .portfolio_management import sarl_environment
except ImportError:
    pass

try:
    from .portfolio_management import inverstor_imitator_environment
except ImportError:
    pass

try:
    from .algorithmic_trading import environment
except ImportError:
    pass

try:
    from .order_execution import eteo_environment
except ImportError:
    pass

try:
    from .order_execution import pd_environment
except ImportError:
    pass

try:
    from .high_frequency_trading import environment as hft_environment
except ImportError:
    pass

ENVIRONMENTS = Registry('environment')
def build_environment(cfg, default_args=None):
    cp_cfg = copy.deepcopy(cfg.environment)
    print("Registered environments:", list(ENVIRONMENTS.module_dict.keys()))
    print("Requested environment type:", cp_cfg.type)
    environment = build_from_cfg(cp_cfg, ENVIRONMENTS, default_args)
    return environment
