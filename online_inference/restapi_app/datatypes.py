from pydantic import BaseModel, conlist


class FeaturesModel(BaseModel):
    feature_names : conlist(item_type=str, min_items=13, max_items=13)
    features : list[conlist(item_type=float, min_items=13, max_items=13)]
    model_type : str


class StatusModel(BaseModel):
    status: int


class PredictResultModel(BaseModel):
    result: list
