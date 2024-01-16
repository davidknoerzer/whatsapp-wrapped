from data.data_handler import prep_data, match_data
from whatsapp_wrapped import get_yearly_wrapped

imported_file_path = 'whatsapp-wrapped/data/original_data/sugus_chat.txt'
#imported_file_path = 'whatsapp-wrapped/data/original_data/ohana_chat.txt'
prepped_data_file_path = 'whatsapp-wrapped/data/prepped_data.txt'

prep_data(imported_file_path, prepped_data_file_path)
df = match_data(prepped_data_file_path)

year = '2023'

get_yearly_wrapped(df, year, 3)