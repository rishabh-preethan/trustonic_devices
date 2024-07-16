import requests
import pandas as pd
import openpyxl

url = "https://mcprod.store.ais.th/graphql?query=query%20products(%24filter%3AProductAttributeFilterInput!%24sort%3AProductAttributeSortInput%24pageSize%3AInt!%24currentPage%3AInt!)%7Bproducts(filter%3A%24filter%20sort%3A%24sort%20pageSize%3A%24pageSize%20currentPage%3A%24currentPage)%7Btotal_count%20items%7Bid%20name%20created_at%20sku%20product_subtype%20brand%20recommended_item%20capacity%20capacity_config%20url_subdirectory_1%20url_subdirectory_2%20additional_image_urls%20network_compatibility%20primary_image_url%20thumbnail_url%20pre_booking_item%20min_bundle_price%20type_of_product%20price%7BregularPrice%7Bamount%7Bvalue%20currency%20__typename%7D__typename%7D__typename%7Dprice_range%7Bminimum_price%7Bregular_price%7Bvalue%20currency%20__typename%7D__typename%7Dmaximum_price%7Bregular_price%7Bvalue%20currency%20__typename%7D__typename%7D__typename%7Dcategories%7Bid%20__typename%7D...on%20ConfigurableProduct%7Bconfigurable_options%7Bid%20label%20attribute_code%20values%7Bvalue_index%20label%20__typename%7Dproduct_id%20__typename%7Dvariants%7Bproduct%7Bid%20name%20sku%20color_code%20capacity_config%20...on%20PhysicalProductInterface%7Bweight%20__typename%7Dprice_range%7Bminimum_price%7Bregular_price%7Bvalue%20currency%20__typename%7D__typename%7D__typename%7D__typename%7Dattributes%7Blabel%20code%20value_index%20__typename%7D__typename%7D__typename%7D__typename%7D__typename%7D%7D&operationName=products&variables=%7B%22filter%22%3A%7B%22category_uid%22%3A%7B%22in%22%3A%5B%22MTU%3D%22%2C%22MTY%3D%22%2C%22MTc%3D%22%2C%22MTg%3D%22%2C%22MTQ%3D%22%2C%22MjA%3D%22%2C%22MjM%3D%22%2C%22MjQ%3D%22%2C%22MjU%3D%22%2C%22MTk%3D%22%2C%22Mjc%3D%22%2C%22MjY%3D%22%2C%22Mjk%3D%22%2C%22MzA%3D%22%2C%22MzE%3D%22%2C%22MzI%3D%22%2C%22Mjg%3D%22%2C%22MzQ%3D%22%2C%22MzM%3D%22%2C%22MzY%3D%22%2C%22MzU%3D%22%2C%22NjE%3D%22%2C%22NjI%3D%22%2C%22NjM%3D%22%2C%22NjQ%3D%22%2C%22NjA%3D%22%2C%22NzQ%3D%22%2C%22NzU%3D%22%5D%7D%2C%22price%22%3A%7B%22from%22%3A%220.01%22%7D%2C%22url_subdirectory_1%22%3A%7B%22eq%22%3A%22phones%22%7D%7D%2C%22sort%22%3A%7B%22recommended_item%22%3A%22DESC%22%7D%2C%22pageSize%22%3A1200%2C%22currentPage%22%3A1%7D"
base_url = "https://mcprod.store.ais.th/graphql?query=query%20products(%24filter%3AProductAttributeFilterInput!)%7Bproducts(filter%3A%24filter)%7Bitems%7Bid%20list_of_tariff_plans%20name%20sku%20device_only%20mat_code%20product_subtype%20hot_item_flag%20zero_percent_flag%20ais_smart_flag%20primary_image_url%20type_of_product%20pre_booking_item%20pre_order_date1%20pre_order_date2%20pre_order_delivery_date1%20pre_order_delivery_date2%20pre_order_description%20pre_order_remark%20event_start_date%20event_end_date%20additional_image_urls%20stock_status%20qty%20only_x_left_in_stock%20download_speed%20upload_speed%20play_box%20router%20setup_fee%20price_exc_vat%20charge_type%20contract_term%20data_description%20call_description%20ais_super_wifi_description%20content_description%20privilege_description%20terms_and_conditions%20brand%20operating_system%20processor_type%20capacity%20ram%20wifi%20bluetooth%20usb_type%20size%20transmission_speed%20locate_satellite%20video%20screen_resolution%20battery_life_idle%20battery_life_during_calls%20others%20insurance%20warranty%20main_features%20special_features%20other_features%20common_features%20water_dust_proof%20microphone%20speaker%20gps%20cpu_chip%20camera%20screen_size%20cellular%20sim_card%20power_and_battery%20software_version%20connectivity%20sensor%20sound_image_video%20device_material%20url_subdirectory_1%20url_subdirectory_2%20__typename%20description%7Bhtml%20__typename%7Dprice_range%7Bminimum_price%7Bregular_price%7Bvalue%20currency%20__typename%7D__typename%7D__typename%7Dcategories%7Bid%20__typename%7D...on%20ConfigurableProduct%7Bconfigurable_options%7Bid%20attribute_id%20label%20attribute_code%20values%7Bvalue_index%20label%20swatch_data%7Bvalue%20__typename%7D__typename%7Dproduct_id%20__typename%7Dvariants%7Bproduct%7Bid%20name%20sku%20pre_order_date1%20pre_order_date2%20pre_order_delivery_date1%20pre_order_delivery_date2%20pre_order_description%20pre_order_remark%20event_start_date%20event_end_date%20device_only%20mat_code%20color_code%20stock_status%20qty%20only_x_left_in_stock%20device_model%20additional_image_urls%20...on%20PhysicalProductInterface%7Bweight%20__typename%7Dmin_bundle_price%20price_range%7Bminimum_price%7Bregular_price%7Bvalue%20currency%20__typename%7D__typename%7D__typename%7D__typename%7Dattributes%7Blabel%20code%20value_index%20__typename%7D__typename%7D__typename%7D%7D__typename%7D%7D&operationName=products&variables=%7B%22filter%22%3A%7B%22url_subdirectory_2%22%3A%7B%22eq%22%3A%22replacable_value_1%2Freplacable_value_2%22%7D%2C%22url_subdirectory_1%22%3A%7B%22eq%22%3A%22phones%22%7D%2C%22category_uid%22%3A%7B%22in%22%3A%5B%22MTU%3D%22%2C%22MTY%3D%22%2C%22MTc%3D%22%2C%22MTg%3D%22%2C%22MTQ%3D%22%2C%22MjA%3D%22%2C%22MjM%3D%22%2C%22MjQ%3D%22%2C%22MjU%3D%22%2C%22MTk%3D%22%2C%22Mjc%3D%22%2C%22MjY%3D%22%2C%22Mjk%3D%22%2C%22MzA%3D%22%2C%22MzE%3D%22%2C%22MzI%3D%22%2C%22Mjg%3D%22%2C%22MzQ%3D%22%2C%22MzM%3D%22%2C%22MzY%3D%22%2C%22MzU%3D%22%2C%22NjE%3D%22%2C%22NjI%3D%22%2C%22NjM%3D%22%2C%22NjQ%3D%22%2C%22NjA%3D%22%2C%22NzQ%3D%22%2C%22NzU%3D%22%5D%7D%7D%7D"

wb = openpyxl.Workbook()
sheet = wb.active

# Set the column headers
sheet['A1'] = 'Name'
sheet['B1'] = 'Price'

response = requests.get(url)
data = response.json()

# Extract the 'items' list from the response
items = data['data']['products']['items']

# Extract the 'url_subdirectory_2' value from each item and store it in a new list
models = [item['url_subdirectory_2'] for item in items]

# Keep track of the items already added to avoid duplicates
added_items = set()

for model in models:
    try:
        l = model.split('/')
        device_name = l[0]
        device_model = l[1]
        new_url = base_url.replace("replacable_value_1", device_name).replace("replacable_value_2", device_model)
        response = requests.get(new_url)
        data1 = response.json()
        items = data1['data']['products']['items']
        name = items[0]['name']
        if name != 'NA':
            for variant in items[0]['variants']:
                label = variant['attributes'][0]['label']
                price = variant['product']['min_bundle_price']
                # Check if the combination of name and label already exists
                if (device_name, name, label) not in added_items:
                    added_items.add((device_name, name, label))
                    sheet.append([device_name, name + ' ' + label, price])
        print(name)
    except:
        print("failed")
        continue

# Save the Excel file
wb.save('AIS.xlsx')