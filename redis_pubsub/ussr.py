# USSR New Redis impl.
from globs.caches import beatmaps

async def drop_bmap_cache_pubsub(data: bytes) -> None:
    """
    Handles the `ussr:bmap_decache`.
    Drops the beatmap from cache. Takes in a string that is the beatmap md5.
    """
    
    beatmaps.drop(data.decode())

# TODO: Add verify handler.
