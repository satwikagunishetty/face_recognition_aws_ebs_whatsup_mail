from python_terraform import *

def aws_ebs_os(apply):
    tf = Terraform()
    if apply=="True":
        r=os.system("terraform init")
        if r ==0:
            print("terraform intialized successfully")
        
       #plan terraform 
        ret_code, stdout, stderr= tf.plan(dir_or_plan='C:/Users/hp/Desktop/ml/face_recognition', no_color=IsFlagged, refresh=False,variables=None)
        if ret_code ==0 or ret_code ==2:
            print("terraform plan run successfuly")
            print(stdout)
        #run apply if plan successful
            ret_code_a, stdout_a, stderr_a=tf.apply(dir_or_plan='C:/Users/hp/Desktop/ml/face_recognition', input=False, skip_plan=True, no_color=IsFlagged)
            print(ret_code_a, stdout_a, stderr_a)
        else:
            print(stderr)
    else:
        ret_code_d, stdout_d, stderr_d=tf.destroy(dir_or_plan='C:/Users/hp/Desktop/ml/face_recognition', force=IsFlagged)
        print(ret_code_d, stdout_d, stderr_d) 