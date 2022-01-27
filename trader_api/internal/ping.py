from fastapi import APIRouter

router = APIRouter(
    prefix='/_internal',
)


@router.get('/ping')
def read_ping():
    return {'result': 'pong'}
