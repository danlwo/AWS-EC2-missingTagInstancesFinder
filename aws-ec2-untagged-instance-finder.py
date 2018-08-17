# danlwo.tem96@g2.nctu.edu.tw

import boto3

def main():
    untagged_instance_list = []
    aws_access_key_ID = raw_input('---[CONF] Please Enter Access Key ID:\t')
    aws_access_key = raw_input('---[CONF] Please Enter Access Key:\t')
    designated_region = raw_input('---[CONF] Please Enter Designated Region:\t')
    designated_tag = raw_input('---[CONF] Please Enter Designated Tag:\t')
    session = boto3.Session(
        aws_access_key_id=aws_access_key_ID, 
        aws_secret_access_key=aws_access_key
        )
    ec2 = session.resource('ec2', region_name = designated_region)
    instance_iterator = ec2.instances.all()
    print '\n---[INFO] Successfully Connected & Starting to Scan.\n'
    for instance in instance_iterator:
        print '---[INFO] Now Scanning Instance:\t%s' % (str(instance.id))
        instance_tag_list = []
        if instance.tags == None:
            untagged_instance_list.append(str(instance.id))
        else:
            for tag in instance.tags:
                instance_tag_list.append(str(tag['Key']))
            if designated_tag not in instance_tag_list:
                untagged_instance_list.append(str(instance.id))
            else:
                pass
    print '\n---[INFO] Untagged Instances of Tag <%s> in <%s> region:' % (designated_tag, designated_region)
    print '\n', untagged_instance_list, '\n'

if __name__ == '__main__':
    main()