
def get_exchange_rate(rates, cu_from, cu_to):
    exch_tuple = [conv_element
                  for conv_element in rates
                  if cu_from in conv_element and cu_to in conv_element]
    if exch_tuple == []:
        return 0
    else:
        if cu_from == exch_tuple[0][0]:
            return exch_tuple[0][2]
        else:
            return (1/exch_tuple[0][2])


def convert(rates, value, cu_from, cu_to):
    if cu_from == cu_to:
        return value
    else:
        exch_converter = get_exchange_rate(rates, cu_from, cu_to)
        return exch_converter*value
