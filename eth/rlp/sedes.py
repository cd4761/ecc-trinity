from rlp.sedes import (
    BigEndianInt,
    Binary,
)


address = Binary.fixed_length(20, allow_empty=True)
hash32 = Binary.fixed_length(32)
uint24 = BigEndianInt(24)
uint32 = BigEndianInt(32)
uint64 = BigEndianInt(64)
uint256 = BigEndianInt(256)
trie_root = Binary.fixed_length(32, allow_empty=True)
