from .GRnodes import GRPromptSelector, GRImageResize, GRMaskResize, GRMaskCreate, GRMultiMaskCreate, GRImageSize, GRTileImage, GRPromptSelectorMulti, GRTileFlipImage, GRMaskCreateRandom, GRStackImage, GRResizeImageMethods, GRImageDetailsDisplayer, GRImageDetailsSave
NODE_CLASS_MAPPINGS = { "GR Prompt Selector" : GRPromptSelector , "GR Image Resize" : GRImageResize, "GR Mask Resize" : GRMaskResize, "GR Mask Create" : GRMaskCreate, "GR Multi Mask Create" : GRMultiMaskCreate, "GR Image Size": GRImageSize, "GR Tile and Border Image": GRTileImage, "GR Prompt Selector Multi": GRPromptSelectorMulti, "GR Tile and Border Image Random Flip" : GRTileFlipImage, "GR Mask Create Random": GRMaskCreateRandom, "GR Stack Image": GRStackImage, "GR Image Resize Methods" : GRResizeImageMethods,"GR Image Details Displayer": GRImageDetailsDisplayer, "GR Image Details Saver": GRImageDetailsSave }
NODE_DISPLAY_NAME_MAPPINGS = { }
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']

