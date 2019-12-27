from qiniu import Auth, put_file, etag, put_data
import qiniu.config


# 需要填写你的 Access Key 和 Secret Key
access_key = 'INwRUsgA7boGEi6fbM8kQU4d_ep2N87XNrTul946'
secret_key = 'UfpLl_dN6OWuATgVjrDyxT4kwlanKq_iuCnRCFw4'

# 构建鉴权对象
q = Auth(access_key, secret_key)

# 要上传的空间
bucket_name = 'read-buy1'


def image_store(file_data):
    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, None, 3600)

    # 要上传文件的本地路径
    # localfile = './sync/bbb.jpg'

    # put_data上传二进制图片
    ret, info = put_data(token, None, file_data)
    return ret["key"]

