import pytest

from eth.chains.base import MiningChain
from eth.chains.mainnet import MAINNET_VMS
from eth.consensus.pow import check_eccpow
from eth.tools.mining import POWMiningMixin
from eth.tools.builder.chain import (
    genesis,
)


@pytest.mark.parametrize(
    'base_vm_class',
    MAINNET_VMS,
)
def test_mining_tools_proof_of_work_mining(base_vm_class):
    vm_class = type(base_vm_class.__name__, (POWMiningMixin, base_vm_class), {})

    class ChainClass(MiningChain):
        vm_configuration = (
            (0, vm_class),
        )

    chain = genesis(ChainClass)

    block = chain.mine_block()
    check_eccpow(
        block.header.parent_hash,
        block.header.mining_hash,
        24,
        3,
        6
    )
