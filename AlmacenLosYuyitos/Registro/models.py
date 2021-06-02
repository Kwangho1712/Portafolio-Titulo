# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Boleta(models.Model):
    id_boleta = models.CharField(primary_key=True, max_length=9)
    fecha = models.DateField()
    total = models.FloatField()
    subtotal = models.FloatField()

    class Meta:
        managed = False
        db_table = 'boleta'


class Cliente(models.Model):
    run = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=99)
    edad = models.BigIntegerField(blank=True, null=True)
    fiar = models.CharField(max_length=5)
    fiado_id_fiado = models.ForeignKey('Fiado', models.DO_NOTHING, db_column='fiado_id_fiado')

    class Meta:
        managed = False
        db_table = 'cliente'


class DetalleBoleta(models.Model):
    id_boleta = models.CharField(primary_key=True, max_length=10)
    suma_precio = models.FloatField()
    cantidad = models.BigIntegerField()
    producto_cod_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='producto_cod_producto')
    boleta_id_boleta = models.ForeignKey(Boleta, models.DO_NOTHING, db_column='boleta_id_boleta')

    class Meta:
        managed = False
        db_table = 'detalle_boleta'


class DetallePedido(models.Model):
    id_detalle_pedido = models.BigIntegerField(primary_key=True)
    cantidad = models.BigIntegerField()
    suma_precio_compra = models.FloatField()
    producto_cod_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='producto_cod_producto')
    pedido_id_pedido = models.ForeignKey('Pedido', models.DO_NOTHING, db_column='pedido_id_pedido')

    class Meta:
        managed = False
        db_table = 'detalle_pedido'


class DetalleVenta(models.Model):
    id_detalle_venta = models.CharField(primary_key=True, max_length=9)
    cantidad = models.BigIntegerField()
    suma_total = models.FloatField()
    venta_id_venta = models.ForeignKey('Venta', models.DO_NOTHING, db_column='venta_id_venta')
    producto_cod_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='producto_cod_producto')

    class Meta:
        managed = False
        db_table = 'detalle_venta'


class FamiliaProducto(models.Model):
    id_familia_producto = models.CharField(primary_key=True, max_length=3)
    dsc_familia_producto = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'familia_producto'


class Fiado(models.Model):
    id_fiado = models.CharField(primary_key=True, max_length=3)
    monto_fiado = models.FloatField(blank=True, null=True)
    fecha_fiado = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fiado'


class Pedido(models.Model):
    id_pedido = models.CharField(primary_key=True, max_length=3)
    estado = models.CharField(max_length=999)
    fecha_pedido = models.DateField()
    fecha_recepcion = models.DateField(blank=True, null=True)
    proveedor_rut = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='proveedor_rut')

    class Meta:
        managed = False
        db_table = 'pedido'


class Producto(models.Model):
    cod_producto = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    precio_compra = models.FloatField()
    precio_venta = models.FloatField()
    tipo_prod_id_tipo_prod = models.ForeignKey('TipoProducto', models.DO_NOTHING, db_column='tipo_prod_id_tipo_prod')
    fam_prod_id_fam_prod = models.ForeignKey(FamiliaProducto, models.DO_NOTHING, db_column='fam_prod_id_fam_prod')
    stock_id_stock = models.ForeignKey('Stock', models.DO_NOTHING, db_column='stock_id_stock')

    class Meta:
        managed = False
        db_table = 'producto'


class Proveedor(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=99)
    telefono = models.CharField(max_length=13, blank=True, null=True)
    email = models.CharField(max_length=99, blank=True, null=True)
    direccion = models.CharField(max_length=60, blank=True, null=True)
    rubro = models.CharField(max_length=90, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedor'


class Stock(models.Model):
    id_stock = models.CharField(primary_key=True, max_length=20)
    stock_actual = models.FloatField()
    stock_critico = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock'


class TipoProducto(models.Model):
    id_tipo_producto = models.CharField(primary_key=True, max_length=3)
    dsc_tipo_producto = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_producto'


class TipoUsuario(models.Model):
    id_tipo_usuario = models.CharField(primary_key=True, max_length=10)
    dsc_tipo_usuario = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_usuario'


class Usuario(models.Model):
    email = models.CharField(primary_key=True, max_length=99)
    contrasena = models.CharField(max_length=10)
    nombre = models.CharField(max_length=90)
    telefono = models.CharField(max_length=13, blank=True, null=True)
    direccion = models.CharField(max_length=90, blank=True, null=True)
    tipo_usuario_id_tipo_usuario = models.ForeignKey(TipoUsuario, models.DO_NOTHING, db_column='tipo_usuario_id_tipo_usuario')

    class Meta:
        managed = False
        db_table = 'usuario'


class Venta(models.Model):
    id_venta = models.CharField(primary_key=True, max_length=3)
    fecha_venta = models.DateField()
    total = models.FloatField()
    cantidad_productos_total = models.BigIntegerField()
    usuario_email = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='usuario_email')
    fiado_id_fiado = models.ForeignKey(Fiado, models.DO_NOTHING, db_column='fiado_id_fiado')

    class Meta:
        managed = False
        db_table = 'venta'
