# From Specify the base image
FROM continuumio/miniconda3:latest

#Optional metadata for image
#LABEL Author = 'Sanket Sharma' Email= "ur.sanketsharma@gmail.com" linkedin= "https://www.linkedin.com/in/ursanketsharma" Github= "https://github.com/thesanketsharma" description = "Docker for Red wine quality Prediction"

#Copies files or directories from build source and adds them to the filesystem of the container
COPY . /usr/RED_wine_quality/

# The EXPOSE instruction informs DOCker that the container listens on the specified network ports at runtime.
EXPOSE 5000

# WORKDIR specifies the working directory.
WORKDIR /usr/RED_wine_quality/

# The RUN instruction will exexute any commands in a new layer on top of the current image and commit the result
RUN pip install -r requirements.txt

#The CMD provide defaults when executing a container.
CMD streamlit run app.py