from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_root():
    return {"Hello": "World"}

@router.post("/transfer-history")
async def get_transfer_history(request: TransferHistoryRequest):
    # Implement the logic to process the request and return the response
    response = TransferHistoryResponse(
        PointCount=request.GetPerPage * request.PageNo,
        Result={}
    )
    return response