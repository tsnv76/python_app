import yaml
from yaml import SafeLoader


def write_dict_to_yaml(dict, file):
    with open(file, 'w', encoding='utf-8') as f_n:
        yaml.dump(dict, f_n, default_flow_style=False, allow_unicode=True)

    with open(file, encoding='utf-8') as f_n:
        f_n_content = yaml.load(f_n, Loader=yaml.FullLoader)

    print(f_n_content == dict)


if __name__ == "__main__":
    my_dict = {
        '1500€': [1, 2, 3, 4],
        '2000€': 8000,
        '30000€': {
            'first': [1, 2, 3, 4],
            'second': 800,
        }
    }

    write_dict_to_yaml(my_dict, 'file.yaml')
