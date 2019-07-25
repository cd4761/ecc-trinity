from eth.consensus import (
    pow,
)

from eth.rlp.blocks import (
    BaseBlock,
)


class POWMiningMixin:
    """
    A VM that does POW mining as well. Should be used only in tests, when we
    need to programatically populate a ChainDB.
    """
    def finalize_block(self, block: BaseBlock) -> BaseBlock:
        block = super().finalize_block(block)  # type: ignore
        nonce, mix_hash = pow.mine_eccpow_nonce(
            block.header.parent_hash, block.header.mining_hash, 24, 3, 6)
        # return block.copy(header=block.header.copy(nonce=nonce))

        return block.copy(header=block.header.copy(nonce=nonce, mix_hash=mix_hash))
