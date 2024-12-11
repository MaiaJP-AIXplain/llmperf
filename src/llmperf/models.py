from typing import Any, Dict, List, Optional, Tuple
from pydantic import BaseModel


class RequestConfig(BaseModel):
    """The configuration for a request to the LLM API.

    Args:
        model: The model to use.
        prompt: The prompt to provide to the LLM API.
        sampling_params: Additional sampling parameters to send with the request.
            For more information see the Router app's documentation for the completions
        llm_api: The name of the LLM API to send the request to.
        metadata: Additional metadata to attach to the request for logging or validation purposes.
        header_params: Additional header parameters to send with the request.
        verify_ssl: Whether to verify SSL certificates when making requests. Defaults to True.
    """

    model: str
    prompt: Tuple[str, int]
    sampling_params: Optional[Dict[str, Any]] = None
    llm_api: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    header_params: Optional[Dict[str, Any]] = None
    verify_ssl: Optional[bool] = True