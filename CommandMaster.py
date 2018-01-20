import os

class CommandMaster(object):

    def __init__(self, command_runner, parent_dir='.'):
        self.all_files = self.get_all_files(parent_dir)
        self.command_runner = command_runner

    def get_all_files(self, parent_dir):
        all_files = [os.path.join(root, _file) for root, folders, files in os.walk(parent_dir) for _file in files if _file == 'shape.geojson' and 'TN-3' not in root]
        return all_files

    def run(self):
        total_files_to_process = len(self.all_files)
        for index, _file in enumerate(self.all_files):
            print 'Processing {} out of {}...'.format(index, total_files_to_process)
            self.command_runner(_file)
        return True

def main():
    import CommandRunner
    command_master = CommandMaster(CommandRunner.command_runner, parent_dir='./districts/cds/2016/')
    command_master.run()

if __name__ == '__main__':
    main()
