#HARE KRSNA
print('Hare Krsna')
if __name__ != '__main__':
    from django.core.files.storage import default_storage
    from django.conf import  settings

    import tensorflow as tf
    import tensorflow_hub as hub
    import os
    import numpy as np
    import pandas as pd


    def breed(request):
        for file in os.listdir('media'):
            os.remove((os.path.join('media', file)))
        file = default_storage.save('rk.jpg', request.FILES['SentFile'])
        # file_path = default_storage.url(file)
        image_path = os.listdir(settings.MEDIA_ROOT)

        image = tf.io.read_file('./media/rk.jpg')
        image = tf.image.decode_image(image, channels=3)
        image = tf.image.convert_image_dtype(image, tf.float32)
        image = tf.expand_dims( tf.image.resize(image, size=[224,224]), axis=0)

        model_path = os.path.join(settings.MODELS, 'dog_breeds_mobilenetv2_Adam_v1_.h5')
        label_path = os.path.join(settings.MODELS, 'labels.csv')

        breeds_name = np.unique(pd.read_csv(label_path).breed.to_numpy())
        model = tf.keras.models.load_model(model_path, custom_objects={'KerasLayer':hub.KerasLayer})

        prediction = model.predict(image)
        pred_breed = breeds_name[np.argmax(prediction)]
        return pred_breed, image_path[0]