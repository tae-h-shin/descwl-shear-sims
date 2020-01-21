import numpy as np
import warnings

# default mask bits from the stack
BAD_COLUMN = np.int64(2**0)
COSMIC_RAY = np.int64(2**3)
EDGE = np.int64(2**4)


# double check they match the stack
def _check_bits_against_stack():
    try:
        import lsst.afw.image as afw_image

        mask = afw_image.Mask()
        cr_val = 2**mask.getMaskPlane('CR')
        bad_val = 2**mask.getMaskPlane('BAD')
        edge_val = 2**mask.getMaskPlane('EDGE')

        if (cr_val != COSMIC_RAY or
                bad_val != BAD_COLUMN or
                edge_val != EDGE):
            warnings.warn(
                "simulation bit mask flags do not match those of the DM stack")

    except ImportError:
        warnings.warn(
            "the DM stack could not be imported to check the simulation "
            "bit mask flags")


# do this here
_check_bits_against_stack()
