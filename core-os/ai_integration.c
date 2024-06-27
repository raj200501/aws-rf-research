#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/sysinfo.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <openssl/sha.h>

void perform_secure_operations() {
    char *filename = "secure_data.txt";
    char *data = "Sensitive Data for AI Model";
    unsigned char hash[SHA256_DIGEST_LENGTH];

    SHA256((unsigned char*)data, strlen(data), hash);

    int fd = open(filename, O_WRONLY | O_CREAT, 0600);
    if (fd < 0) {
        perror("Failed to open file for writing");
        return;
    }

    write(fd, hash, SHA256_DIGEST_LENGTH);
    close(fd);

    printf("Secure operations completed and data written to %s\n", filename);
}

void print_system_info() {
    struct sysinfo sys_info;
    if (sysinfo(&sys_info) != 0) {
        perror("sysinfo");
        return;
    }

    printf("System uptime: %ld seconds\n", sys_info.uptime);
    printf("Total RAM: %lu MB\n", sys_info.totalram / (1024 * 1024));
    printf("Free RAM: %lu MB\n", sys_info.freeram / (1024 * 1024));
    printf("Process count: %d\n", sys_info.procs);
}

void monitor_performance() {
    while (1) {
        print_system_info();
        sleep(5);
    }
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        fprintf(stderr, "Usage: %s <operation>\n", argv[0]);
        fprintf(stderr, "Operations: secure, monitor\n");
        return 1;
    }

    if (strcmp(argv[1], "secure") == 0) {
        perform_secure_operations();
    } else if (strcmp(argv[1], "monitor") == 0) {
        monitor_performance();
    } else {
        fprintf(stderr, "Invalid operation: %s\n", argv[1]);
        return 1;
    }

    return 0;
}
