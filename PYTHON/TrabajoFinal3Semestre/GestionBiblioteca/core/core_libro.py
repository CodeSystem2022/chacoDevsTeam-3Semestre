import psycopg2
import config.logger_base as logger_base


class ABMLibro:
    MI_BD = 'gestionbiblioteca'
    TABLA = 'libro'
    CONEXION_CONFIG = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432',
                                       database=MI_BD)

    @classmethod
    def nuevo_libro(cls, libro):
        conexion = cls.CONEXION_CONFIG
        try:
            with conexion.cursor() as cursor:
                sentencia = f'INSERT INTO {cls.TABLA} (titulo, genero, anio_publicacion, isbn, autor_id, cantidad) VALUES (%s, %s, %s, %s, %s, %s)'
                valores = (libro.titulo, libro.genero, libro.anio_publicacion, libro.isbn, libro.autor_id, libro.cantidad)
                cursor.execute(sentencia, valores)
                registros_insertados = cursor.rowcount
                print(f'Los registros insertados son: {registros_insertados}')
                logger_base.log.info(f'Los registros insertados son: {valores}')
                conexion.commit()
        except Exception as e:
            print(f'Ocurrio un error {e}')
            logger_base.log.error(f'OCURRIO UN ERROR {e}')

    @classmethod
    def buscar_libro(cls, id_libro):
        conexion = cls.CONEXION_CONFIG
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    sentencia = f'SELECT titulo, genero, autor.nombre, anio_publicacion, isbn FROM {cls.TABLA} JOIN autor ON libro.autor_id = autor.id_autor WHERE id_libro = %s '
                    cursor.execute(sentencia, (id_libro,))
                    registros = cursor.fetchone()
                    print(registros)
        except Exception as e:
            print(f'Ocurrio un error {e}')
            logger_base.log.error(f'OCURRIO UN ERROR {e}')

    @classmethod
    def listar_libros(cls):
        conexion = cls.CONEXION_CONFIG
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    sentencia = f'SELECT titulo, genero, autor.nombre, anio_publicacion, isbn, cantidad FROM {cls.TABLA} JOIN autor ON libro.autor_id = autor.id_autor'
                    cursor.execute(sentencia)
                    registros = cursor.fetchall()
                    for registro in registros:
                        print(registro)
        except Exception as e:
            print(f'Ocurrio un error {e}')
            logger_base.log.error(f'OCURRIO UN ERROR {e}')

    @classmethod
    def borrar_libro(cls, id_libro):
        conexion = cls.CONEXION_CONFIG
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    sentencia = f'DELETE FROM {cls.TABLA} WHERE id_libro=%s'
                    valores = (id_libro,)
                    cursor.execute(sentencia, valores)
                    registros_eliminados = cursor.rowcount
                    print(f'Los registros eliminados son: {registros_eliminados}')
                    logger_base.log.info(f'Los registros eliminados son: {valores}')
        except Exception as e:
            print(f'Ocurrio un error {e}')
            logger_base.log.error(f'OCURRIO UN ERROR {e}')

    @classmethod
    def modificar_libro(cls, libro, id_libro):
        conexion = cls.CONEXION_CONFIG
        try:
            with conexion.cursor() as cursor:
                sentencia = f'UPDATE {cls.TABLA} SET titulo=%s, genero= %s, anio_publicacion=%s, isbn=%s, autor_id=%s WHERE id_libro=%s'
                valores = (libro.titulo, libro.genero, libro.anio_publicacion, libro.isbn, libro.autor_id, id_libro)
                cursor.execute(sentencia, valores)
                registros_actualizados = cursor.rowcount
                print(f'Los registros actualizados son: {registros_actualizados}')
                logger_base.log.info(f'Los registros actualizados son: {valores}')
                conexion.commit()
        except Exception as e:
            print(f'Ocurrio un error {e}')
            logger_base.log.error(f'OCURRIO UN ERROR {e}')

    @classmethod
    def agregar_libro_existente(cls, cantidad, id_libro):
        conexion = cls.CONEXION_CONFIG
        try:
            with conexion.cursor() as cursor:
                sentencia = f'UPDATE {cls.TABLA} SET cantidad=%s WHERE id_libro=%s'
                valores = (cantidad, id_libro)
                cursor.execute(sentencia, valores)
                registros_actualizados = cursor.rowcount
                print(f'Los registros actualizados son: {registros_actualizados}')
                logger_base.log.info(f'Los registros actualizados son: {valores}')
                conexion.commit()
        except Exception as e:
            print(f'Ocurrio un error {e}')
            logger_base.log.error(f'OCURRIO UN ERROR {e}')

    @classmethod
    def buscar_libro_por_titulo(cls, titulo):
        conexion = cls.CONEXION_CONFIG
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    sentencia = f'SELECT id_libro FROM {cls.TABLA} WHERE titulo like %s'
                    cursor.execute(sentencia, (f'%{titulo}%',))
                    registros = cursor.fetchone()
                    return registros
        except Exception as e:
            print(f'Ocurrio un error {e}')
            logger_base.log.error(f'OCURRIO UN ERROR {e}')

    @classmethod
    def buscar_id_libro_por_id(cls, titulo):
        conexion = cls.CONEXION_CONFIG
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    sentencia = f'SELECT id_libro FROM {cls.TABLA} WHERE id_libro = %s'
                    cursor.execute(sentencia, (titulo,))
                    registros = cursor.fetchone()
                    return registros
        except Exception as e:
            print(f'Ocurrio un error {e}')
            logger_base.log.error(f'OCURRIO UN ERROR {e}')

    @classmethod
    def buscar_libro_por_isbn(cls, isbn):
        conexion = cls.CONEXION_CONFIG
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    sentencia = f'SELECT id_libro FROM {cls.TABLA} WHERE isbn like %s'
                    cursor.execute(sentencia, (f'%{isbn}%',))
                    registros = cursor.fetchone()
                    return registros
        except Exception as e:
            print(f'Ocurrio un error {e}')
            logger_base.log.error(f'OCURRIO UN ERROR {e}')

    @classmethod
    def buscar_cantidad_libro_por_isbn(cls, isbn):
        conexion = cls.CONEXION_CONFIG
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    sentencia = f'SELECT cantidad FROM {cls.TABLA} WHERE isbn = %s'
                    cursor.execute(sentencia, (isbn,))
                    registros = cursor.fetchone()
                    return registros
        except Exception as e:
            print(f'Ocurrio un error {e}')
            logger_base.log.error(f'OCURRIO UN ERROR {e}')

    @classmethod
    def buscar_cantidad_libro_por_id(cls, id_libro):
        conexion = cls.CONEXION_CONFIG
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    sentencia = f'SELECT cantidad FROM {cls.TABLA} WHERE id_libro = %s'
                    cursor.execute(sentencia, (id_libro,))
                    registros = cursor.fetchone()
                    return registros
        except Exception as e:
            print(f'Ocurrio un error {e}')
            logger_base.log.error(f'OCURRIO UN ERROR {e}')