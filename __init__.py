from data.data_handler import prep_data, scan_data
from whatsapp_wrapped import get_yearly_wrapped_stats

imported_file = 'whatsapp-wrapped/data/original_data/sugus_chat.txt'
prepped_data_file = 'whatsapp-wrapped/data/prepped_data.txt'

prep_data(imported_file, prepped_data_file)
get_yearly_wrapped_stats(scan_data(prepped_data_file), 5, 2023)
