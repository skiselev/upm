// Include doxygen-generated documentation
%include "pyupm_doxy2swig.i"
%module pyupm_th02
%include "../upm.i"

%include "th02.hpp"
%{
    #include "th02.hpp"
%}
