# Ozon API Import File Generator
This code allows you to obtain an unloading of your goods from the Ozon site and generate an Excel file for import to the Wildberries site. Using the Ozon API, this code can retrieve the following information about your products:

- Price (using the `/v2/product/info`)
- Seller's product code and name (using the `/v2/product/info`)
- Manufacturer code and brand (using the `/v3/products/info/attributes`)
- List of photos (using the `/v3/products/info/attributes`)
- Dimensions: length, width, height (using the `/v3/products/info/attributes`)

Please note that dimensions in millimeters are unloaded from ozone, and centimeters need to be loaded on Wildberries. To accommodate this difference, this code divides the dimensions by 10. Additionally, the dimensions are increased by **1.35** times and the price is increased by **1.20** times compared to the values obtained from ozone. This is necessary if the packaging requirements or the commission of these sites are different. For example, if the product's dimensions in ozone are **100 mm x 200 mm x 300 mm**, the dimensions in the generated import file will be **13.5 cm x 27 cm x 40.5 cm**. Similarly, if the product's price in Ozon is **1000 rubles**, the price in the generated import file will be **1200 rubles**.

## Getting Started
To use this code, you will need to provide your authorization data for the Ozon API. You can do this by adding your client ID and API key to the `Config` class in the `config.py` file.

Once you have provided your authorization data, you can use this code to generate an import file for Wildberries. This will be done by calling the `create_file_for_import` function, which will use the Ozon API to retrieve the necessary data and generate an Excel file for import.

Please note that if you have a large number of goods, the unloading process may take some time. Additionally, the generated import file will be suitable for the Wildberries site, but may need to be modified to be used on other sites.