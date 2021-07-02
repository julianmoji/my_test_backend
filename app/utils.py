import binascii

from graphql_relay import from_global_id


def generic_model_mutation_process(model, data, id=None, commit=True):
    """
        :param model: django.db.models.base.ModelBase
        :param data: La data para crear o actualizar el modelo, debe ser un diccionario
        :param id: Si id None entonces se crea un objeto nuevo, para actualizar un objeto debes enviar el id
        :param commit: Si True guardar los cambios en la base de datos

        Esta función crea o actualiza un objeto de tipo model
    """
    print('id   ',  id)
    print('data   ',  data)
    if id:
        item = model.objects.get(id=id)
        print('item_id', item.id)
        try:
            del data['id']
        except KeyError:
            pass

        for field, value in data.items():
            setattr(item, field, value)
    else:
        item = model(**data)

    if commit:
        item.save()

    return item


def clean_global_ids(data, exclude_fields=None):
    if exclude_fields is None:
        exclude_fields = []

    if type(data) is list:
        for index, item in enumerate(data):
            data[index] = clean_global_ids(item)

    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, str):
                if key not in exclude_fields and '_id' in key or key == 'id':
                    try:
                        data[key] = int(from_global_id(value.strip())[1])
                    except (UnicodeDecodeError, TypeError):
                        if key == 'id' or key[-3:] == '_id':
                            raise ValueError(f'El valor para el campo {key} es inválido.')
                        data[key] = value.strip()
                    except (binascii.Error, ValueError):
                        if key == 'id' or key[-3:] == '_id':
                            raise ValueError(f'El valor para el campo {key} es inválido.')
                else:
                    data[key] = value.strip()

            elif isinstance(value, dict):
                data[key] = clean_global_ids(value)

            elif isinstance(value, list):
                result = []
                for item in value:
                    result.append(clean_global_ids(item))
                data[key] = result
        return data

    if isinstance(data, str):
        try:
            return from_global_id(data.strip())[1]
        except (UnicodeDecodeError, TypeError, binascii.Error, ValueError):
            return data

    return data
