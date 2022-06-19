from __future__ import annotations

from fastapi import APIRouter
from fastapi import Response

from . import leaderboards
from . import replays
from . import score_sub
from . import screenshots

router = APIRouter(default_response_class=Response)

router.add_api_route("/web/osu-osz2-getscores.php", leaderboards.get_leaderboard)
router.add_api_route(
    "/web/osu-submit-modular-selector.php",
    score_sub.submit_score,
    methods=["POST"],
)

router.add_api_route(
    "/web/osu-screenshot.php",
    screenshots.upload_screenshot,
    methods=["POST"],
)

router.add_api_route("/web/osu-getreplay.php", replays.get_replay)
router.add_api_route("/web/replays/{score_id}", replays.get_full_replay)
