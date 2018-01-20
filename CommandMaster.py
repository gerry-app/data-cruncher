import os

class CommandMaster(object):

    def __init(self, command_runner, parent_dir='.'):
        self.all_files = self.get_all_files(parent_dir)
        self.command_runner = command_runner

    def get_all_files(self):
        root, folders, files = os.walk(self.parent_dir)
        all_files = [os.path.join(root, _file) for _file in files if _file == 'shape.geojson']
        return all_files

    def run(self):
        for _file in self.all_files:
            self.command_runner(_file)
        return True

def main():
    import CommandRunner
    command_master = CommandMaster(CommandRunner.command_runner, parent_dir='./districts/cds/2016/')
    command_master.run()

if __name__ == '__main__':
    main()
