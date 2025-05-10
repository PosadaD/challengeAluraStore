import pandas

tienda1_df = pandas.read_csv("base-de-datos-challenge1-latam/tienda_1.csv", header='infer');
tienda2_df = pandas.read_csv("base-de-datos-challenge1-latam/tienda_2.csv", header='infer');
tienda3_df = pandas.read_csv("base-de-datos-challenge1-latam/tienda_3.csv", header='infer');
tienda4_df = pandas.read_csv("base-de-datos-challenge1-latam/tienda_4.csv", header='infer');

tiendas = [tienda1_df, tienda2_df, tienda3_df, tienda4_df];

#HEADERS
#'Producto' 'Categoría del Producto' 'Precio' 'Costo de envío' 'Fecha de Compra' 'Vendedor' 'Lugar de Compra' 'Calificación' 'Método de pago' 'Cantidad de cuotas' 'lat' 'lon'

facturacion = {};
categoriasporTienda = {};
calificacionPromedioTienda = {};
masVendidos = {}
costoEnivoPromedioTienda = {}

for x in range(1, 5):
    tienda = tiendas[x-1]
    totalFacturacion = 0;

    for y in range(0, len(tienda)):
        
        # 1. Análisis de facturación
        #facturacion total de cada tienda 
        precio = tienda.loc[y, "Precio"];
        totalFacturacion += precio

    facturacion[f"tienda_{x}"] = float(totalFacturacion);


    # 2. Ventas por categoría
    # categorias mas populares 
    ventaCategoria = tienda["Categoría del Producto"].value_counts(); 
    ventaCategoria = ventaCategoria.to_dict()
    categoriasporTienda[f"tienda_{x}"] = ventaCategoria;

            
    # 3. Calificación promedio de la tienda
    #Promedio de calificacion de los clientes
    calificaciones = tienda["Calificación"];
    calificaciones = calificaciones.to_list();
    calificacionPromedioTienda[f"tienda_{x}"] = round(sum(calificaciones) / len(tienda), 2);


    # 4. Productos más y menos vendidos
    ventasProducto = tienda["Producto"].value_counts(); 
    ventasProducto = ventasProducto.to_dict()
    masVendidos[f"tienda_{x}"] = ventasProducto;


    # 5. Envío promedio por tienda    
    #costo pormedio de envio 
    costoEnvio = tienda["Costo de envío"];
    costoEnvio = costoEnvio.to_list();
    costoEnivoPromedioTienda[f"tienda_{x}"] = round(sum(costoEnvio) / len(tienda), 2);


# print(facturacion);
# print(categoriasporTienda);
# print(calificacionPromedioTienda);
# print(masVendidos);
# print(costoEnivoPromedioTienda);



     
##conclusion: 
# Tienda 4 tiene la facturación más baja, pero tiene una calificación promedio bastante competitiva (4.00), similar a la de Tienda 1 (3.98). Sin embargo, su facturación es significativamente más baja que las demás tiendas, lo que podría indicar que su rendimiento general no está a la par con las otras tiendas.

# Tienda 1 tiene una facturación más alta, pero su calificación es la más baja (3.98), lo que podría sugerir problemas con la satisfacción del cliente.

# En base a estos factores, la Tienda 4 parece ser la candidata más probable para cerrar, dado que tiene una combinación de menor facturación y una cantidad de productos populares no muy destacada. Sin embargo, si la satisfacción del cliente es más crítica, la Tienda 1 también podría ser considerada debido a su baja calificación.