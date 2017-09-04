all:
	ansible-playbook nodes.yml
	ansible-playbook controller.yml
	ansible-playbook nodes-cleanup.yml
