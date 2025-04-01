#officy ial python image on docker hub
FROM python:3.12-slim-bullseye
#naming my working directory
WORKDIR /mydirectory
#creating non-root user with a home directory
RUN useradd -m myuser
#copying + installing dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
#making directories and making them owned by non-root user
RUN mkdir logs qrcodes && chown myuser:myuser logs qrcodes
#copying files and directories into image working directory and changing ownership
#1st dot represents source directory, 2nd dot represents destination (WORKDIR)
COPY --chown=myuser:myuser . . 
#switching to myuser to run
USER myuser
#setting entrypoint for allowing of command-line arguments to be passed to the script via docker run
ENTRYPOINT ["python", "main.py"]
#this sets a default argument, also how to use cmd
CMD [ "--url", "https://github.com/vina-cpu/Homework7"]