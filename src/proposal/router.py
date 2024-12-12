from fastapi import APIRouter

from proposal.schemas import ProposalEvaluationRequestDto, ProposalEvaluationResponseDto, SummaryGenerationRequestDto, SummaryDto
from proposal.service import proposal_evaluation, summary_generation

router = APIRouter()


@router.post("/gen/proposal/evaluation")
def proposal_evaluation_router(request: ProposalEvaluationRequestDto) -> ProposalEvaluationResponseDto:
    return proposal_evaluation(request)


@router.post("/gen/proposal/summary")
def summary_generation_router(request: SummaryGenerationRequestDto) -> ProposalEvaluationResponseDto:
    return summary_generation(request)
