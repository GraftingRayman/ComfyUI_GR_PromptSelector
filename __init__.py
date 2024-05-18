from .nodes import GRPromptSelector, GRImageResize, GRMaskResize, GRMaskCreate, GRMultiMaskCreate, GRImageSize, GRTileImage
NODE_CLASS_MAPPINGS = { "GR Prompt Selector" : GRPromptSelector , "GR Image Resize" : GRImageResize, "GR Mask Resize" : GRMaskResize, "GR Mask Create" : GRMaskCreate, "GR Multi Mask Create" : GRMultiMaskCreate, "GR Image Size": GRImageSize, "GR Tile and Border Image": GRTileImage }
NODE_DISPLAY_NAME_MAPPINGS = { }
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']

