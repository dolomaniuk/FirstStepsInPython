class EmptyError(Exception):
    def __init__(self, message, errors):

        # Call the base class constructor with the parameters it needs
        super(EmptyError, self).__init__(message)

        # Now for your custom code...
        self.errors = errors

# class EmptyError(Exception):
#     pass
filename = ["myfile", "nonExistent", "emptyFile", "myfile2"]
for file in filename:
    try:
        f = open(file, 'r')
        line = f.readline()
        if line == "":
            f.close()
            raise EmptyFileError("%s: is empty" % file)
    except IOError as error:
        print("%s: could not be opened: %s" % (file, error.strerror))
    except EmptyFileError as error:
        print(error)
    else:
        print("%s: %s" % (file, f.readline()))
    finally:
        print("Done processing\t", file)
