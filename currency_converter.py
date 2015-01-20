
def get_exchange_rate(rates, cu_from, cu_to):
    exch_tuple = [conv_element
                  for conv_element in rates
                  if conv_element[0] == cu_from and conv_element[1] == cu_to]
    if exch_tuple == []:
        return 0
    else:
        return exch_tuple[0][2]


def convert(rates, value, cu_from, cu_to):
    if cu_from == cu_to:
        return value
    else:
        exch_converter = get_exchange_rate(rates, cu_from, cu_to)
        return exch_converter*value
