����:win10+python3.5+tensorflow1.5.0

����ʹ������Ϊ�����͵�sin�����������ļ���data�ļ�����

predict_result.png��ģ��ѵ��1000�εĽ��
# observed������ԭ��������
# evaluated�������������
# predicted������Ԥ������

ʹ��pre.py�е�train_and_predict(csv_file_name, model_save_dir, training_steps, predicted_steps)�����Ϳ��Խ���Ԥ��
# csv_file_name�������ļ�����model_save_sir��ѵ��ģ�ͱ������ʱĿ¼
# training_steps��ѵ������(ѵ����������2-4��)��predicted_steps�����Ԥ���������Ŀ
# ��������ͼ�񽫻ᱣ����model_save_dir/predict_result.png
# ���к󻹻��ӡ��Ԥ���ʱ���Ͷ�Ӧ��ֵ

train_and_predict()�᷵������������predicted_times, predicted
# predicted_times�洢ʱ��㣬predicted�洢ʱ����Ӧ��Ԥ������

