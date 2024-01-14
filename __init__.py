from data.data_handler import prep_data, match_data
from whatsapp_wrapped import get_yearly_wrapped

imported_file_path = 'whatsapp-wrapped/data/original_data/sugus_chat.txt'
prepped_data_file_path = 'whatsapp-wrapped/data/prepped_data.txt'

prep_data(imported_file_path, prepped_data_file_path)
#get_yearly_wrapped_stats(scan_data(prepped_data_file), 5, 2023)
df = match_data(prepped_data_file_path)

get_yearly_wrapped(df, '2023', 5)