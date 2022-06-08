from vyper import v


def get_config():
	v.set_config_name('ocp-kpi-web')
	v.add_config_path('.')
	v.read_in_config()
	return v


if __name__ == '__main__':
    c = get_config()
    print(c.get('cors_origins'))