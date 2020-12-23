from fastapi import APIRouter, Depends, HTTPException

from ..dependencies import get_token_header

router = APIRouter(
    prefix="/conf",
    tags=['conf'],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

conference_db = {
    "B1G": {
        "wisconsin": {"nick_name": ["badgers", 'bucky']},
        "psu": {"nick_name": ["nitany lions", 'who knows?']},
    },
    "SEC": {
        "tennessee": {"nick_name": ["volunteers", 'smokey']},
        "mizzou": {"nick_name": ['tigers', 'stripey']},
    },
    "Big 12": {
        "kansas": {"nick_name": ["jayhawks", 'rock chalk']},
    },
}


@router.get("/")
async def read_items():
    return [json.dumps(conference_db)]


@router.get("/{conf}/{university}")
async def read_item(university: str):
    rv_jason = None
    if c not in conference_db.keys():
        if u not in conference_db[c].keys():
            rv_jason = conference_db[c][uni]
        else:
            conference_db[c][u] = []
    else:
        # conference .... new
        conference_db[conf] = {}
    # {"university": university, "nick_name": names[0], "mascot": names[1]}
    return rv_jason


@router.put("/{university}/{nick_name{/{mascot}")
def update_item(university: str, nick_name: str, mascot: str):
    university_db[university] = [nick_name, mascot]

    return {"university": university, "nick_name": university_db[university][0], 'mascot': university_db[university][1]}


@router.put(
    "/{item_id}",
    tags=["custom"],
    responses={403: {"description": "Operation forbidden"}},
)
async def update_item(item_id: str):
    if item_id != "plumbus":
        raise HTTPException(
            status_code=403, detail="You can only update the item: plumbus"
        )
    return {"item_id": item_id, "name": "The great Plumbus"}
