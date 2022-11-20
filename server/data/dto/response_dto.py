from pydantic import BaseModel

from server.data.dto_mapper import dto_indexed_from_branch_indexed


class FindBranchResponseDto(BaseModel):
    size: int
    result: list


def find_branch_response(branches: list) -> FindBranchResponseDto:
    response = FindBranchResponseDto.construct()
    response.size = len(branches)
    response.result = list(dto_indexed_from_branch_indexed(branch).dict(by_alias=True) for branch in branches)
    return response
