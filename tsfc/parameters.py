import numpy


PARAMETERS = {
    "quadrature_rule": "auto",
    "quadrature_degree": "auto",

    # Default mode
    "mode": "spectral",

    # Maximum extent to unroll index sums. Default is 3, so that loops
    # over geometric dimensions are unrolled; this improves assembly
    # performance.  Can be disabled by setting it to None, False or 0;
    # that makes compilation time much shorter.
    "unroll_indexsum": 3,

    # Scalar type numpy dtype
    "scalar_type": numpy.float64,

    # So that tests pass (needs to match scalar_type)
    "scalar_type_c": "double",

    # Precision of float printing (number of digits)
    "precision": numpy.finfo(numpy.dtype("double")).precision,
}


def default_parameters():
    return PARAMETERS.copy()


def is_complex(scalar_type):
    """Decides complex mode based on scalar type."""
    return scalar_type and (isinstance(scalar_type, numpy.dtype) and scalar_type.kind == 'c') \
        or (isinstance(scalar_type, str) and "complex" in scalar_type)
