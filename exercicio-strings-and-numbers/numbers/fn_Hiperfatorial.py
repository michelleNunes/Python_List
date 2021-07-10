def fn_Hiperfatorial(int_var_n):
    if int_var_n < 1:
        return 1
    else:
        return (int_var_n ** int_var_n) * fn_Hiperfatorial(int_var_n - 1)
