import index
import matplotlib.pyplot as plt

calificacion = index.calificacionPromedioTienda
facturacion = index.facturacion
envio = index.costoEnivoPromedioTienda

# Graficar facturación por tienda
plt.plot(facturacion.keys(), facturacion.values())
plt.title('Facturación por Tienda')
plt.xlabel('Tiendas')
plt.ylabel('Facturación')
# Guardar la figura en un archivo PNG
plt.savefig('facturacion_por_tienda.png')
# Si no se muestra el gráfico, guarda y abre la imagen manualmente
plt.close()


# Graficar calificacion promedio por tienda
plt.plot(calificacion.keys(), calificacion.values())
plt.title('Calificacion promedio por Tienda')
plt.xlabel('Tiendas')
plt.ylabel('Calificacion')
# Guardar la figura en un archivo PNG
plt.savefig('calificacion_por_tienda.png')
# Si no se muestra el gráfico, guarda y abre la imagen manualmente
plt.close()


# Graficar envio promedio por tienda
plt.plot(envio.keys(), envio.values())
plt.title('Envio promedio por Tienda')
plt.xlabel('Tiendas')
plt.ylabel('Envio')
# Guardar la figura en un archivo PNG
plt.savefig('envio_por_tienda.png')
# Si no se muestra el gráfico, guarda y abre la imagen manualmente
plt.close()