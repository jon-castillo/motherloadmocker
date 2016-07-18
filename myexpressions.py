def sub_regexmodifier_repeating(input):
    output = '(?:'+input+')+'
    return output

def sub_regexmodifier_match(input):
    output = '('+input+')'
    return output

def sub_regexmodifier_optional(input):
    output = '(?:'+input+'){0,1}'
    return output

def sub_regexmodifier_capture(input):
    output = '('+input+')'
    return output

str_regexpattern_core_space = '(?:\s+)'
str_regexpattern_core_spaceOrNoSpace = '(?:\s*)'
str_regexpattern_core_value = '(?:[\w:_]+)'
str_regexpattern_core_repeatedreferencedereference = '(?:[\*\&]*)'
str_regexpattern_core_variableName = '(?:[~\w:_]+)'
str_regexpattern_core_memberName = '(?:[~\w:_\<\>\+\-\*\/\=]+)(?:\s*)'
str_regexpattern_core_variableType =                        \
    str_regexpattern_core_variableName +                    \
    sub_regexmodifier_optional(                             \
        str_regexpattern_core_spaceOrNoSpace +              \
        str_regexpattern_core_repeatedreferencedereference  \
    )

str_regexpattern_method_specifierFront = '(?:(?:virtual|explicit)\s+)+'
str_regexpattern_method_returnType = str_regexpattern_core_variableType+ str_regexpattern_core_space
str_regexpattern_method_parameterlist =                     \
    sub_regexmodifier_repeating(                            \
        str_regexpattern_core_spaceOrNoSpace +              \
        str_regexpattern_core_variableType +                \
        str_regexpattern_core_spaceOrNoSpace +                       \
        sub_regexmodifier_optional(                         \
            str_regexpattern_core_variableName +            \
            sub_regexmodifier_optional(                     \
                str_regexpattern_core_spaceOrNoSpace +      \
                '=' +                                       \
                str_regexpattern_core_spaceOrNoSpace +      \
                str_regexpattern_core_variableName          \
            ) +                                             \
            sub_regexmodifier_optional(                     \
                str_regexpattern_core_spaceOrNoSpace +      \
                ','                                        \
            ) \
        )                                                   \
    )

str_regexpattern_method_initializerlist =                   \
    sub_regexmodifier_repeating(                            \
        str_regexpattern_core_variableName +                \
        str_regexpattern_core_spaceOrNoSpace +              \
        '\(' +                                              \
        str_regexpattern_core_spaceOrNoSpace +              \
        str_regexpattern_core_value +                       \
        str_regexpattern_core_spaceOrNoSpace +              \
        '\)' +                                              \
        sub_regexmodifier_optional(                         \
            '\s*,\s*'                                       \
        )                                                   \
    )

str_regexpattern_method_specifierBack = '(?:(?:override|final|const)\s*)+'

str_regexpattern_method_cppmethod=                                                  \
    '^' +                                                                           \
    str_regexpattern_core_spaceOrNoSpace +                                          \
    sub_regexmodifier_capture(sub_regexmodifier_optional(str_regexpattern_method_specifierFront )) +                    \
    sub_regexmodifier_capture(sub_regexmodifier_optional(str_regexpattern_method_returnType)) +                         \
    sub_regexmodifier_capture(str_regexpattern_core_memberName)+'\s*'+'\(' +                                         \
    str_regexpattern_core_spaceOrNoSpace +                                          \
    sub_regexmodifier_capture(sub_regexmodifier_optional(str_regexpattern_method_parameterlist)) +                                \
    str_regexpattern_core_spaceOrNoSpace +                                          \
    '\)'+                                                                           \
    str_regexpattern_core_spaceOrNoSpace +                                          \
    sub_regexmodifier_optional(                             \
        ':' +                                               \
        str_regexpattern_core_spaceOrNoSpace +                                          \
        sub_regexmodifier_capture(str_regexpattern_method_initializerlist))                     \
     + \
    str_regexpattern_core_spaceOrNoSpace +                                          \
    sub_regexmodifier_capture(sub_regexmodifier_optional(str_regexpattern_method_specifierBack)) +                      \
    str_regexpattern_core_spaceOrNoSpace +                                          \
    sub_regexmodifier_optional('[;|{]')


str_debug_specifierfront = sub_regexmodifier_capture(sub_regexmodifier_optional(str_regexpattern_method_specifierFront ))
str_debug_returntype = sub_regexmodifier_capture(sub_regexmodifier_optional(str_regexpattern_method_returnType))
str_debug_methodname =  sub_regexmodifier_capture(str_regexpattern_core_memberName)+'\s*'+'\('
str_debug_paramlist = sub_regexmodifier_capture(sub_regexmodifier_optional(str_regexpattern_method_parameterlist))
str_debug_initlist = '\)'+ str_regexpattern_core_spaceOrNoSpace + sub_regexmodifier_optional(':'+str_regexpattern_core_spaceOrNoSpace + sub_regexmodifier_capture( str_regexpattern_method_initializerlist))
str_debug_specifierback = str_regexpattern_core_spaceOrNoSpace+sub_regexmodifier_capture(sub_regexmodifier_optional(str_regexpattern_method_specifierBack)) + str_regexpattern_core_spaceOrNoSpace + sub_regexmodifier_optional('[;|{]')
#1.	virtual explicit
#2.	int
#3.	caller
#4.	void
#5.	mymock(a),mybb(v)
#6.	mybb
#7.	final override const


