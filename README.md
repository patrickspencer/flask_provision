# AWS Setup

## Keypairs

- Log into AWS console
- In the left hand menu, under Network & Security, click Key Pairs
- Create a keypair
- Save the keypair somewhere (like ~/.ssh/)


### Optional

If you don't want to keep typing in the location of your keypair in your
ssh command do the following:

- Alter your .bashrc file in `~/.bashrc` to load the ssh keypair. I put this:
```
AWS_KEY="/home/patrick/.ssh/aws_key.pem"
if [ -f $AWS_KEY ]; then
  ssh-add $AWS_KEY &>/dev/null
fi
```

## Security group

- In the AWS left hand menu, under Network & Security, click Security
  Groups and create a new security group
- Add two rules. Under the "Type column" make sure one rule is SSH and
  the other one is HTTP. Under the Source column choose "anywhere" for
  both. (It's not super secure this way but it works.)

# EC2 Instance

- Create a new EC2 instance By going to Instances in the left hand menu
  and then clicking on "Launch Instance". I choose the "Ubuntu Server
  16.04 LTS" and then the "t2.micro" size on the next page.
- Click "Next: Configure Instance Details" instead of "Review and Launch".
- Click "Next" until you get to the "Configure Security Groups" and add
  this instance to the security group.
- Create the instance now. Say you want to use your new keypair.
- Go pack to the EC2 Instances page, click on your new instance and
  scroll down until you get to the Public DNS (IPv4). (Say it is
  something like ec2-120-220-160-5.compute-1.amazonaws.com)
- Type in `ssh -i ~/Downloads/key_file.pem
  ubuntu@ec2-120-220-160-5.compute-1.amazonaws.com` into your terminal.
  Change the location of your keyfile to where it is. Don't forget the
  `ubuntu@` part if you used an AWS Ubuntu server. If you added the
  location of your keypair to your bashrc file then your don't need the
  `-i ~/Downloads/key_file.pem` part.


