import time


RUNTIME_PROCESS_STARTED = time.monotonic()


import base64


import collections


import contextlib


import ctypes


import datetime


import functools


import gzip


import hashlib


import io


import json


import math


import os


import pathlib


import platform


import queue


import random


import re


import signal


import shlex


import shutil


import socket


import sqlite3


import stat


import struct


import subprocess


import sys


import tempfile


import threading


import traceback


import uuid


import xml.etree.ElementTree as ET


import zipfile


import urllib.request


import urllib.parse


import urllib.error


import zlib


from pathlib import Path


import statistics


APP_NAME = "通用游戏 Agent · 自适应视觉与智能交互"


APP_VERSION = "8.7.0-local-learning"


RUNTIME_BYTES_PER_KIB = 1024


RUNTIME_BYTES_PER_MIB = RUNTIME_BYTES_PER_KIB ** 2


RUNTIME_BYTES_PER_GIB = RUNTIME_BYTES_PER_KIB ** 3


RUNTIME_MILLISECONDS_PER_SECOND = 1000


RUNTIME_PERCENT_SCALE = 100


RUNTIME_CANCEL_POLL_SECONDS = 0.05


RUNTIME_SOCKET_POLL_SECONDS = 0.1


RUNTIME_STATUS_REFRESH_SECONDS = 0.5


RUNTIME_LATENCY_MEAN_WEIGHT = 1 / 8


RUNTIME_LATENCY_DEVIATION_WEIGHT = 1 / 4


RUNTIME_TIMEOUT_DEVIATIONS = 4


RUNTIME_TIMING_SCHEMA_VERSION = 1


RUNTIME_LOG_MIB = 8


RUNTIME_BOOTSTRAP_COMMAND_TIMEOUT_SECONDS = 20


RUNTIME_BOOTSTRAP_SHELL_TIMEOUT_SECONDS = 20


RUNTIME_BOOTSTRAP_SCREENSHOT_TIMEOUT_SECONDS = 15


RUNTIME_BOOTSTRAP_CONSOLE_TIMEOUT_SECONDS = 3


RUNTIME_BOOTSTRAP_CONNECT_TIMEOUT_SECONDS = 1.5


RUNTIME_BOOTSTRAP_DISCOVERY_SECONDS = 60


RUNTIME_BOOTSTRAP_HOST_TIMEOUT_SECONDS = 5


RUNTIME_BOOTSTRAP_HIERARCHY_SECONDS = 3


RUNTIME_BOOTSTRAP_CONTEXT_SECONDS = 4


RUNTIME_BOOTSTRAP_ADB_START_SECONDS = 15


RUNTIME_BOOTSTRAP_INSTALL_SECONDS = 120


RUNTIME_BOOTSTRAP_INSTALL_BYTES_PER_SECOND = RUNTIME_BYTES_PER_MIB


RUNTIME_BOOTSTRAP_ANDROID_MEMORY_MB = 1536


RUNTIME_ANDROID_Q_API = 29


RUNTIME_ANDROID_Q_MIN_MEMORY_MB = 2048


RUNTIME_ANDROID_17_API = 37


RUNTIME_ANDROID_17_MIN_MEMORY_MB = 4096


RUNTIME_EMULATOR_MAX_MEMORY_MB = 8192


RUNTIME_BOOTSTRAP_DISPLAY_WIDTH = 720


RUNTIME_BOOTSTRAP_DISPLAY_HEIGHT = 1280


RUNTIME_BOOTSTRAP_DISPLAY_HZ = 60


RUNTIME_BOOTSTRAP_LONG_PRESS_MS = 500


RUNTIME_BOOTSTRAP_TAP_FRAMES = 2


RUNTIME_ANDROID_CACHE_MEMORY_DIVISOR = 8


RUNTIME_ANDROID_HEAP_MEMORY_DIVISOR = 4


RUNTIME_COMPUTE_CONSUMERS = 2


RUNTIME_DISK_FREE_FRACTION = 0.01


RUNTIME_MAX_MESSAGE_CHARACTERS = 2500


RUNTIME_DIAGNOSTIC_TAIL_BYTES = 8192


RUNTIME_MAX_EVENT_ITEMS = 4000


RUNTIME_ADB_LENGTH_DIGITS = 4


RUNTIME_HEXADECIMAL_BASE = 16


RUNTIME_ADB_MAX_SERVICE_BYTES = RUNTIME_HEXADECIMAL_BASE ** RUNTIME_ADB_LENGTH_DIGITS - 1


RUNTIME_ADB_SHELL_STDOUT = 1


RUNTIME_ADB_SHELL_STDERR = 2


RUNTIME_ADB_SHELL_EXIT = 3


RUNTIME_ADB_SHELL_CLOSE_STDIN = 4


RUNTIME_ADB_SHELL_HEADER = struct.Struct("<BI")


RUNTIME_ADB_INITIAL_OUTPUT_BYTES = 32 * RUNTIME_BYTES_PER_MIB


RUNTIME_ADB_INITIAL_PACKET_BYTES = 16 * RUNTIME_BYTES_PER_MIB


RUNTIME_CONSOLE_FIRST_PORT = 5554


RUNTIME_CONSOLE_LAST_PORT = 5682


RUNTIME_CONSOLE_PORT_STRIDE = 2


RUNTIME_LINUX_PROC_STARTTIME_INDEX = 19


RUNTIME_WIN32_JOB_KILL_ON_CLOSE = 0x2000


RUNTIME_WIN32_JOB_EXTENDED_LIMITS = 9


RUNTIME_WIN32_JOB_CPU_RATE = 15


RUNTIME_WIN32_CPU_WEIGHTED = 3


RUNTIME_WIN32_CPU_WEIGHT_LOW = 1


RUNTIME_WIN32_CPU_WEIGHT_NORMAL = 5


RUNTIME_WIN32_BELOW_NORMAL_PRIORITY = 0x4000


RUNTIME_WIN32_THREAD_BACKGROUND_BEGIN = 0x00010000


RUNTIME_WIN32_THREAD_BACKGROUND_END = 0x00020000


RUNTIME_WIN32_DEVICE_PRESENT = 0x00000002


RUNTIME_WIN32_DEVICE_SCOPE_GLOBAL = 0x00000001


RUNTIME_WIN32_DEVICE_DRIVER_KEY = 0x00000002


RUNTIME_WIN32_ERROR_NO_MORE_ITEMS = 259


RUNTIME_WIN32_DISPLAY_CLASS = "4d36e968-e325-11ce-bfc1-08002be10318"


RUNTIME_WINDOWS_11_MIN_BUILD = 22000


RUNTIME_WIN32_PROCESS_POWER_THROTTLING = 4


RUNTIME_WIN32_POWER_THROTTLING_VERSION = 1


RUNTIME_WIN32_EXECUTION_SPEED_THROTTLE = 1


RUNTIME_WIN32_PROCESS_QUERY_LIMITED = 0x1000


RUNTIME_WIN32_SYNCHRONIZE = 0x00100000


RUNTIME_WIN32_WAIT_TIMEOUT = 0x00000102


RUNTIME_WIN32_CO_APARTMENT_THREADED = 2


RUNTIME_WIN32_GUID_TAIL_BYTES = 8


RUNTIME_WIN32_MAX_PATH_CHARACTERS = 32768


RUNTIME_WIN32_PROFILE_FOLDER = 0x28


RUNTIME_WIN32_SCREEN_WIDTH = 0


RUNTIME_WIN32_SCREEN_HEIGHT = 1


RUNTIME_WIN32_VERTICAL_REFRESH = 116


RUNTIME_DWORD_MASK = (1 << 32) - 1


RUNTIME_BOOTSTRAP_ACTIVITY_SECONDS = 15


RUNTIME_ANDROID_XML_CHUNK = struct.Struct("<HHI")


RUNTIME_ANDROID_XML_STRING_POOL = struct.Struct("<IIIII")


RUNTIME_ANDROID_XML_START_ELEMENT = struct.Struct("<IIHHHHHH")


RUNTIME_ANDROID_XML_ATTRIBUTE = struct.Struct("<IIIHBBI")


RUNTIME_ANDROID_XML_NODE = struct.Struct("<II")


RUNTIME_ANDROID_XML_WORD = struct.Struct("<I")


RUNTIME_ANDROID_XML_SHORT = struct.Struct("<H")


RUNTIME_ANDROID_XML_KIND = 3


RUNTIME_ANDROID_XML_STRING_POOL_KIND = 1


RUNTIME_ANDROID_XML_START_ELEMENT_KIND = 0x102


RUNTIME_ANDROID_XML_UTF8 = 0x100


RUNTIME_ANDROID_XML_LENGTH8_HIGH = 0x80


RUNTIME_ANDROID_XML_LENGTH16_HIGH = 0x8000


RUNTIME_ANDROID_XML_BYTE_BITS = 8


RUNTIME_ANDROID_XML_SHORT_BITS = 16


RUNTIME_ANDROID_XML_INTEGER_TYPES = frozenset((0x10, 0x11))


RUNTIME_ANDROID_XML_STRING_TYPE = 3


RUNTIME_ANDROID_NAMESPACE = "http://schemas.android.com/apk/res/android"


RUNTIME_APK_MANIFEST_BYTES = 4 * RUNTIME_BYTES_PER_MIB


RUNTIME_ROTATION_HALF_TURN = 2


RUNTIME_ROTATION_THREE_QUARTER_TURN = 3


RUNTIME_INPUT_EVENTS = {"slot": (3, 47), "tracking": (3, 57), "x": (3, 53), "y": (3, 54), "pressure": (3, 58), "major": (3, 48), "contact": (1, 330), "sync": (0, 0)}


RUNTIME_PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


RUNTIME_PNG_CHUNK_PREFIX = struct.Struct(">I4s")


RUNTIME_PNG_DIMENSIONS = struct.Struct(">II")


RUNTIME_MINIMUM_PROCESS_STOP_SECONDS = 1


RUNTIME_STARTUP_ERROR_CONFIRMATIONS = 3


RUNTIME_BOOTSTRAP_COLD_BOOT_SECONDS = 360


RUNTIME_BOOTSTRAP_SOFTWARE_BOOT_SECONDS = 1200


RUNTIME_BOOTSTRAP_SOFTWARE_DISCOVERY_SECONDS = 480


RUNTIME_BOOTSTRAP_SHUTDOWN_SECONDS = 8


RUNTIME_BOOTSTRAP_SNAPSHOT_SAVE_SECONDS = 45


RUNTIME_BOOTSTRAP_GPU_PROBE_SECONDS = 20


RUNTIME_HEALTH_SUCCESS_CACHE_SECONDS = 8


RUNTIME_BOOT_STATUS_SECONDS = 15


RUNTIME_IMAGE_RESOURCE_RESERVE_MB = 512


RUNTIME_ANDROID_MIN_FREE_DISK_BYTES = 5 * RUNTIME_BYTES_PER_GIB


RUNTIME_SUPERVISOR_POLL_SECONDS = 3


RUNTIME_SUPERVISOR_HEARTBEAT_SECONDS = 50


RUNTIME_SUPERVISOR_RETRY_MAX_SECONDS = 60


RUNTIME_WINDOWS_WORK_AREA = 0x0030


RUNTIME_FRAMEBUFFER_ALIGNMENT = 2


RUNTIME_BOOTSTRAP_ANDROID_DPI = 240


RUNTIME_JSON_INDENT = 2


RUNTIME_SOCKET_RECEIVE_BYTES = 64 * RUNTIME_BYTES_PER_KIB


RUNTIME_CONSOLE_RESPONSE_BYTES = 64 * RUNTIME_BYTES_PER_KIB


RUNTIME_PROCESS_REAP_SECONDS = 3


RUNTIME_PROCESS_FORCE_STOP_SECONDS = 2


RUNTIME_ADB_RECOVERY_CONFIRMATIONS = 2


RUNTIME_PACKAGE_LIST_TIMEOUT_SECONDS = 8


RUNTIME_APP_LAUNCH_TIMEOUT_SECONDS = 12


RUNTIME_ADB_HEALTH_TIMEOUT_SECONDS = 6


RUNTIME_GPU_LOG_BYTES = 12000


RUNTIME_LOGCAT_LINES = 400


RUNTIME_DIAGNOSTIC_TEXT_BYTES = 100000


RUNTIME_ADB_LOG_PREVIEW_LINES = 2


RUNTIME_BOOTSTRAP_DEVICE_REGISTRATION_SECONDS = 3


RUNTIME_LOCAL_ANDROID_ADB_PORTS = (5555, 5557, 5559, 7555, 16384, 21503, 62001)


RUNTIME_LOCAL_ANDROID_VIRTUAL_HINTS = ("goldfish", "ranchu", "vbox", "nox", "mumu", "ldplayer", "memu", "emulator", "qemu", "bluestacks")


RUNTIME_LOCAL_ANDROID_VENDOR_FOLDERS = ("Nox", "LDPlayer", "LDPlayer9", "Microvirt", "MEmu", "Netease", "MuMuPlayer-12.0", "BlueStacks_nxt")


RUNTIME_LOCAL_ANDROID_ADB_FILENAMES = ("adb.exe", "nox_adb.exe", "HD-Adb.exe")


RUNTIME_LOCAL_ANDROID_ADB_PROBE_SECONDS = RUNTIME_BOOTSTRAP_CONNECT_TIMEOUT_SECONDS


RUNTIME_PROCESS_IDENTITY_WAIT_SECONDS = 2


RUNTIME_STATE_READ_TIMEOUT_SECONDS = 2


ANDROID_OFFICIAL_REPOSITORY = "https://dl.google.com/android/repository/"


ANDROID_REPOSITORY_INDEX = "repository2-1.xml"


ANDROID_IMAGE_INDEXES = ("sys-img/google_apis/sys-img2-5.xml", "sys-img/google_apis/sys-img2-1.xml", "sys-img/google_apis_playstore/sys-img2-5.xml", "sys-img/google_apis_playstore/sys-img2-1.xml", "sys-img/android/sys-img2-5.xml", "sys-img/android/sys-img2-1.xml")


ANDROID_PREFERRED_APIS = (35, 36, 34, 33)


ANDROID_METADATA_MAX_BYTES = 32 * RUNTIME_BYTES_PER_MIB


ANDROID_ARCHIVE_MAX_BYTES = 8 * RUNTIME_BYTES_PER_GIB


ANDROID_EXTRACT_MAX_BYTES = 32 * RUNTIME_BYTES_PER_GIB


ANDROID_MIN_FREE_DISK_BYTES = 10 * RUNTIME_BYTES_PER_GIB


ANDROID_HTTP_TIMEOUT_SECONDS = 30


ANDROID_DOWNLOAD_UPDATE_SECONDS = 3


ANDROID_DOWNLOAD_RETRIES = 3


ANDROID_RETRY_SECONDS = 2


ANDROID_DOWNLOAD_BLOCK_BYTES = RUNTIME_BYTES_PER_MIB


ANDROID_HOST_BITS = str(struct.calcsize("P") * RUNTIME_ANDROID_XML_BYTE_BITS)


ANDROID_ARCHIVE_PREFIXES = {"emulator": "emulator", "platform-tools": "platform-tools", "system-image": "x86_64"}


class RuntimeMeasurements:
    def __init__(self, path=None):
        self.path = pathlib.Path(path) if path is not None else None
        self.lock = threading.RLock()
        self.values = {}
        stored = read_json(self.path, {}) if self.path is not None else {}
        if isinstance(stored, dict) and stored.get("version") == RUNTIME_TIMING_SCHEMA_VERSION:
            records = stored.get("measurements", {})
            for key, item in records.items() if isinstance(records, dict) else ():
                if not isinstance(key, str) or not isinstance(item, dict):
                    continue
                numbers = (item.get("mean"), item.get("deviation"), item.get("count"))
                if any(isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value < 0 for value in numbers):
                    continue
                if numbers[0] > 0 and type(numbers[-1]) is int and numbers[-1] > 0:
                    self.values[key] = {"mean": float(numbers[0]), "deviation": float(numbers[1]), "count": numbers[-1], "failures": 0}
        self.dirty = False

    def estimate(self, key, fallback):
        with self.lock:
            value = self.values.get(str(key))
            return max(0, value["mean"] if value else float(fallback))

    def timeout(self, key, fallback):
        minimum = max(RUNTIME_SOCKET_POLL_SECONDS, float(fallback))
        with self.lock:
            value = self.values.get(str(key))
            if value is None:
                return minimum
            mean, deviation = value["mean"], value["deviation"]
            uncertainty = max(deviation, mean / math.sqrt(value["count"]))
            return max(minimum, mean + RUNTIME_TIMEOUT_DEVIATIONS * uncertainty)

    def observe(self, key, seconds, success=True, units=None):
        seconds = float(seconds)
        if not math.isfinite(seconds) or seconds <= 0:
            return
        key = str(key)
        with self.lock:
            value = self.values.get(key)
            if value is None:
                value = {"mean": seconds, "deviation": seconds / RUNTIME_TIMEOUT_DEVIATIONS, "count": 0, "failures": 0}
                self.values[key] = value
            error = abs(seconds - value["mean"])
            value["deviation"] += RUNTIME_LATENCY_DEVIATION_WEIGHT * (error - value["deviation"])
            value["mean"] += RUNTIME_LATENCY_MEAN_WEIGHT * (seconds - value["mean"])
            value["count"] += 1
            value["failures"] = 0 if success else value["failures"] + 1
            if not success:
                value["mean"] = max(value["mean"], seconds)
                value["deviation"] = max(value["deviation"], seconds / RUNTIME_TIMEOUT_DEVIATIONS)
            self.dirty = True
        if success and units is not None and float(units) > 0:
            self.observe(key + ":per_unit", seconds / float(units))

    @contextlib.contextmanager
    def measure(self, key, units=None):
        started = time.monotonic()
        try:
            yield
        except Cancelled:
            raise
        except BaseException:
            self.observe(key, time.monotonic() - started, success=False)
            raise
        else:
            self.observe(key, time.monotonic() - started, units=units)

    def snapshot(self):
        with self.lock:
            return {key: dict(value) for key, value in self.values.items()}

    def save(self):
        if self.path is None:
            return
        with self.lock:
            if not self.dirty:
                return
            value = {"version": RUNTIME_TIMING_SCHEMA_VERSION, "measurements": self.snapshot()}
            atomic_json(self.path, value)
            self.dirty = False


def runtime_io_capacity():
    cpu_count = max(1, os.cpu_count() or 1)
    return max(1, math.isqrt(cpu_count))


@contextlib.contextmanager
def runtime_background_work(log=None):
    kernel = None
    entered = False
    if os.name == "nt" and threading.current_thread() is not threading.main_thread():
        try:
            kernel = ctypes.WinDLL("kernel32", use_last_error=True)
            kernel.GetCurrentThread.restype = ctypes.c_void_p
            kernel.SetThreadPriority.argtypes = [ctypes.c_void_p, ctypes.c_int]
            kernel.SetThreadPriority.restype = ctypes.c_int
            entered = bool(kernel.SetThreadPriority(kernel.GetCurrentThread(), RUNTIME_WIN32_THREAD_BACKGROUND_BEGIN))
            if not entered and log is not None:
                log("background_scheduling_unavailable", error=ctypes.get_last_error(), thread=threading.current_thread().name)
        except (AttributeError, OSError) as exc:
            if log is not None:
                log("background_scheduling_unavailable", error=str(exc), thread=threading.current_thread().name)
    try:
        yield
    finally:
        if entered:
            if not kernel.SetThreadPriority(kernel.GetCurrentThread(), RUNTIME_WIN32_THREAD_BACKGROUND_END) and log is not None:
                log("background_scheduling_restore_failed", error=ctypes.get_last_error(), thread=threading.current_thread().name)


def runtime_disk_reserve(folder):
    usage = shutil.disk_usage(folder)
    return max(io.DEFAULT_BUFFER_SIZE, math.ceil(usage.free * RUNTIME_DISK_FREE_FRACTION))


def runtime_input_event(name, value):
    category, code = RUNTIME_INPUT_EVENTS[name]
    return str(category) + ":" + str(code) + ":" + str(int(value))


def runtime_default_display(pixel_budget=None, memory_mb=None):
    width, height, hz = RUNTIME_BOOTSTRAP_DISPLAY_WIDTH, RUNTIME_BOOTSTRAP_DISPLAY_HEIGHT, RUNTIME_BOOTSTRAP_DISPLAY_HZ
    memory_scale = max(1, float(memory_mb or RUNTIME_BOOTSTRAP_ANDROID_MEMORY_MB) / RUNTIME_BOOTSTRAP_ANDROID_MEMORY_MB)
    capacity = width * height * math.sqrt(memory_scale)
    if pixel_budget is not None:
        if isinstance(pixel_budget, bool) or not math.isfinite(float(pixel_budget)) or float(pixel_budget) <= 0:
            raise ValueError("视觉像素预算必须是有限正数")
        capacity = min(capacity, float(pixel_budget))
    if os.name == "nt":
        user = ctypes.WinDLL("user32", use_last_error=True)
        native_width = user.GetSystemMetrics(RUNTIME_WIN32_SCREEN_WIDTH)
        native_height = user.GetSystemMetrics(RUNTIME_WIN32_SCREEN_HEIGHT)
        class Rect(ctypes.Structure):
            _fields_ = [("left", ctypes.c_long), ("top", ctypes.c_long), ("right", ctypes.c_long), ("bottom", ctypes.c_long)]
        work = Rect()
        user.SystemParametersInfoW.argtypes = [ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_uint32]
        user.SystemParametersInfoW.restype = ctypes.c_int
        if user.SystemParametersInfoW(RUNTIME_WINDOWS_WORK_AREA, 0, ctypes.byref(work), 0):
            native_width, native_height = work.right - work.left, work.bottom - work.top
        if native_width > 0 and native_height > 0:
            short, long = sorted((native_width, native_height))
            scale = min(1, math.sqrt(capacity / (short * long)))
            width = max(RUNTIME_FRAMEBUFFER_ALIGNMENT, round(short * scale) // RUNTIME_FRAMEBUFFER_ALIGNMENT * RUNTIME_FRAMEBUFFER_ALIGNMENT)
            height = max(RUNTIME_FRAMEBUFFER_ALIGNMENT, round(long * scale) // RUNTIME_FRAMEBUFFER_ALIGNMENT * RUNTIME_FRAMEBUFFER_ALIGNMENT)
        user.GetDC.argtypes = [ctypes.c_void_p]
        user.GetDC.restype = ctypes.c_void_p
        user.ReleaseDC.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
        user.ReleaseDC.restype = ctypes.c_int
        dc = user.GetDC(None)
        if dc:
            try:
                gdi = ctypes.WinDLL("gdi32", use_last_error=True)
                gdi.GetDeviceCaps.argtypes = [ctypes.c_void_p, ctypes.c_int]
                gdi.GetDeviceCaps.restype = ctypes.c_int
                refresh = gdi.GetDeviceCaps(dc, RUNTIME_WIN32_VERTICAL_REFRESH)
                if refresh > 1:
                    hz = refresh
            finally:
                user.ReleaseDC(None, dc)
    if os.name != "nt":
        scale = min(1, math.sqrt(capacity / (width * height)))
        width = max(RUNTIME_FRAMEBUFFER_ALIGNMENT, round(width * scale) // RUNTIME_FRAMEBUFFER_ALIGNMENT * RUNTIME_FRAMEBUFFER_ALIGNMENT)
        height = max(RUNTIME_FRAMEBUFFER_ALIGNMENT, round(height * scale) // RUNTIME_FRAMEBUFFER_ALIGNMENT * RUNTIME_FRAMEBUFFER_ALIGNMENT)
    return width, height, hz


class Cancelled(Exception):
    pass


class CombinedCancel:
    def __init__(self, *events):
        self.events = tuple(event for event in events if event is not None)

    def is_set(self):
        return any(event.is_set() for event in self.events)

    def wait(self, timeout=None):
        deadline = None if timeout is None else time.monotonic() + max(0.0, timeout)
        while not self.is_set():
            remaining = RUNTIME_CANCEL_POLL_SECONDS if deadline is None else min(RUNTIME_CANCEL_POLL_SECONDS, deadline - time.monotonic())
            if remaining <= 0:
                return self.is_set()
            if self.events:
                self.events[0].wait(remaining)
            else:
                time.sleep(remaining)
        return True


class GeometryPending(RuntimeError):
    pass


class ComponentFailure(RuntimeError):
    def __init__(self, component, error):
        self.component = str(component)
        super().__init__(str(error))


def check_cancel(cancel):
    if cancel is not None and cancel.is_set():
        raise Cancelled("操作已取消")


def utc_now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="milliseconds")


def path_is_link(path):
    path = pathlib.Path(path)
    if path.is_symlink() or getattr(path, "is_junction", lambda: False)():
        return True
    if os.name == "nt":
        try:
            return bool(path.lstat().st_file_attributes & stat.FILE_ATTRIBUTE_REPARSE_POINT)
        except (AttributeError, OSError):
            return False
    return False


def atomic_json(path, value):
    path = pathlib.Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if path_is_link(path) or path_is_link(path.parent):
        raise OSError("拒绝通过链接写入状态文件：" + str(path))
    temp = path.with_name(path.name + "." + uuid.uuid4().hex + ".tmp")
    try:
        with temp.open("x", encoding="utf-8", newline="\n") as handle:
            json.dump(value, handle, ensure_ascii=False, indent=RUNTIME_JSON_INDENT)
            handle.flush()
            os.fsync(handle.fileno())
        if path_is_link(path):
            raise OSError("状态文件被替换成了链接：" + str(path))
        os.replace(temp, path)
    finally:
        with contextlib.suppress(OSError):
            temp.unlink()


def safe_workspace_file(root, dest):
    raw_root = pathlib.Path(root).absolute()
    if ".." in raw_root.parts or path_is_link(raw_root):
        raise ValueError("工作文件夹不得包含上级目录跳转或符号链接")
    root = raw_root.resolve()
    dest = pathlib.Path(dest).absolute()
    if ".." in dest.parts:
        raise ValueError("工作路径不得包含上级目录跳转：" + str(dest))
    try:
        relative = dest.relative_to(root)
    except ValueError as exc:
        raise ValueError("文件路径必须位于所选工作文件夹内：" + str(dest)) from exc
    current = root
    for part in relative.parts:
        current = current / part
        if path_is_link(current):
            raise ValueError("工作路径包含链接，拒绝写入：" + str(current))
    if dest.resolve(strict=False) != dest:
        raise ValueError("工作路径解析后发生变化，拒绝写入：" + str(dest))
    return dest


def read_json(path, default=None):
    try:
        with pathlib.Path(path).open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except (OSError, ValueError):
        return default


def system_memory_mb():
    if os.name == "nt":
        class MemoryStatus(ctypes.Structure):
            _fields_ = [("length", ctypes.c_uint32), ("load", ctypes.c_uint32), ("total", ctypes.c_uint64), ("available", ctypes.c_uint64), ("page_total", ctypes.c_uint64), ("page_available", ctypes.c_uint64), ("virtual_total", ctypes.c_uint64), ("virtual_available", ctypes.c_uint64), ("extended", ctypes.c_uint64)]
        state = MemoryStatus()
        state.length = ctypes.sizeof(state)
        kernel = ctypes.WinDLL("kernel32", use_last_error=True)
        kernel.GlobalMemoryStatusEx.argtypes = [ctypes.POINTER(MemoryStatus)]
        kernel.GlobalMemoryStatusEx.restype = ctypes.c_int
        if kernel.GlobalMemoryStatusEx(ctypes.byref(state)):
            total = int(state.total // RUNTIME_BYTES_PER_MIB)
            available = int(min(state.available, state.page_available, state.virtual_available) // RUNTIME_BYTES_PER_MIB)
            if total > 0 and 0 <= available <= total:
                return total, available
        raise ComponentFailure("resources", "Windows 内存/提交预算读取失败，不能据此分配模拟器和本地计算内存")
    try:
        info = {}
        with pathlib.Path("/proc/meminfo").open(encoding="ascii") as stream:
            for line in stream:
                fields = line.split()
                if len(fields) >= 2 and fields[1].isdigit():
                    info[fields[0].rstrip(":")] = int(fields[1]) * RUNTIME_BYTES_PER_KIB
        total = info.get("MemTotal", 0)
        available = info.get("MemAvailable", info.get("MemFree", 0))
        if total > 0 and 0 <= available <= total:
            return total // RUNTIME_BYTES_PER_MIB, available // RUNTIME_BYTES_PER_MIB
    except (OSError, ValueError):
        pass
    try:
        page = os.sysconf("SC_PAGE_SIZE")
        total = int(page * os.sysconf("SC_PHYS_PAGES") // RUNTIME_BYTES_PER_MIB)
        available = int(page * os.sysconf("SC_AVPHYS_PAGES") // RUNTIME_BYTES_PER_MIB)
        if total > 0 and 0 <= available <= total:
            return total, available
    except (AttributeError, OSError, ValueError):
        pass
    raise ComponentFailure("resources", "无法读取设备真实可用内存，正在等待资源检测恢复")


def physical_memory_mb():
    return system_memory_mb()[0]


def available_memory_mb():
    return system_memory_mb()[1]


class UIEventQueue:
    def __init__(self, limit=RUNTIME_MAX_EVENT_ITEMS):
        self.limit = max(1, int(limit))
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)
        self.items = collections.deque()
        self.dropped = 0
        self.closed = False
        self.critical = frozenset({"manual_text_result", "exported", "install_result"})
        self.coalesced = frozenset({"status", "stats", "running", "stopping", "prepared", "resources", "plan", "learning", "scene"})

    def put(self, item, block=True, timeout=None):
        kind = item[0] if isinstance(item, tuple) and item else ""
        deadline = None if timeout is None else time.monotonic() + max(0.0, timeout)
        with self.condition:
            if self.closed:
                return
            if kind in self.coalesced:
                for index in range(len(self.items) - 1, -1, -1):
                    if self.items[index][0] == kind:
                        del self.items[index]
                        break
            elif kind == "progress" and len(item) > 1 and isinstance(item[1], dict):
                identity = (item[1].get("stage"), item[1].get("name"))
                for index in range(len(self.items) - 1, -1, -1):
                    previous = self.items[index]
                    if previous[0] == "progress" and isinstance(previous[1], dict) and (previous[1].get("stage"), previous[1].get("name")) == identity:
                        del self.items[index]
                        break
            while len(self.items) >= self.limit:
                if self.closed:
                    return
                removable = next((index for index, value in enumerate(self.items) if value[0] not in self.critical), None)
                if removable is not None:
                    del self.items[removable]
                    self.dropped += 1
                    break
                if kind not in self.critical:
                    self.dropped += 1
                    return
                if not block:
                    raise queue.Full
                remaining = None if deadline is None else deadline - time.monotonic()
                if remaining is not None and remaining <= 0:
                    raise queue.Full
                self.condition.wait(remaining)
            if self.closed:
                return
            self.items.append(item)

    def get_nowait(self):
        with self.condition:
            if not self.items:
                raise queue.Empty
            item = self.items.popleft()
            self.condition.notify_all()
            return item

    def qsize(self):
        with self.condition:
            return len(self.items)

    def close(self):
        with self.condition:
            self.closed = True
            self.items.clear()
            self.condition.notify_all()


def desktop_directory():
    if os.name == "nt":
        class GUID(ctypes.Structure):
            _fields_ = [("data1", ctypes.c_uint32), ("data2", ctypes.c_uint16), ("data3", ctypes.c_uint16), ("data4", ctypes.c_ubyte * RUNTIME_WIN32_GUID_TAIL_BYTES)]
        folder = GUID.from_buffer_copy(uuid.UUID("B4BFCC3A-DB2C-424C-B029-7FE99A87C641").bytes_le)
        pointer = ctypes.c_void_p()
        initialized = ctypes.windll.ole32.CoInitializeEx(None, RUNTIME_WIN32_CO_APARTMENT_THREADED)
        try:
            function = ctypes.windll.shell32.SHGetKnownFolderPath
            function.argtypes = [ctypes.POINTER(GUID), ctypes.c_uint32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p)]
            function.restype = ctypes.c_long
            code = function(ctypes.byref(folder), 0, None, ctypes.byref(pointer))
            if code == 0 and pointer.value:
                return pathlib.Path(ctypes.wstring_at(pointer.value))
        finally:
            if pointer.value:
                ctypes.windll.ole32.CoTaskMemFree.argtypes = [ctypes.c_void_p]
                ctypes.windll.ole32.CoTaskMemFree(pointer)
            if initialized in (0, 1):
                ctypes.windll.ole32.CoUninitialize()
    return pathlib.Path.home() / "Desktop"


class WorkspaceLock:
    def __init__(self, root):
        self.path = pathlib.Path(root) / "session.lock"
        if path_is_link(self.path):
            raise OSError("会话锁文件不得是符号链接")
        self.handle = self.path.open("a+b")
        self.handle.seek(0)
        if self.path.stat().st_size == 0:
            self.handle.write(b"0")
            self.handle.flush()
        self.handle.seek(0)
        try:
            if os.name == "nt":
                import msvcrt
                msvcrt.locking(self.handle.fileno(), msvcrt.LK_NBLCK, 1)
            else:
                import fcntl
                fcntl.flock(self.handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except Exception:
            self.handle.close()
            raise OSError("这个工作文件夹正在被另一个实例使用，请关闭那个实例或选择另一个文件夹")

    def close(self):
        if not self.handle.closed:
            with contextlib.suppress(OSError):
                self.handle.seek(0)
                if os.name == "nt":
                    import msvcrt
                    msvcrt.locking(self.handle.fileno(), msvcrt.LK_UNLCK, 1)
                else:
                    import fcntl
                    fcntl.flock(self.handle.fileno(), fcntl.LOCK_UN)
            self.handle.close()


class _AndroidProcessJob:
    def __init__(self, process):
        self.handle = None
        self.kernel = None
        self.process = process
        self._policy_lock = threading.Lock()
        self._policy = None
        if os.name != "nt":
            return
        import ctypes
        class BasicLimits(ctypes.Structure):
            _fields_ = [("process_time", ctypes.c_int64), ("job_time", ctypes.c_int64), ("flags", ctypes.c_uint32), ("min_working_set", ctypes.c_size_t), ("max_working_set", ctypes.c_size_t), ("active_processes", ctypes.c_uint32), ("affinity", ctypes.c_size_t), ("priority", ctypes.c_uint32), ("scheduling", ctypes.c_uint32)]
        class IoCounters(ctypes.Structure):
            _fields_ = [(name, ctypes.c_uint64) for name in ("read_operations", "write_operations", "other_operations", "read_bytes", "write_bytes", "other_bytes")]
        class ExtendedLimits(ctypes.Structure):
            _fields_ = [("basic", BasicLimits), ("io", IoCounters), ("process_memory", ctypes.c_size_t), ("job_memory", ctypes.c_size_t), ("peak_process_memory", ctypes.c_size_t), ("peak_job_memory", ctypes.c_size_t)]
        kernel = ctypes.WinDLL("kernel32", use_last_error=True)
        kernel.CreateJobObjectW.argtypes = [ctypes.c_void_p, ctypes.c_wchar_p]
        kernel.CreateJobObjectW.restype = ctypes.c_void_p
        kernel.SetInformationJobObject.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32]
        kernel.SetInformationJobObject.restype = ctypes.c_int
        kernel.AssignProcessToJobObject.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
        kernel.AssignProcessToJobObject.restype = ctypes.c_int
        kernel.CloseHandle.argtypes = [ctypes.c_void_p]
        kernel.CloseHandle.restype = ctypes.c_int
        handle = kernel.CreateJobObjectW(None, None)
        if not handle:
            raise ctypes.WinError(ctypes.get_last_error())
        try:
            limits = ExtendedLimits()
            limits.basic.flags = RUNTIME_WIN32_JOB_KILL_ON_CLOSE
            if not kernel.SetInformationJobObject(handle, RUNTIME_WIN32_JOB_EXTENDED_LIMITS, ctypes.byref(limits), ctypes.sizeof(limits)):
                raise ctypes.WinError(ctypes.get_last_error())
            if not kernel.AssignProcessToJobObject(handle, int(process._handle)):
                raise ctypes.WinError(ctypes.get_last_error())
        except Exception:
            kernel.CloseHandle(handle)
            raise
        self.handle = handle
        self.kernel = kernel
        kernel.SetPriorityClass.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
        kernel.SetPriorityClass.restype = ctypes.c_int
        kernel.SetProcessInformation.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32]
        kernel.SetProcessInformation.restype = ctypes.c_int
        with contextlib.suppress(Exception):
            self.set_background_policy(False)

    def set_background_policy(self, pressure=False):
        with self._policy_lock:
            if not self.handle or self.kernel is None:
                return False
            selected = bool(pressure)
            if selected == self._policy:
                return True
            class CpuWeight(ctypes.Structure):
                _fields_ = [("flags", ctypes.c_uint32), ("weight", ctypes.c_uint32)]
            class PowerState(ctypes.Structure):
                _fields_ = [("version", ctypes.c_uint32), ("control", ctypes.c_uint32), ("state", ctypes.c_uint32)]
            weight = CpuWeight(RUNTIME_WIN32_CPU_WEIGHTED, RUNTIME_WIN32_CPU_WEIGHT_LOW if selected else RUNTIME_WIN32_CPU_WEIGHT_NORMAL)
            weighted = bool(self.kernel.SetInformationJobObject(self.handle, RUNTIME_WIN32_JOB_CPU_RATE, ctypes.byref(weight), ctypes.sizeof(weight)))
            if self.process.poll() is None:
                handle = int(self.process._handle)
                self.kernel.SetPriorityClass(handle, RUNTIME_WIN32_BELOW_NORMAL_PRIORITY)
                power = PowerState(RUNTIME_WIN32_POWER_THROTTLING_VERSION, RUNTIME_WIN32_EXECUTION_SPEED_THROTTLE if selected else 0, RUNTIME_WIN32_EXECUTION_SPEED_THROTTLE if selected else 0)
                self.kernel.SetProcessInformation(handle, RUNTIME_WIN32_PROCESS_POWER_THROTTLING, ctypes.byref(power), ctypes.sizeof(power))
            if weighted:
                self._policy = selected
            return weighted

    def close(self):
        with self._policy_lock:
            handle, self.handle = self.handle, None
            if handle and self.kernel is not None:
                self.kernel.CloseHandle(handle)


class DesktopLoad:
    def __init__(self):
        self.previous = None
        self.kernel = None
        self.user = None
        if os.name == "nt":
            self.kernel = ctypes.WinDLL("kernel32", use_last_error=True)
            self.user = ctypes.WinDLL("user32", use_last_error=True)
            self.kernel.GetSystemTimes.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
            self.kernel.GetSystemTimes.restype = ctypes.c_int
            self.kernel.GetTickCount.restype = ctypes.c_uint32
            self.user.GetForegroundWindow.restype = ctypes.c_void_p
            self.user.GetWindowThreadProcessId.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32)]
            self.user.GetWindowThreadProcessId.restype = ctypes.c_uint32
            self.user.GetLastInputInfo.argtypes = [ctypes.c_void_p]
            self.user.GetLastInputInfo.restype = ctypes.c_int

    def sample(self):
        total, free = system_memory_mb()
        result = {"total_mb": total, "free_mb": free, "cpu_percent": None, "other_app_active": False}
        if self.kernel is None:
            return result
        idle, kernel, user = ctypes.c_uint64(), ctypes.c_uint64(), ctypes.c_uint64()
        if self.kernel.GetSystemTimes(ctypes.byref(idle), ctypes.byref(kernel), ctypes.byref(user)):
            current = (idle.value, kernel.value + user.value)
            if self.previous is not None and current[1] > self.previous[1]:
                result["cpu_percent"] = round(max(0.0, min(RUNTIME_PERCENT_SCALE, RUNTIME_PERCENT_SCALE * (1 - (current[0] - self.previous[0]) / (current[1] - self.previous[1])))), 1)
            self.previous = current
        class LastInput(ctypes.Structure):
            _fields_ = [("size", ctypes.c_uint32), ("time", ctypes.c_uint32)]
        activity = LastInput(ctypes.sizeof(LastInput), 0)
        pid = ctypes.c_uint32()
        foreground = self.user.GetForegroundWindow()
        if foreground and self.user.GetLastInputInfo(ctypes.byref(activity)):
            self.user.GetWindowThreadProcessId(foreground, ctypes.byref(pid))
            elapsed = (self.kernel.GetTickCount() - activity.time) & RUNTIME_DWORD_MASK
            result["other_app_active"] = bool(pid.value and pid.value != os.getpid() and elapsed < RUNTIME_BOOTSTRAP_ACTIVITY_SECONDS * RUNTIME_MILLISECONDS_PER_SECOND)
        return result


def process_token(pid):
    pid = int(pid or 0)
    if pid <= 0:
        return ""
    if os.name == "nt":
        kernel = ctypes.WinDLL("kernel32", use_last_error=True)
        kernel.OpenProcess.argtypes = [ctypes.c_uint32, ctypes.c_int, ctypes.c_uint32]
        kernel.OpenProcess.restype = ctypes.c_void_p
        kernel.GetProcessTimes.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
        kernel.GetProcessTimes.restype = ctypes.c_int
        kernel.CloseHandle.argtypes = [ctypes.c_void_p]
        kernel.CloseHandle.restype = ctypes.c_int
        handle = kernel.OpenProcess(RUNTIME_WIN32_PROCESS_QUERY_LIMITED, 0, pid)
        if not handle:
            return ""
        try:
            created = ctypes.c_uint64()
            exited = ctypes.c_uint64()
            kernel_time = ctypes.c_uint64()
            user_time = ctypes.c_uint64()
            if kernel.GetProcessTimes(handle, ctypes.byref(created), ctypes.byref(exited), ctypes.byref(kernel_time), ctypes.byref(user_time)):
                return str(created.value)
        finally:
            kernel.CloseHandle(handle)
        return ""
    try:
        raw = pathlib.Path("/proc") / str(pid) / "stat"
        data = raw.read_text(encoding="utf-8")
        return data.rsplit(")", 1)[1].split()[RUNTIME_LINUX_PROC_STARTTIME_INDEX]
    except (OSError, IndexError):
        return ""


def process_running(pid, token):
    if not token or process_token(pid) != token:
        return False
    if os.name == "nt":
        kernel = ctypes.WinDLL("kernel32", use_last_error=True)
        kernel.OpenProcess.argtypes = [ctypes.c_uint32, ctypes.c_int, ctypes.c_uint32]
        kernel.OpenProcess.restype = ctypes.c_void_p
        kernel.WaitForSingleObject.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
        kernel.WaitForSingleObject.restype = ctypes.c_uint32
        kernel.CloseHandle.argtypes = [ctypes.c_void_p]
        kernel.CloseHandle.restype = ctypes.c_int
        handle = kernel.OpenProcess(RUNTIME_WIN32_SYNCHRONIZE, 0, int(pid))
        if not handle:
            return False
        try:
            return kernel.WaitForSingleObject(handle, 0) == RUNTIME_WIN32_WAIT_TIMEOUT
        finally:
            kernel.CloseHandle(handle)
    try:
        line = (pathlib.Path("/proc") / str(int(pid)) / "stat").read_text(encoding="utf-8")
        return line.rsplit(")", 1)[1].split()[0] not in ("Z", "X")
    except OSError:
        return False


def persisted_run_record(root):
    root = pathlib.Path(root)
    candidates = []
    stored = read_json(root / "state" / "run-intent.json", None)
    if isinstance(stored, dict) and type(stored.get("desired_running")) is bool:
        try:
            revision = max(0, int(stored.get("revision", 0)))
        except (TypeError, ValueError):
            revision = 0
        candidates.append((revision, stored["desired_running"]))
    database = root / "data" / "memory.sqlite3"
    if database.is_file():
        connection = None
        try:
            connection = sqlite3.connect(database.resolve().as_uri() + "?mode=ro", uri=True, timeout=RUNTIME_STATE_READ_TIMEOUT_SECONDS)
            rows = connection.execute("SELECT key,value FROM settings WHERE key IN ('run_intent','desired_running')").fetchall()
            for key, value in rows:
                try:
                    item = json.loads(value)
                except (TypeError, ValueError):
                    continue
                if key == "run_intent" and isinstance(item, dict) and type(item.get("desired_running")) is bool:
                    try:
                        revision = max(0, int(item.get("revision", 0)))
                    except (TypeError, ValueError):
                        revision = 0
                    candidates.append((revision, item["desired_running"]))
                elif key == "desired_running" and type(item) is bool:
                    candidates.append((0, item))
        except (OSError, ValueError, TypeError, sqlite3.Error):
            pass
        finally:
            if connection is not None:
                connection.close()
    if not candidates:
        return None
    revision, running = max(candidates, key=lambda item: (item[0], not item[1]))
    return {"desired_running": running, "revision": revision}


def supervisor_process(root, initial_pid):
    root = pathlib.Path(root).resolve()
    state = root / "state" / "supervisor.json"
    logfile = root / "logs" / "supervisor-restarts.jsonl"
    logfile.parent.mkdir(parents=True, exist_ok=True)
    pid = int(initial_pid)
    token = process_token(pid)
    if not token:
        return
    starts = 0
    child = None
    warned = False
    stalled_checks = 0
    latch = SessionRunLatch(root)
    try:
        while True:
            snapshot = read_json(state, {})
            if not isinstance(snapshot, dict):
                snapshot = {}
            valid = child.poll() is None if child is not None and child.pid == pid else process_running(pid, token)
            if valid:
                if snapshot.get("pid") == pid and snapshot.get("token") == token:
                    if snapshot.get("closing"):
                        return
                    try:
                        stale = time.time() - float(snapshot.get("heartbeat", 0))
                        progress_age = float(snapshot.get("progress_age_seconds", 0))
                        expected = float(snapshot.get("expected_progress_seconds") or RUNTIME_SUPERVISOR_HEARTBEAT_SECONDS)
                    except (ValueError, TypeError, OverflowError):
                        stale, progress_age, expected = 0.0, 0.0, RUNTIME_SUPERVISOR_HEARTBEAT_SECONDS
                    progress_stalled = snapshot.get("phase") in CONTROL_MONITORED_WORK_PHASES and progress_age > max(RUNTIME_SUPERVISOR_HEARTBEAT_SECONDS, expected * RUNTIME_ADB_RECOVERY_CONFIRMATIONS)
                    stalled = bool(snapshot.get("desired_running")) and not latch.is_stopped() and (stale > RUNTIME_SUPERVISOR_HEARTBEAT_SECONDS or progress_stalled)
                    stalled_checks = stalled_checks + 1 if stalled else 0
                    if stalled and not warned:
                        with logfile.open("a", encoding="utf-8") as handle:
                            handle.write(json.dumps({"time": utc_now(), "reason": "worker_or_heartbeat_stalled", "pid": pid, "phase": snapshot.get("phase"), "progress_age_seconds": progress_age, "action": "confirm_before_restart"}, ensure_ascii=False) + "\n")
                    warned = stalled
                    if stalled_checks >= RUNTIME_ADB_RECOVERY_CONFIRMATIONS and not latch.is_stopped() and process_token(pid) == token:
                        with logfile.open("a", encoding="utf-8") as handle:
                            handle.write(json.dumps({"time": utc_now(), "reason": "worker_or_heartbeat_stalled", "pid": pid, "action": "terminate_for_supervised_restart"}, ensure_ascii=False) + "\n")
                        try:
                            if child is not None and child.pid == pid and child.poll() is None:
                                child.kill()
                            else:
                                os.kill(pid, signal.SIGTERM)
                        except (OSError, ValueError) as exc:
                            with logfile.open("a", encoding="utf-8") as handle:
                                handle.write(json.dumps({"time": utc_now(), "reason": "stalled_termination_failed", "pid": pid, "error": str(exc)}, ensure_ascii=False) + "\n")
                        stalled_checks = 0
                time.sleep(RUNTIME_SUPERVISOR_POLL_SECONDS)
                continue
            if latch.is_stopped() or snapshot.get("closing"):
                return
            starts += 1
            try:
                program = pathlib.Path(__file__).resolve()
                with (root / "logs" / "supervisor-output.log").open("ab", buffering=0) as output:
                    if latch.is_stopped():
                        return
                    flags = getattr(subprocess, "CREATE_NO_WINDOW", 0) if os.name == "nt" else 0
                    child = subprocess.Popen([sys.executable, str(program), "--resume-root", str(root)], stdin=subprocess.DEVNULL, stdout=output, stderr=subprocess.STDOUT, cwd=str(root), creationflags=flags, shell=False)
                pid = child.pid
                token = process_token(pid)
                deadline = time.monotonic() + RUNTIME_PROCESS_IDENTITY_WAIT_SECONDS
                while not token and child.poll() is None and time.monotonic() < deadline:
                    if latch.is_stopped():
                        return
                    time.sleep(RUNTIME_SOCKET_POLL_SECONDS)
                    token = process_token(pid)
                atomic_json(state, {"pid": pid, "token": token, "heartbeat": time.time(), "progress_age_seconds": 0, "phase": "relaunching", "desired_running": not latch.is_stopped(), "closing": False, "restart_count": starts})
                with logfile.open("a", encoding="utf-8") as handle:
                    handle.write(json.dumps({"time": utc_now(), "reason": "process_exited", "pid": pid, "restart_count": starts}, ensure_ascii=False) + "\n")
                warned = False
                stalled_checks = 0
            except Exception as exc:
                with logfile.open("a", encoding="utf-8") as handle:
                    handle.write(json.dumps({"time": utc_now(), "reason": "spawn_failed", "error": str(exc)}, ensure_ascii=False) + "\n")
            time.sleep(min(RUNTIME_SUPERVISOR_RETRY_MAX_SECONDS, RUNTIME_SUPERVISOR_POLL_SECONDS * max(1, starts)))
    finally:
        latch.close()


def axml_min_sdk(data):
    data = bytes(data)
    if data.lstrip().startswith(b"<"):
        try:
            root = ET.fromstring(data)
            sdk = root.find("uses-sdk")
            value = sdk.get("{" + RUNTIME_ANDROID_NAMESPACE + "}minSdkVersion") if sdk is not None else None
            return int(value) if value is not None and value.isdecimal() else None
        except (ET.ParseError, ValueError, UnicodeError):
            return None
    header = RUNTIME_ANDROID_XML_CHUNK
    if len(data) < header.size:
        return None
    kind, file_header, file_size = header.unpack_from(data)
    if kind != RUNTIME_ANDROID_XML_KIND or file_header < header.size or file_header > file_size or file_size > len(data):
        return None
    strings = []
    at = file_header
    try:
        while at + header.size <= file_size:
            kind, header_size, chunk_size = header.unpack_from(data, at)
            end = at + chunk_size
            if chunk_size < header_size or header_size < header.size or end > file_size:
                return None
            if kind == RUNTIME_ANDROID_XML_STRING_POOL_KIND:
                if header_size < header.size + RUNTIME_ANDROID_XML_STRING_POOL.size:
                    return None
                string_count, style_count, flags, strings_start, styles_start = RUNTIME_ANDROID_XML_STRING_POOL.unpack_from(data, at + header.size)
                table_end = header_size + (string_count + style_count) * RUNTIME_ANDROID_XML_WORD.size
                if table_end > strings_start or strings_start > chunk_size or styles_start and not strings_start <= styles_start <= chunk_size:
                    return None
                string_limit = at + (styles_start or chunk_size)
                def length8(position):
                    if position >= string_limit:
                        raise ValueError("字符串长度越界")
                    first = data[position]
                    position += 1
                    if first & RUNTIME_ANDROID_XML_LENGTH8_HIGH:
                        if position >= string_limit:
                            raise ValueError("字符串长度越界")
                        return ((first & (RUNTIME_ANDROID_XML_LENGTH8_HIGH - 1)) << RUNTIME_ANDROID_XML_BYTE_BITS) | data[position], position + 1
                    return first, position
                def length16(position):
                    if position + RUNTIME_ANDROID_XML_SHORT.size > string_limit:
                        raise ValueError("字符串长度越界")
                    first = RUNTIME_ANDROID_XML_SHORT.unpack_from(data, position)[0]
                    position += RUNTIME_ANDROID_XML_SHORT.size
                    if first & RUNTIME_ANDROID_XML_LENGTH16_HIGH:
                        if position + RUNTIME_ANDROID_XML_SHORT.size > string_limit:
                            raise ValueError("字符串长度越界")
                        second = RUNTIME_ANDROID_XML_SHORT.unpack_from(data, position)[0]
                        return ((first & (RUNTIME_ANDROID_XML_LENGTH16_HIGH - 1)) << RUNTIME_ANDROID_XML_SHORT_BITS) | second, position + RUNTIME_ANDROID_XML_SHORT.size
                    return first, position
                for index in range(string_count):
                    offset = RUNTIME_ANDROID_XML_WORD.unpack_from(data, at + header_size + index * RUNTIME_ANDROID_XML_WORD.size)[0]
                    position = at + strings_start + offset
                    if position < at + strings_start or position >= string_limit:
                        return None
                    if flags & RUNTIME_ANDROID_XML_UTF8:
                        _, position = length8(position)
                        size, position = length8(position)
                        if position + size >= string_limit or data[position + size] != 0:
                            return None
                        text = data[position:position + size].decode("utf-8")
                    else:
                        size, position = length16(position)
                        byte_count = size * RUNTIME_ANDROID_XML_SHORT.size
                        if position + byte_count + RUNTIME_ANDROID_XML_SHORT.size > string_limit or RUNTIME_ANDROID_XML_SHORT.unpack_from(data, position + byte_count)[0] != 0:
                            return None
                        text = data[position:position + byte_count].decode("utf-16-le")
                    strings.append(text)
            elif kind == RUNTIME_ANDROID_XML_START_ELEMENT_KIND:
                node_bytes = header.size + RUNTIME_ANDROID_XML_NODE.size
                if header_size < node_bytes or at + header_size + RUNTIME_ANDROID_XML_START_ELEMENT.size > end:
                    return None
                _, name, attribute_start, attribute_size, attribute_count, _, _, _ = RUNTIME_ANDROID_XML_START_ELEMENT.unpack_from(data, at + header_size)
                if not 0 <= name < len(strings):
                    return None
                if strings[name] != "uses-sdk":
                    at = end
                    continue
                attributes_at = at + header_size + attribute_start
                if attribute_start < RUNTIME_ANDROID_XML_START_ELEMENT.size or attribute_size < RUNTIME_ANDROID_XML_ATTRIBUTE.size or attributes_at + attribute_size * attribute_count > end:
                    return None
                for index in range(attribute_count):
                    field = attributes_at + attribute_size * index
                    namespace, name, raw, value_size, _, value_kind, value = RUNTIME_ANDROID_XML_ATTRIBUTE.unpack_from(data, field)
                    if value_size != RUNTIME_ANDROID_XML_WORD.size + RUNTIME_ANDROID_XML_SHORT.size + 1 + 1:
                        return None
                    if not 0 <= name < len(strings) or strings[name] != "minSdkVersion":
                        continue
                    if not 0 <= namespace < len(strings) or strings[namespace] != RUNTIME_ANDROID_NAMESPACE:
                        continue
                    if value_kind in RUNTIME_ANDROID_XML_INTEGER_TYPES:
                        return int(value) if value > 0 else None
                    if value_kind == RUNTIME_ANDROID_XML_STRING_TYPE and 0 <= value < len(strings) and strings[value].isdecimal():
                        return int(strings[value])
                    if 0 <= raw < len(strings) and strings[raw].isdecimal():
                        return int(strings[raw])
                return None
            at = end
    except (IndexError, struct.error, UnicodeError, ValueError, OverflowError):
        return None
    return None


def selected_apk_files(paths):
    values = paths if isinstance(paths, (tuple, list)) else [paths]
    if not values:
        raise ValueError("请选择游戏 APK 文件")
    files = [pathlib.Path(value).resolve() for value in values]
    if len(files) != len(set(files)) or any(not file.is_file() or file.suffix.lower() != ".apk" for file in files):
        raise ValueError("请选择有效且不重复的 APK 文件")
    return files


def _apk_compatibility_uncached(path):
    path = pathlib.Path(path)
    with zipfile.ZipFile(path) as archive:
        try:
            manifest = archive.getinfo("AndroidManifest.xml")
        except KeyError as exc:
            raise ValueError("APK 缺少 AndroidManifest.xml") from exc
        if not 0 < manifest.file_size <= RUNTIME_APK_MANIFEST_BYTES:
            raise ValueError("APK 应用清单异常")
        min_sdk = axml_min_sdk(archive.read(manifest))
        libraries = set()
        for item in archive.infolist():
            parts = item.filename.split("/")
            if len(parts) >= ANDROID_APK_LIB_PATH_FIELDS and parts[0] == "lib" and parts[-1].endswith(".so"):
                libraries.add(parts[1])
    return {"min_sdk": min_sdk, "native_abis": sorted(libraries)}


ANDROID_SYNC_HEADER = struct.Struct("<4sI")


ANDROID_SYNC_DATA_BYTES = 64 * RUNTIME_BYTES_PER_KIB


ANDROID_SYNC_FILE_MODE = 0o100644


ANDROID_DEFAULT_PACKAGE_NAME_PATTERN = r"[A-Za-z0-9_]+(?:\.[A-Za-z0-9_]+)+"


ANDROID_APK_LIB_PATH_FIELDS = 3


RUNTIME_APK_METADATA_CACHE_ENTRIES = RUNTIME_COMPUTE_CONSUMERS * RUNTIME_ADB_LENGTH_DIGITS


def _apk_package_info_uncached(path):
    path = Path(path)
    with zipfile.ZipFile(path) as archive:
        record = archive.getinfo("AndroidManifest.xml")
        if not 0 < record.file_size <= RUNTIME_APK_MANIFEST_BYTES:
            raise ValueError("APK 应用清单大小无效")
        data = archive.read(record)
    if data.lstrip().startswith(b"<"):
        element = ET.fromstring(data)
        if element.tag != "manifest":
            raise ValueError("APK 应用清单没有 manifest 根节点")
        attributes = {"package": element.get("package", ""), "split": element.get("split", ""), "versionCode": element.get("{" + RUNTIME_ANDROID_NAMESPACE + "}versionCode", ""), "versionCodeMajor": element.get("{" + RUNTIME_ANDROID_NAMESPACE + "}versionCodeMajor", "")}
    else:
        chunk = RUNTIME_ANDROID_XML_CHUNK
        if len(data) < chunk.size:
            raise ValueError("APK 二进制清单被截断")
        kind, header_size, file_size = chunk.unpack_from(data)
        if kind != RUNTIME_ANDROID_XML_KIND or not chunk.size <= header_size <= file_size <= len(data):
            raise ValueError("APK 二进制清单头无效")
        strings = []
        attributes = None
        position = header_size
        while position + chunk.size <= file_size:
            kind, current_header, size = chunk.unpack_from(data, position)
            end = position + size
            if not chunk.size <= current_header <= size or end > file_size:
                raise ValueError("APK 清单区块越界")
            if kind == RUNTIME_ANDROID_XML_STRING_POOL_KIND:
                if current_header < chunk.size + RUNTIME_ANDROID_XML_STRING_POOL.size:
                    raise ValueError("APK 清单字符串表头被截断")
                count, style_count, flags, start, styles = RUNTIME_ANDROID_XML_STRING_POOL.unpack_from(data, position + chunk.size)
                if current_header + (count + style_count) * RUNTIME_ANDROID_XML_WORD.size > start or not start <= size or styles and not start <= styles <= size:
                    raise ValueError("APK 清单字符串表范围无效")
                limit = position + (styles or size)
                def read_length(at, wide):
                    unit = RUNTIME_ANDROID_XML_SHORT.size if wide else 1
                    if at + unit > limit:
                        raise ValueError("APK 清单字符串长度越界")
                    first = RUNTIME_ANDROID_XML_SHORT.unpack_from(data, at)[0] if wide else data[at]
                    at += unit
                    high = RUNTIME_ANDROID_XML_LENGTH16_HIGH if wide else RUNTIME_ANDROID_XML_LENGTH8_HIGH
                    bits = RUNTIME_ANDROID_XML_SHORT_BITS if wide else RUNTIME_ANDROID_XML_BYTE_BITS
                    if first & high:
                        if at + unit > limit:
                            raise ValueError("APK 清单字符串长度越界")
                        second = RUNTIME_ANDROID_XML_SHORT.unpack_from(data, at)[0] if wide else data[at]
                        return ((first & (high - 1)) << bits) | second, at + unit
                    return first, at
                for index in range(count):
                    offset = RUNTIME_ANDROID_XML_WORD.unpack_from(data, position + current_header + index * RUNTIME_ANDROID_XML_WORD.size)[0]
                    at = position + start + offset
                    if not position + start <= at < limit:
                        raise ValueError("APK 清单字符串偏移无效")
                    if flags & RUNTIME_ANDROID_XML_UTF8:
                        _, at = read_length(at, False)
                        length, at = read_length(at, False)
                        if at + length >= limit or data[at + length] != 0:
                            raise ValueError("APK 清单 UTF-8 字符串被截断")
                        strings.append(data[at:at + length].decode("utf-8"))
                    else:
                        length, at = read_length(at, True)
                        byte_count = length * RUNTIME_ANDROID_XML_SHORT.size
                        if at + byte_count + RUNTIME_ANDROID_XML_SHORT.size > limit or RUNTIME_ANDROID_XML_SHORT.unpack_from(data, at + byte_count)[0] != 0:
                            raise ValueError("APK 清单 UTF-16 字符串被截断")
                        strings.append(data[at:at + byte_count].decode("utf-16-le"))
            elif kind == RUNTIME_ANDROID_XML_START_ELEMENT_KIND:
                if current_header < chunk.size + RUNTIME_ANDROID_XML_NODE.size or position + current_header + RUNTIME_ANDROID_XML_START_ELEMENT.size > end:
                    raise ValueError("APK 清单节点被截断")
                _, name, attribute_start, attribute_size, count, _, _, _ = RUNTIME_ANDROID_XML_START_ELEMENT.unpack_from(data, position + current_header)
                if not 0 <= name < len(strings):
                    raise ValueError("APK 清单节点名称无效")
                if strings[name] != "manifest":
                    position = end
                    continue
                at = position + current_header + attribute_start
                if attribute_start < RUNTIME_ANDROID_XML_START_ELEMENT.size or attribute_size < RUNTIME_ANDROID_XML_ATTRIBUTE.size or at + attribute_size * count > end:
                    raise ValueError("APK 清单属性范围无效")
                attributes = {}
                for index in range(count):
                    namespace, name, raw, value_size, reserved, value_kind, value = RUNTIME_ANDROID_XML_ATTRIBUTE.unpack_from(data, at + index * attribute_size)
                    if not 0 <= name < len(strings):
                        raise ValueError("APK 清单属性名称无效")
                    label = strings[name]
                    if label in {"package", "split"} and namespace != RUNTIME_DWORD_MASK:
                        continue
                    if label in {"versionCode", "versionCodeMajor"} and not (0 <= namespace < len(strings) and strings[namespace] == RUNTIME_ANDROID_NAMESPACE):
                        continue
                    if 0 <= raw < len(strings):
                        resolved = strings[raw]
                    elif value_kind == RUNTIME_ANDROID_XML_STRING_TYPE and 0 <= value < len(strings):
                        resolved = strings[value]
                    elif value_kind in RUNTIME_ANDROID_XML_INTEGER_TYPES:
                        resolved = str(value)
                    else:
                        continue
                    attributes[label] = resolved
                break
            position = end
        if attributes is None:
            raise ValueError("无法读取 APK 包名，未执行安装")
    package = str(attributes.get("package", ""))
    split = str(attributes.get("split", ""))
    if not re.fullmatch(ANDROID_DEFAULT_PACKAGE_NAME_PATTERN, package):
        raise ValueError("APK 包名无效，未执行安装")
    if split and not re.fullmatch(r"[A-Za-z0-9_.-]+", split):
        raise ValueError("APK 分包名称无效")
    return {"package": package, "split": split, "version_code": str(attributes.get("versionCode", "")), "version_code_major": str(attributes.get("versionCodeMajor", ""))}


def _apk_cache_key(path):
    file = pathlib.Path(path).resolve()
    record = file.stat()
    return str(file), record.st_size, record.st_mtime_ns


@functools.lru_cache(maxsize=RUNTIME_APK_METADATA_CACHE_ENTRIES)
def _apk_cached_metadata(name, size, modified_ns):
    file = pathlib.Path(name)
    current = file.stat()
    if current.st_size != size or current.st_mtime_ns != modified_ns:
        raise ValueError("APK 文件在读取过程中发生变化")
    return _apk_compatibility_uncached(file), _apk_package_info_uncached(file)


def apk_compatibility(path):
    metadata = _apk_cached_metadata(*_apk_cache_key(path))[0]
    return {**metadata, "native_abis": list(metadata["native_abis"])}


def apk_package_info(path):
    return dict(_apk_cached_metadata(*_apk_cache_key(path))[1])


class AndroidRuntime:
    IMAGE_PACKAGE = "system-images;android-0;local;x86_64"

    def __init__(self, root, log, status, total_memory_mb=None):
        self.base = Path(root)
        self.root = self.base / "android"
        self.sdk = self.root / "sdk"
        self.user_home = self.root / "user"
        self.avd_home = self.user_home / "avd"
        marker = read_json(self.root / "runtime.json", {})
        installed_image = marker.get("image_package", "") if isinstance(marker, dict) else ""
        self.IMAGE_PACKAGE = installed_image if re.fullmatch(r"system-images;android-\d+;[A-Za-z0-9_]+;(?:x86_64|x86|arm64-v8a|armeabi-v7a)", str(installed_image)) else self.IMAGE_PACKAGE
        self.avd_name = "GameAI_API" + self.IMAGE_PACKAGE.split(";")[1].split("-")[-1]
        self.avd = self.avd_home / (self.avd_name + ".avd")
        self.cache = self.base / "cache" / "android"
        self.logs = self.base / "logs"
        self.temp = self.root / "temp"
        self.profile = self.root / "profile"
        self.log = log
        self.status = status
        self.total_memory_mb = int(total_memory_mb) if total_memory_mb is not None else physical_memory_mb()
        self.memory_mb = RUNTIME_BOOTSTRAP_ANDROID_MEMORY_MB
        self.cores = max(1, (os.cpu_count() or 1) // RUNTIME_COMPUTE_CONSUMERS)
        self.measurements = RuntimeMeasurements(self.base / "state" / "android-measurements.json")
        self.emulator = self.sdk / "emulator" / "emulator.exe"
        self.adb = self.sdk / "platform-tools" / "adb.exe"
        self.image = self.sdk.joinpath(*self.IMAGE_PACKAGE.split(";"))
        self.marker = self.root / "runtime.json"
        self.process = None
        self.adb_process = None
        self._emulator_job = None
        self._adb_job = None
        self.console_port = None
        self.adb_port = None
        self.serial = None
        self.acceleration = None
        self.gpu_mode = "host"
        self._graphics_identity_value = ""
        self._graphics_profile_path = self.base / "state" / "android-graphics.json"
        self.booted = False
        self.width, self.height, self._refresh_hz = runtime_default_display()
        self._long_press_ms = RUNTIME_BOOTSTRAP_LONG_PRESS_MS
        self._closed = False
        self._prepared = False
        self._action_lock = threading.RLock()
        self._adb_io_lock = threading.RLock()
        self._adb_stream_lock = threading.RLock()
        self._adb_streams = set()
        self._capture_lock = threading.RLock()
        self._hierarchy_lock = threading.RLock()
        self._console_lock = threading.RLock()
        self._geometry_lock = threading.RLock()
        self._console_socket = None
        self._console_buffer = bytearray()
        self._touches = {}
        self._input_layout = None
        self._touch_tracking_id = 0
        self._display_rotation = 0
        self._display_size = (self.width, self.height)
        self._geometry_dirty = True
        self._geometry_at = 0.0
        self._geometry_requested = 0
        self._geometry_applied = 0
        self._geometry_changes = 0
        self._geometry_stop = threading.Event()
        self._geometry_thread = None
        self._next_hierarchy = 0.0
        self._hierarchy_cache = "<hierarchy/>"
        self.hierarchy_started_at = 0.0
        self.hierarchy_finished_at = 0.0
        self._hierarchy_failures = 0
        self.abis = []
        self.native_bridge = ""
        self.device_api_level = 0
        self._last_context = {}
        self._last_context_at = 0.0
        self._package_lock = threading.RLock()
        self._user_packages = set()
        self._user_packages_at = 0.0
        self._last_health = 0.0
        self._adb_restarts = 0
        self._failures = 0
        self._force_cold_boot = False
        self._snapshot_enabled = False
        self._snapshot_signature = ""
        self._boot_mode = "cold"
        self._launch_wall_ns = 0
        self._launched_avd = None
        self.env = None
        self.owned = True
        self._external = False
        self._local_authorized = False
        self._connection_marker = self.base / "state" / "android-connection.json"
        self._input_backend = "unavailable"
        self._input_commands = set()
        self._input_verified = False
        self._resource_budget = {}
        self._motion_event = False
        self._pending_external_release = None
        self._existing_unicode_ime = False
        self.last_installed_packages = []

    @staticmethod
    def _tag(element):
        return element.tag.rsplit("}", 1)[-1]

    def _dirs(self):
        for path in (self.root, self.user_home, self.avd_home, self.cache, self.logs, self.temp, self.profile, self.profile / "AppData" / "Local", self.profile / "AppData" / "Roaming"):
            path.mkdir(parents=True, exist_ok=True)

    def _critical_files(self):
        if self._external:
            return {}
        kernel = next((path for path in (self.image / "kernel-ranchu", self.image / "kernel-ranchu-64") if path.is_file()), self.image / "kernel-ranchu")
        return {"emulator": self.emulator, "adb": self.adb, "system_image": self.image / "system.img", "userdata_image": self.image / "userdata.img", "kernel": kernel, "ramdisk": self.image / "ramdisk.img"}

    def ready(self, cancel=None):
        check_cancel(cancel)
        if not self._prepared:
            return False
        if self._external:
            return self.adb_port is not None and self.serial is not None
        try:
            return all(path.is_file() and path.stat().st_size > 0 for path in self._critical_files().values())
        except OSError:
            return False

    def prepare(self, cancel=None):
        check_cancel(cancel)
        self._dirs()
        if self.ready(cancel):
            return
        self.status("正在检查本地安卓组件与本工作区独立实例")
        installed = read_json(self.marker, {})
        if self._attach_local_emulator(cancel):
            return
        cached = self._cached_system_image(installed)
        choices = [cached] if cached is not None else self._local_system_images(cancel=cancel)
        if not choices:
            self._install_official_sdk(cancel)
            choices = self._local_system_images(cancel=cancel)
            if not choices:
                raise ComponentFailure("android_assets", "安卓组件安装后仍找不到完整的系统镜像")
        preferred = installed.get("image_directory") if isinstance(installed, dict) else None
        preferred_package = installed.get("image_package") if isinstance(installed, dict) else None
        choice = next((item for item in choices if str(item[-1]) == preferred), None)
        if choice is None:
            choice = next((item for item in choices if "system-images;android-" + str(item[0]) + ";" + item[-1].parent.name + ";" + item[-1].name == preferred_package), choices[0])
        self._select_local_image(choice)
        self.status("本地安卓组件已就绪")

    @staticmethod
    def _xml_value(element, name):
        return str(element.findtext("{*}" + name, default="") or "").strip()

    def _official_manifest(self, relative, cancel=None):
        check_cancel(cancel)
        url = urllib.parse.urljoin(ANDROID_OFFICIAL_REPOSITORY, relative)
        request = urllib.request.Request(url, headers={"User-Agent": "GameAI/" + APP_VERSION, "Accept": "application/xml"})
        try:
            with urllib.request.urlopen(request, timeout=ANDROID_HTTP_TIMEOUT_SECONDS) as response:
                chunks = bytearray()
                while True:
                    check_cancel(cancel)
                    block = response.read(ANDROID_DOWNLOAD_BLOCK_BYTES)
                    if not block:
                        break
                    chunks.extend(block)
                    if len(chunks) > ANDROID_METADATA_MAX_BYTES:
                        raise ValueError("官方 Android 组件目录超过限制")
            return ET.fromstring(chunks)
        except (OSError, ValueError, TimeoutError, ET.ParseError) as exc:
            raise ComponentFailure("android_assets", "无法读取 Google 官方 Android SDK 目录：" + str(exc)) from exc

    @classmethod
    def _official_records(cls, manifest, relative, packages, host=None):
        result = []
        for node in manifest.findall(".//{*}remotePackage"):
            package = str(node.get("path", ""))
            if str(node.get("obsolete", "false")).casefold() == "true" or package not in packages:
                continue
            channel = node.find("{*}channelRef")
            if channel is not None and channel.get("ref", "channel-0") != "channel-0":
                continue
            revision = node.find("{*}revision")
            version = tuple(int(cls._xml_value(revision, field) or "0") if revision is not None else 0 for field in ("major", "minor", "micro"))
            for archive in node.findall("{*}archives/{*}archive"):
                complete = archive.find("{*}complete")
                if complete is None:
                    continue
                host_os = cls._xml_value(archive, "host-os").lower()
                architecture = cls._xml_value(archive, "host-arch").casefold()
                bits = cls._xml_value(archive, "host-bits")
                name = cls._xml_value(complete, "url")
                if host == "windows" and architecture and architecture not in {"x86_64", "amd64", "x86", "any"}:
                    continue
                if host and (host_os and host_os != host or not host_os and host not in name.lower()):
                    continue
                if bits and bits != ANDROID_HOST_BITS:
                    continue
                checksum = complete.find("{*}checksum")
                size = cls._xml_value(complete, "size")
                if checksum is None or not size.isdecimal() or not name.endswith(".zip"):
                    continue
                method = str(checksum.get("type", "sha1")).lower()
                digest = str(checksum.text or "").strip().lower()
                if method not in {"sha1", "sha256"} or not re.fullmatch(r"[0-9a-f]+", digest) or len(digest) != hashlib.new(method).digest_size * AI_HEXADECIMAL_DIGITS_PER_BYTE:
                    continue
                count = int(size)
                if not 0 < count <= ANDROID_ARCHIVE_MAX_BYTES:
                    continue
                url = urllib.parse.urljoin(urllib.parse.urljoin(ANDROID_OFFICIAL_REPOSITORY, relative), name)
                parsed = urllib.parse.urlsplit(url)
                if parsed.scheme != "https" or parsed.hostname != "dl.google.com":
                    continue
                result.append({"package": package, "version": version, "url": url, "size": count, "algorithm": method, "digest": digest})
        return result

    def _download_official(self, record, cancel=None):
        self.cache.mkdir(parents=True, exist_ok=True)
        key = hashlib.sha256(record["url"].encode("utf-8")).hexdigest()
        final = safe_workspace_file(self.base, self.cache / (key + ".zip"))
        part = safe_workspace_file(self.base, self.cache / (key + ".part"))
        expected = record["size"]
        if final.is_file():
            if final.stat().st_size == expected and hash_file(final, record["algorithm"], cancel) == record["digest"]:
                return final
            final.unlink()
        if shutil.disk_usage(self.root).free < max(ANDROID_MIN_FREE_DISK_BYTES, expected + RUNTIME_ANDROID_MIN_FREE_DISK_BYTES):
            raise ComponentFailure("resources", "安卓镜像安装需要工作盘留有至少 10 GiB 空间")
        for attempt in range(ANDROID_DOWNLOAD_RETRIES):
            check_cancel(cancel)
            offset = part.stat().st_size if part.exists() else 0
            if offset == expected and hash_file(part, record["algorithm"], cancel) == record["digest"]:
                os.replace(part, final)
                return final
            if offset >= expected:
                part.unlink()
                offset = 0
            headers = {"User-Agent": "GameAI/" + APP_VERSION}
            if offset:
                headers["Range"] = "bytes=" + str(offset) + "-"
            self.status("下载官方安卓组件 " + record["package"] + " · " + str(round(offset / RUNTIME_BYTES_PER_MIB)) + "/" + str(round(expected / RUNTIME_BYTES_PER_MIB)) + " MiB")
            try:
                with urllib.request.urlopen(urllib.request.Request(record["url"], headers=headers), timeout=ANDROID_HTTP_TIMEOUT_SECONDS) as response:
                    resume = bool(offset and response.status == 206 and str(response.headers.get("Content-Range", "")).startswith("bytes " + str(offset) + "-"))
                    done = offset if resume else 0
                    shown = time.monotonic()
                    with part.open("ab" if resume else "wb") as stream:
                        while True:
                            check_cancel(cancel)
                            data = response.read(ANDROID_DOWNLOAD_BLOCK_BYTES)
                            if not data:
                                break
                            done += len(data)
                            if done > expected:
                                raise ValueError("安卓组件下载超过官方声明的文件长度")
                            stream.write(data)
                            if time.monotonic() - shown >= ANDROID_DOWNLOAD_UPDATE_SECONDS:
                                self.status("下载 " + record["package"] + " · " + str(round(done / RUNTIME_BYTES_PER_MIB)) + "/" + str(round(expected / RUNTIME_BYTES_PER_MIB)) + " MiB")
                                shown = time.monotonic()
                if part.stat().st_size != expected:
                    raise OSError("下载内容不完整")
                if hash_file(part, record["algorithm"], cancel) != record["digest"]:
                    part.unlink()
                    raise ValueError("下载内容哈希校验不通过")
                os.replace(part, final)
                self.log("android_official_download_verified", package=record["package"], size=expected)
                return final
            except Cancelled:
                raise
            except (OSError, ValueError, TimeoutError) as exc:
                self.log("android_official_download_retry", package=record["package"], attempt=attempt + 1, error=str(exc))
                if attempt + 1 == ANDROID_DOWNLOAD_RETRIES:
                    raise ComponentFailure("android_assets", "下载安卓组件失败：" + str(exc)) from exc
                self._wait(cancel, ANDROID_RETRY_SECONDS)
        raise ComponentFailure("android_assets", "安卓组件下载失败")

    def _install_archive(self, record, destination, kind, cancel=None):
        archive_path = self._download_official(record, cancel)
        destination = safe_workspace_file(self.base, destination)
        staging = safe_workspace_file(self.base, destination.with_name(destination.name + ".partial-" + uuid.uuid4().hex))
        backup = safe_workspace_file(self.base, destination.with_name(destination.name + ".backup-" + uuid.uuid4().hex))
        staging.mkdir(parents=True, exist_ok=False)
        installed = False
        try:
            with zipfile.ZipFile(archive_path) as z:
                entries = z.infolist()
                total = sum(item.file_size for item in entries)
                if not entries or total > ANDROID_EXTRACT_MAX_BYTES or shutil.disk_usage(self.root).free < total + RUNTIME_ANDROID_MIN_FREE_DISK_BYTES:
                    raise ComponentFailure("resources", "安卓组件文件异常或解压空间不足")
                names = []
                for item in entries:
                    check_cancel(cancel)
                    text = item.filename.replace("\\", "/")
                    parts = pathlib.PurePosixPath(text).parts
                    if not parts or text.startswith("/") or ".." in parts or any(":" in part or "\x00" in part for part in parts) or stat.S_IFMT(item.external_attr >> 16) == stat.S_IFLNK:
                        raise ValueError("官方安卓安装包包含不安全的路径")
                    names.append(parts)
                prefix = ANDROID_ARCHIVE_PREFIXES[kind]
                strip = all(len(name) > 1 and name[0] == prefix for name, item in zip(names, entries) if not item.is_dir())
                for item, parts in zip(entries, names):
                    check_cancel(cancel)
                    relative = parts[1:] if strip and parts[0] == prefix else parts
                    if not relative:
                        continue
                    location = safe_workspace_file(self.base, staging.joinpath(*relative))
                    if item.is_dir():
                        location.mkdir(parents=True, exist_ok=True)
                    else:
                        location.parent.mkdir(parents=True, exist_ok=True)
                        with z.open(item) as inp, location.open("xb") as out:
                            while True:
                                check_cancel(cancel)
                                block = inp.read(ANDROID_DOWNLOAD_BLOCK_BYTES)
                                if not block:
                                    break
                                out.write(block)
            mandatory = ("adb.exe",) if kind == "platform-tools" else ("emulator.exe",) if kind == "emulator" else ("system.img", "userdata.img", "ramdisk.img")
            if any(not (staging / name).is_file() or (staging / name).stat().st_size == 0 for name in mandatory):
                raise ValueError("安卓组件缺少必要的运行文件")
            if kind == "system-image" and not any((staging / name).is_file() for name in ("kernel-ranchu", "kernel-ranchu-64")):
                raise ValueError("安卓系统镜像缺少启动内核")
            if destination.exists():
                if path_is_link(destination):
                    raise ValueError("不允许覆盖链接目录")
                os.replace(destination, backup)
            try:
                os.replace(staging, destination)
            except BaseException:
                if backup.exists():
                    os.replace(backup, destination)
                raise
            installed = True
            self.log("android_official_component_installed", package=record["package"], location=str(destination))
        finally:
            if staging.exists():
                shutil.rmtree(staging, ignore_errors=True)
            if backup.exists() and destination.exists():
                shutil.rmtree(backup, ignore_errors=True)
            if installed:
                with contextlib.suppress(OSError):
                    archive_path.unlink()

    def _official_image(self, minimum_sdk, cancel=None):
        preferred = tuple(api for api in ANDROID_PREFERRED_APIS if api >= minimum_sdk) or (minimum_sdk,)
        targets = {"system-images;android-" + str(api) + ";" + tag + ";x86_64" for api in preferred for tag in ("google_apis", "google_apis_playstore", "default")}
        records = []
        for relative in ANDROID_IMAGE_INDEXES:
            check_cancel(cancel)
            try:
                index = self._official_manifest(relative, cancel)
                records.extend(self._official_records(index, relative, targets))
            except ComponentFailure as exc:
                self.log("android_repository_fallback", index=relative, error=str(exc))
            if any(item["package"].split(";")[2] == "google_apis" for item in records):
                break
        if not records:
            raise ComponentFailure("android_assets", "官方目录中没有满足 Android API " + str(minimum_sdk) + " 的 x86_64 系统镜像")
        order = {api: len(preferred) - index for index, api in enumerate(preferred)}
        tags = {"google_apis": 3, "google_apis_playstore": 2, "default": 1}
        return max(records, key=lambda item: (order.get(int(item["package"].split(";")[1].split("-")[1]), 0), tags.get(item["package"].split(";")[2], 0), item["version"]))

    def _install_official_sdk(self, cancel=None, minimum_sdk=29):
        check_cancel(cancel)
        if os.name != "nt":
            raise ComponentFailure("android_assets", "自动安装安卓模拟器需要 Windows x64")
        self.status("检测到缺少安卓组件，正在自动安装官方 Android SDK")
        sdk = safe_workspace_file(self.base, self.root / "sdk")
        binaries = (("platform-tools", "adb.exe"), ("emulator", "emulator.exe"))
        missing = [(kind, executable) for kind, executable in binaries if not (sdk / kind / executable).is_file() or (sdk / kind / executable).stat().st_size == 0]
        if missing:
            manifest = self._official_manifest(ANDROID_REPOSITORY_INDEX, cancel)
            options = self._official_records(manifest, ANDROID_REPOSITORY_INDEX, {kind for kind, executable in missing}, host="windows")
            for kind, executable in missing:
                candidates = [item for item in options if item["package"] == kind]
                if not candidates:
                    raise ComponentFailure("android_assets", "官方 SDK 目录中缺少 Windows x64 " + kind)
                self._install_archive(max(candidates, key=lambda item: item["version"]), sdk / kind, kind, cancel)
        record = self._official_image(minimum_sdk, cancel)
        directory = sdk.joinpath(*record["package"].split(";"))
        if self._system_image_choice(sdk, directory, minimum_sdk) is None:
            self.status("自动安装 " + record["package"])
            self._install_archive(record, directory, "system-image", cancel)
        if self._system_image_choice(sdk, directory, minimum_sdk) is None:
            raise ComponentFailure("android_assets", "Android 镜像解压后校验失败")
        self.log("android_official_sdk_ready", sdk=str(sdk), image=record["package"])

    @staticmethod
    def _image_supported_abis(choice):
        architecture = choice[-1].name
        if architecture == "x86_64":
            return frozenset(("x86_64", "x86"))
        return frozenset((architecture,))

    def switch_compatible_image(self, minimum_sdk, package_abis, cancel=None):
        check_cancel(cancel)
        if self._external or not self.owned:
            return False
        groups = tuple(frozenset(abis) for abis in package_abis.values() if abis)
        choices = self._local_system_images(minimum_sdk=minimum_sdk, cancel=cancel)
        compatible = [choice for choice in choices if all(not group.isdisjoint(self._image_supported_abis(choice)) for group in groups)]
        if not compatible and minimum_sdk > self.device_api_level and all(not group or not group.isdisjoint({"x86", "x86_64"}) for group in groups):
            self._install_official_sdk(cancel, minimum_sdk=minimum_sdk)
            choices = self._local_system_images(minimum_sdk=minimum_sdk, cancel=cancel)
            compatible = [choice for choice in choices if all(not group.isdisjoint(self._image_supported_abis(choice)) for group in groups)]
        if not compatible:
            return False
        selected = min(compatible, key=lambda item: (item[0] != minimum_sdk, item[0], item[-1].name != self.image.name, item[-1].parent.name != "google_apis"))
        if selected[-1].resolve() == self.image.resolve() and minimum_sdk <= self.device_api_level:
            return False
        self.force_recycle()
        self._select_local_image(selected)
        self.status("已自动选择兼容的 Android API " + str(selected[0]) + " / " + selected[-1].name + " 系统镜像")
        return True

    @staticmethod
    def _configuration(path):
        try:
            lines = Path(path).read_text(encoding="utf-8-sig").splitlines()
        except (OSError, UnicodeError):
            return {}
        return {key.strip(): value.strip() for line in lines if "=" in line and not line.lstrip().startswith(("#", ";")) for key, value in (line.split("=", 1),)}

    def _image_hardware(self):
        values = self._configuration(self.image / "hardware.ini")
        values.update(self._configuration(self.image / "config.ini"))
        return values

    def _minimum_memory_mb(self):
        match = re.match(r"system-images;android-(\d+);", self.IMAGE_PACKAGE)
        api = int(match.group(1)) if match else 0
        if api >= RUNTIME_ANDROID_17_API:
            return RUNTIME_ANDROID_17_MIN_MEMORY_MB
        if api >= RUNTIME_ANDROID_Q_API:
            return RUNTIME_ANDROID_Q_MIN_MEMORY_MB
        return RUNTIME_BOOTSTRAP_ANDROID_MEMORY_MB

    @staticmethod
    def _configuration_memory_mb(value):
        match = re.fullmatch(r"(\d+)\s*([KMGT]?B?)", str(value).strip().upper())
        if match is None:
            return 0
        unit = match.group(2)
        sizes = {"": RUNTIME_BYTES_PER_MIB, "B": 1, "K": RUNTIME_BYTES_PER_KIB, "KB": RUNTIME_BYTES_PER_KIB, "M": RUNTIME_BYTES_PER_MIB, "MB": RUNTIME_BYTES_PER_MIB, "G": RUNTIME_BYTES_PER_GIB, "GB": RUNTIME_BYTES_PER_GIB, "T": RUNTIME_BYTES_PER_GIB * RUNTIME_BYTES_PER_KIB, "TB": RUNTIME_BYTES_PER_GIB * RUNTIME_BYTES_PER_KIB}
        return (int(match.group(1)) * sizes[unit] + RUNTIME_BYTES_PER_MIB - 1) // RUNTIME_BYTES_PER_MIB

    def configure_resource_budget(self, budget, cancel=None):
        check_cancel(cancel)
        result = dict(budget)
        if self.alive() or self._external:
            result.update(android_planned_mb=0, android_allocated_mb=self.memory_mb, android_mb=self.memory_mb, android_cores=self.cores, android_host_overhead_mb=0, resource_selection="running_instance")
            self._resource_budget = result
            return result
        capacity = int(result.get("android_capacity_mb", result.get("android_mb", 0)))
        minimum = self._minimum_memory_mb()
        if capacity < minimum:
            raise ComponentFailure("resources", f"当前安卓镜像至少需要 {minimum} MB 内存，可用安卓预算为 {capacity} MB；正在等待足够资源并保留桌面运行空间")
        values = self._configuration(self.avd / "config.ini")
        hardware = self._image_hardware()
        previous_memory = self._configuration_memory_mb(values.get("hw.ramSize", ""))
        recommended = self._configuration_memory_mb(hardware.get("hw.ramSize", ""))
        if RUNTIME_BOOTSTRAP_ANDROID_MEMORY_MB <= previous_memory <= RUNTIME_EMULATOR_MAX_MEMORY_MB:
            requested = previous_memory
            source = "existing_avd"
        elif recommended > 0:
            requested = recommended
            source = "image_profile"
        else:
            requested = minimum
            source = "emulator_image_minimum"
        self.memory_mb = min(capacity, RUNTIME_EMULATOR_MAX_MEMORY_MB, max(minimum, requested))
        processors = max(1, os.cpu_count() or 1)
        desktop_cores = max(1, math.ceil(processors * CONTROL_DESKTOP_CORE_FRACTION))
        core_capacity = max(1, processors - desktop_cores)
        previous_cores = values.get("hw.cpu.ncore", "")
        selected_cores = int(previous_cores) if previous_cores.isdecimal() and int(previous_cores) > 0 else int(result.get("android_cores", 1))
        self.cores = max(1, min(core_capacity, selected_cores))
        overhead = math.ceil(self.memory_mb * CONTROL_ANDROID_OVERHEAD_FRACTION)
        remaining = max(0, int(result.get("available_mb", 0)) - int(result.get("protected_mb", 0)) - int(result.get("model_mb", 0)))
        result.update(android_capacity_mb=capacity, android_minimum_mb=minimum, android_mb=self.memory_mb, android_cores=self.cores, android_planned_mb=self.memory_mb, android_allocated_mb=0, android_host_overhead_mb=overhead, headroom_mb=max(0, remaining - self.memory_mb - overhead), resource_selection=source, cold_boot_required=self.memory_mb != requested)
        self._resource_budget = result
        self.configure_visual_budget()
        return result

    def _configure_avd(self):
        self._dirs()
        self.avd.mkdir(parents=True, exist_ok=True)
        config_path = self.avd / "config.ini"
        if config_path.exists():
            original = config_path.read_text(encoding="utf-8-sig")
            values = dict(line.split("=", 1) for line in original.splitlines() if "=" in line and not line.lstrip().startswith(("#", ";")))
            values = {key.strip(): value.strip() for key, value in values.items()}
        else:
            original = ""
            values = {
                "AvdId": self.avd_name,
                "avd.ini.displayname": "Android Game AI",
                "avd.ini.encoding": "UTF-8",
                "abi.type": self.image.name,
                "tag.id": self.image.parent.name,
                "tag.display": self.image.parent.name,
                "image.sysdir.1": self.image.resolve().as_posix() + "/",
                "hw.cpu.arch": "arm64" if self.image.name == "arm64-v8a" else "arm" if self.image.name == "armeabi-v7a" else self.image.name,
                "hw.cpu.ncore": str(self.cores),
                "hw.ramSize": str(self.memory_mb),
                "hw.lcd.width": str(self.width),
                "hw.lcd.height": str(self.height),
                "hw.lcd.density": str(round(RUNTIME_BOOTSTRAP_ANDROID_DPI * math.sqrt((self.width * self.height) / (RUNTIME_BOOTSTRAP_DISPLAY_WIDTH * RUNTIME_BOOTSTRAP_DISPLAY_HEIGHT)))),
                "hw.gpu.enabled": "yes",
                "hw.gpu.mode": self.gpu_mode,
                "hw.keyboard": "yes",
                "hw.mainKeys": "no",
                "hw.battery": "yes",
                "hw.gps": "yes",
                "hw.accelerometer": "yes",
                "hw.sensors.orientation": "yes",
                "hw.initialOrientation": "Portrait",
                "hw.audioInput": "no",
                "hw.touchScreen": "multi-touch",
                "disk.cachePartition": "yes",
                "disk.cachePartition.size": str(max(1, self.memory_mb // RUNTIME_ANDROID_CACHE_MEMORY_DIVISOR)) + "M",
                "vm.heapSize": str(max(1, self.memory_mb // RUNTIME_ANDROID_HEAP_MEMORY_DIVISOR)),
                "fastboot.forceColdBoot": "no",
                "showDeviceFrame": "no",
                "PlayStore.enabled": "false",
            }
        values.update({"image.sysdir.1": self.image.resolve().as_posix() + "/", "tag.id": self.image.parent.name, "abi.type": self.image.name, "hw.cpu.arch": "arm64" if self.image.name == "arm64-v8a" else "arm" if self.image.name == "armeabi-v7a" else self.image.name, "hw.cpu.ncore": str(self.cores), "hw.ramSize": str(self.memory_mb), "hw.gpu.mode": self.gpu_mode, "vm.heapSize": str(max(1, self.memory_mb // RUNTIME_ANDROID_HEAP_MEMORY_DIVISOR)), "fastboot.forceColdBoot": "no"})
        partition = values.get("disk.dataPartition.size", "")
        if not self._configuration_memory_mb(partition):
            values.pop("disk.dataPartition.size", None)
            recommended_partition = self._image_hardware().get("disk.dataPartition.size", "")
            if self._configuration_memory_mb(recommended_partition):
                values["disk.dataPartition.size"] = recommended_partition
        self.width = max(1, int(values.get("hw.lcd.width", self.width)))
        self.height = max(1, int(values.get("hw.lcd.height", self.height)))
        content = "\n".join(key + "=" + value for key, value in values.items()) + "\n"
        if original != content:
            safe_workspace_file(self.base, config_path).write_text(content, encoding="utf-8")
        index = self.avd_home / (self.avd_name + ".ini")
        content = "avd.ini.encoding=UTF-8\npath=" + self.avd.resolve().as_posix() + "\ntarget=" + self.IMAGE_PACKAGE.split(";")[1] + "\n"
        if not index.is_file() or index.read_text(encoding="utf-8") != content:
            safe_workspace_file(self.base, index).write_text(content, encoding="utf-8")

    @staticmethod
    def _free_port():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as probe:
            probe.bind(("127.0.0.1", 0))
            return probe.getsockname()[1]

    @staticmethod
    def _free_console_pair():
        candidates = list(range(RUNTIME_CONSOLE_FIRST_PORT, RUNTIME_CONSOLE_LAST_PORT + 1, RUNTIME_CONSOLE_PORT_STRIDE))
        random.shuffle(candidates)
        for port in candidates:
            first = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            second = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                first.bind(("127.0.0.1", port))
                second.bind(("127.0.0.1", port + 1))
                return port
            except OSError:
                continue
            finally:
                first.close()
                second.close()
        raise RuntimeError("安卓模拟器端口均被占用，稍后将自动重试")

    def _make_env(self):
        values = os.environ.copy()
        if os.name == "nt":
            values.pop("HOME", None)
        values.update({
            "ANDROID_HOME": str(self.sdk),
            "ANDROID_SDK_ROOT": str(self.sdk),
            "ANDROID_USER_HOME": str(self.user_home),
            "ANDROID_EMULATOR_HOME": str(self.user_home),
            "ANDROID_AVD_HOME": str(self.avd_home),
            "ANDROID_SDK_HOME": str(self.root),
            "ANDROID_ADB_SERVER_PORT": str(self.adb_port),
            "ANDROID_ADB_SERVER_ADDRESS": "127.0.0.1",
            "ADB_SERVER_SOCKET": "tcp:127.0.0.1:" + str(self.adb_port),
            "ADB_VENDOR_KEYS": str(self.user_home / "adbkey"),
            "ADB_MDNS_AUTO_CONNECT": "0",
            "ADB_LOCAL_TRANSPORT_MAX_PORT": "0",
            "ADBHOST": "127.0.0.1",
            "ADB_USB": "0",
            "ADB_EMU": "0",
            "ANDROID_ADB_LOG_PATH": str(self.logs / "adb-native.log"),
            "ANDROID_I_WANT_MY_TCG": "yes",
            "USERPROFILE": str(self.profile),
            "XDG_CACHE_HOME": str(self.root / "xdg-cache"),
            "XDG_CONFIG_HOME": str(self.root / "xdg-config"),
            "APPDATA": str(self.profile / "AppData" / "Roaming"),
            "LOCALAPPDATA": str(self.profile / "AppData" / "Local"),
            "TEMP": str(self.temp),
            "TMP": str(self.temp),
            "QT_QUICK_DISK_CACHE_PATH": str(self.root / "qt-cache"),
        })
        return values

    def _flags(self):
        if os.name != "nt":
            return 0
        return getattr(subprocess, "CREATE_NO_WINDOW", 0) | getattr(subprocess, "BELOW_NORMAL_PRIORITY_CLASS", 0)

    def _run(self, args, cancel=None, timeout=None, check=True):
        check_cancel(cancel)
        process = subprocess.Popen([str(item) for item in args], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.DEVNULL, env=self.env, cwd=str(self.root), creationflags=self._flags(), shell=False)
        operation = "process:" + pathlib.Path(str(args[0])).name
        started = time.monotonic()
        deadline = started + (self.measurements.timeout(operation, RUNTIME_BOOTSTRAP_COMMAND_TIMEOUT_SECONDS) if timeout is None else float(timeout))
        succeeded = False
        try:
            while True:
                check_cancel(cancel)
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    raise TimeoutError("安卓命令超时：" + str(args[0]))
                try:
                    output, error = process.communicate(timeout=min(RUNTIME_CANCEL_POLL_SECONDS, remaining))
                    break
                except subprocess.TimeoutExpired:
                    continue
            if check and process.returncode:
                message = (error or output).decode("utf-8", "replace").strip()
                raise RuntimeError(message[:RUNTIME_MAX_MESSAGE_CHARACTERS] or "安卓命令失败，退出码 " + str(process.returncode))
            succeeded = True
            return output, error, process.returncode
        finally:
            if cancel is None or not cancel.is_set():
                self.measurements.observe(operation, time.monotonic() - started, success=succeeded)
            if process.poll() is None:
                process.terminate()
                try:
                    process.wait(timeout=1.0)
                except subprocess.TimeoutExpired:
                    process.kill()
                    process.wait(timeout=RUNTIME_PROCESS_FORCE_STOP_SECONDS)

    def _adb_command(self, arguments, cancel=None, timeout=None, device=True, check=True):
        if self.adb_port is None or not self.adb.is_file():
            raise RuntimeError("安卓尚未启动")
        if self.adb_process is not None and self.adb_process.poll() is not None:
            raise RuntimeError("独立 ADB 服务已退出，正在等待恢复")
        args = [str(self.adb), "-H", "127.0.0.1", "-P", str(self.adb_port)]
        if device:
            if not self.serial:
                raise RuntimeError("安卓设备尚未连接")
            args.extend(["-s", self.serial])
        args.extend(arguments)
        while not self._adb_io_lock.acquire(timeout=RUNTIME_SOCKET_POLL_SECONDS):
            check_cancel(cancel)
        try:
            check_cancel(cancel)
            operation = "adb:" + str(arguments[0])
            selected_timeout = self.measurements.timeout(operation, RUNTIME_BOOTSTRAP_COMMAND_TIMEOUT_SECONDS)
            if timeout is not None:
                selected_timeout = max(RUNTIME_SOCKET_POLL_SECONDS, float(timeout))
            with self.measurements.measure(operation):
                return self._run(args, cancel=cancel, timeout=selected_timeout, check=check)
        finally:
            self._adb_io_lock.release()

    @staticmethod
    def _adb_read(connection, length, deadline, cancel=None):
        content = bytearray()
        while len(content) < length:
            check_cancel(cancel)
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise TimeoutError("ADB 数据通道响应超时")
            connection.settimeout(min(RUNTIME_SOCKET_POLL_SECONDS, remaining))
            try:
                block = connection.recv(min(RUNTIME_SOCKET_RECEIVE_BYTES, length - len(content)))
            except socket.timeout:
                continue
            if not block:
                raise ConnectionError("ADB 数据通道意外断开")
            content.extend(block)
        return bytes(content)

    def _adb_request(self, connection, service, deadline, cancel=None):
        check_cancel(cancel)
        payload = str(service).encode("utf-8")
        if not 0 < len(payload) <= RUNTIME_ADB_MAX_SERVICE_BYTES:
            raise ValueError("ADB 请求长度无效")
        self._adb_send_all(connection, format(len(payload), "0" + str(RUNTIME_ADB_LENGTH_DIGITS) + "x").encode("ascii") + payload, deadline, cancel)
        result = self._adb_read(connection, RUNTIME_ADB_LENGTH_DIGITS, deadline, cancel)
        if result == b"OKAY":
            return
        if result == b"FAIL":
            length = int(self._adb_read(connection, RUNTIME_ADB_LENGTH_DIGITS, deadline, cancel), RUNTIME_HEXADECIMAL_BASE)
            message = self._adb_read(connection, length, deadline, cancel).decode("utf-8", "replace")
            raise RuntimeError("ADB 拒绝请求：" + message[:RUNTIME_MAX_MESSAGE_CHARACTERS])
        raise RuntimeError("ADB 返回了无效的协议状态")

    def _open_adb_stream(self, service, cancel=None, timeout=None, device=True):
        check_cancel(cancel)
        if self._closed or self.adb_port is None or device and not self.serial:
            raise RuntimeError("安卓数据通道尚未就绪")
        if self.adb_process is not None and self.adb_process.poll() is not None:
            raise RuntimeError("独立 ADB 服务已退出")
        selected_timeout = RUNTIME_BOOTSTRAP_COMMAND_TIMEOUT_SECONDS if timeout is None else max(RUNTIME_SOCKET_POLL_SECONDS, float(timeout))
        deadline = time.monotonic() + selected_timeout
        with self.measurements.measure("adb_connect"):
            connection = socket.create_connection(("127.0.0.1", self.adb_port), timeout=min(selected_timeout, self.measurements.timeout("adb_connect", RUNTIME_BOOTSTRAP_CONNECT_TIMEOUT_SECONDS)))
        connection.settimeout(RUNTIME_SOCKET_POLL_SECONDS)
        connection.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        with self._adb_stream_lock:
            self._adb_streams.add(connection)
        try:
            check_cancel(cancel)
            if device:
                self._adb_request(connection, "host:transport:" + self.serial, deadline, cancel)
            self._adb_request(connection, service, deadline, cancel)
            return connection, deadline
        except BaseException:
            self._close_adb_stream(connection)
            raise

    def _close_adb_stream(self, connection):
        with self._adb_stream_lock:
            self._adb_streams.discard(connection)
        with contextlib.suppress(OSError):
            connection.shutdown(socket.SHUT_RDWR)
        with contextlib.suppress(OSError):
            connection.close()

    def _disconnect_adb_streams(self):
        with self._adb_stream_lock:
            connections = tuple(self._adb_streams)
            self._adb_streams.clear()
        for connection in connections:
            self._close_adb_stream(connection)

    def _adb_host(self, service, cancel=None, timeout=RUNTIME_BOOTSTRAP_HOST_TIMEOUT_SECONDS):
        connection, deadline = self._open_adb_stream(service, cancel, timeout, device=False)
        try:
            length = int(self._adb_read(connection, RUNTIME_ADB_LENGTH_DIGITS, deadline, cancel), RUNTIME_HEXADECIMAL_BASE)
            return self._adb_read(connection, length, deadline, cancel)
        finally:
            self._close_adb_stream(connection)

    def _notify_owned_emulator(self, cancel=None):
        check_cancel(cancel)
        if not self.console_port or self.adb_port is None or self.process is None or self.process.poll() is not None:
            return
        payload = ("host:emulator:" + str(self.console_port + 1)).encode("ascii")
        with socket.create_connection(("127.0.0.1", self.adb_port), timeout=RUNTIME_SOCKET_POLL_SECONDS) as connection:
            connection.sendall(format(len(payload), "0" + str(RUNTIME_ADB_LENGTH_DIGITS) + "x").encode("ascii") + payload)

    def _adb_exec(self, arguments, cancel=None, timeout=None, max_bytes=None):
        command = " ".join(shlex.quote(str(item)) for item in arguments)
        operation = "exec:" + str(arguments[0])
        selected_timeout = self.measurements.timeout(operation, RUNTIME_BOOTSTRAP_SCREENSHOT_TIMEOUT_SECONDS)
        if timeout is not None:
            selected_timeout = max(RUNTIME_SOCKET_POLL_SECONDS, float(timeout))
        connection, deadline = self._open_adb_stream("exec:" + command, cancel, selected_timeout)
        if max_bytes is None:
            max_bytes = max(RUNTIME_ADB_INITIAL_OUTPUT_BYTES, self.width * self.height * ctypes.sizeof(ctypes.c_uint32) + RUNTIME_BYTES_PER_MIB)
        started = time.monotonic()
        succeeded = False
        content = bytearray()
        try:
            while True:
                check_cancel(cancel)
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    raise TimeoutError("ADB 输出通道响应超时")
                connection.settimeout(min(RUNTIME_SOCKET_POLL_SECONDS, remaining))
                try:
                    block = connection.recv(RUNTIME_SOCKET_RECEIVE_BYTES)
                except socket.timeout:
                    continue
                if not block:
                    succeeded = True
                    return bytes(content)
                content.extend(block)
                if len(content) > max_bytes:
                    raise RuntimeError("ADB 输出超过本次请求容量")
        finally:
            self._close_adb_stream(connection)
            if cancel is None or not cancel.is_set():
                self.measurements.observe(operation, time.monotonic() - started, success=succeeded, units=len(content) if succeeded else None)

    def _shell(self, arguments, cancel=None, timeout=None, check=True):
        command = " ".join(shlex.quote(str(item)) for item in arguments)
        operation = "shell:" + str(arguments[0])
        selected_timeout = self.measurements.timeout(operation, RUNTIME_BOOTSTRAP_SHELL_TIMEOUT_SECONDS)
        if timeout is not None:
            selected_timeout = max(RUNTIME_SOCKET_POLL_SECONDS, float(timeout))
        connection, deadline = self._open_adb_stream("shell,v2,raw:" + command, cancel, selected_timeout)
        output, error = bytearray(), bytearray()
        started = time.monotonic()
        succeeded = False
        try:
            self._adb_send_all(connection, RUNTIME_ADB_SHELL_HEADER.pack(RUNTIME_ADB_SHELL_CLOSE_STDIN, 0), deadline, cancel)
            while True:
                channel, length = RUNTIME_ADB_SHELL_HEADER.unpack(self._adb_read(connection, RUNTIME_ADB_SHELL_HEADER.size, deadline, cancel))
                if channel not in (RUNTIME_ADB_SHELL_STDOUT, RUNTIME_ADB_SHELL_STDERR, RUNTIME_ADB_SHELL_EXIT) or length > RUNTIME_ADB_INITIAL_PACKET_BYTES or len(output) + len(error) + length > RUNTIME_ADB_INITIAL_OUTPUT_BYTES:
                    raise RuntimeError("ADB shell 数据包无效")
                block = self._adb_read(connection, length, deadline, cancel)
                if channel == RUNTIME_ADB_SHELL_EXIT:
                    if length != 1:
                        raise RuntimeError("ADB shell 退出码无效")
                    code = block[0]
                    if check and code:
                        raise RuntimeError((error or output).decode("utf-8", "replace")[:RUNTIME_MAX_MESSAGE_CHARACTERS] or "安卓命令失败，退出码 " + str(code))
                    succeeded = True
                    return bytes(output), bytes(error), code
                (output if channel == RUNTIME_ADB_SHELL_STDOUT else error).extend(block)
        finally:
            self._close_adb_stream(connection)
            if cancel is None or not cancel.is_set():
                self.measurements.observe(operation, time.monotonic() - started, success=succeeded)

    def _open_log(self, name):
        path = self.logs / name
        if path.is_file() and path.stat().st_size > RUNTIME_LOG_MIB * RUNTIME_BYTES_PER_KIB * RUNTIME_BYTES_PER_KIB:
            previous = path.with_suffix(path.suffix + ".previous")
            try:
                os.replace(path, previous)
            except OSError:
                pass
        handle = path.open("ab", buffering=0)
        return handle

    def _start_adb(self, cancel):
        check_cancel(cancel)
        if self.adb_process is not None and self.adb_process.poll() is None:
            return
        if self._adb_job is not None:
            self._adb_job.close()
            self._adb_job = None
        if self.adb_port is None:
            self.adb_port = self._free_port()
        self.env = self._make_env()
        handle = self._open_log("adb.log")
        log_offset = handle.tell()
        args = [str(self.adb), "-L", "tcp:127.0.0.1:" + str(self.adb_port), "server", "nodaemon"]
        self.log("android_adb_starting", endpoint="tcp:127.0.0.1:" + str(self.adb_port))
        try:
            self.adb_process = subprocess.Popen(args, stdin=subprocess.DEVNULL, stdout=handle, stderr=handle, cwd=str(self.root), env=self.env, creationflags=self._flags(), shell=False)
        finally:
            handle.close()
        try:
            try:
                self._adb_job = _AndroidProcessJob(self.adb_process)
            except Exception as exc:
                self.log("android_process_job_error", process="adb", error=str(exc))
            started = time.monotonic()
            deadline = started + self.measurements.timeout("adb_start", RUNTIME_BOOTSTRAP_ADB_START_SECONDS)
            while time.monotonic() < deadline:
                check_cancel(cancel)
                code = self.adb_process.poll()
                if code is not None:
                    detail = self._adb_launch_log(log_offset)
                    self.log("android_adb_start_failed", exit_code=code, detail=detail)
                    raise RuntimeError("独立 ADB 服务启动失败（退出码 " + str(code) + "）：" + (detail or "请检查 adb.log"))
                try:
                    version = self._adb_host("host:version", cancel, timeout=RUNTIME_BOOTSTRAP_CONSOLE_TIMEOUT_SECONDS)
                    if re.fullmatch(b"[0-9a-fA-F]{4,8}", version):
                        self._notify_owned_emulator(cancel)
                        self.measurements.observe("adb_start", time.monotonic() - started)
                        self.log("android_adb_started", port=self.adb_port)
                        return
                    self.log("android_adb_probe_error", detail=version.decode("utf-8", "replace")[:RUNTIME_MAX_MESSAGE_CHARACTERS])
                except Cancelled:
                    raise
                except (OSError, TimeoutError, RuntimeError):
                    pass
                self._wait(cancel, self.measurements.estimate("adb_connect", RUNTIME_SOCKET_POLL_SECONDS))
            self.measurements.observe("adb_start", time.monotonic() - started, success=False)
            detail = self._adb_launch_log(log_offset)
            self.log("android_adb_start_timeout", detail=detail)
            raise TimeoutError("独立 ADB 服务启动超时：" + (detail or "ADB 未能响应 devices 命令"))
        except BaseException:
            self._kill_owned(self.adb_process)
            if self._adb_job is not None:
                self._adb_job.close()
                self._adb_job = None
            self.adb_process = None
            raise

    def _restart_adb(self, cancel):
        check_cancel(cancel)
        if self._external:
            self._disconnect_adb_streams()
            self.booted = False
            self._prepared = False
            self.prepare(cancel)
            return
        self._disconnect_adb_streams()
        self._last_health = 0.0
        self._adb_restarts += 1
        self.log("android_adb_restart", port=self.adb_port, serial=self.serial, attempts=self._adb_restarts)
        process, job = self.adb_process, self._adb_job
        self._kill_owned(process)
        if job is not None:
            job.close()
        if self.adb_process is process:
            self.adb_process = None
        if self._adb_job is job:
            self._adb_job = None
        self._start_adb(cancel)

    def _adb_launch_log(self, offset):
        try:
            with (self.logs / "adb.log").open("rb") as stream:
                stream.seek(max(0, int(offset)))
                detail = stream.read(RUNTIME_DIAGNOSTIC_TAIL_BYTES).decode("utf-8", "replace").strip().splitlines()
            return "；".join(line.strip()[-RUNTIME_MAX_MESSAGE_CHARACTERS:] for line in detail[-RUNTIME_ADB_LOG_PREVIEW_LINES:])[-RUNTIME_MAX_MESSAGE_CHARACTERS:]
        except OSError:
            return ""

    @staticmethod
    def _wait(cancel, seconds):
        seconds = float(seconds)
        if not math.isfinite(seconds) or seconds < 0:
            raise ValueError("等待时长必须是非负有限数")
        deadline = time.monotonic() + seconds
        if not math.isfinite(deadline):
            raise ValueError("等待截止时间无法表示")
        while True:
            check_cancel(cancel)
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                return
            interval = min(RUNTIME_CANCEL_POLL_SECONDS, remaining)
            if cancel is None:
                time.sleep(interval)
            elif cancel.wait(interval):
                check_cancel(cancel)

    def _choose_acceleration(self, cancel):
        if self.acceleration is not None:
            return
        try:
            output, error, code = self._run([self.emulator, "-accel-check"], cancel=cancel, timeout=RUNTIME_BOOTSTRAP_GPU_PROBE_SECONDS, check=False)
            text = (output + error).decode("utf-8", "replace")
            self.acceleration = "on" if code == 0 else "off"
            self.log("android_acceleration", mode=self.acceleration, detail=text[:RUNTIME_MAX_MESSAGE_CHARACTERS])
        except Cancelled:
            raise
        except Exception as exc:
            self.acceleration = "off"
            self.log("android_acceleration", mode="off", error=str(exc))
        if self.acceleration == "off":
            self.status("没有可用的虚拟化加速，正在尝试软件模拟；启动可能很慢")

    def _next_graphics_backend(self, reason):
        previous = self.gpu_mode
        self.gpu_mode = {"host": "auto", "auto": "software", "software": "host"}.get(previous, "host")
        with contextlib.suppress(OSError, ValueError):
            atomic_json(safe_workspace_file(self.base, self._graphics_profile_path), {"verified": False, "identity": self._graphics_identity_value, "failed_mode": previous})
        self._graphics_identity_value = self._graphics_identity()
        if previous != self.gpu_mode:
            self.log("android_graphics_fallback", previous=previous, selected=self.gpu_mode, reason=str(reason)[:RUNTIME_MAX_MESSAGE_CHARACTERS])

    @staticmethod
    def _graphics_adapters():
        if os.name != "nt":
            return []
        import winreg
        raw_guid = uuid.UUID(RUNTIME_WIN32_DISPLAY_CLASS).bytes_le
        guid_type = ctypes.c_ubyte * len(raw_guid)
        guid = guid_type.from_buffer_copy(raw_guid)
        class DeviceInfo(ctypes.Structure):
            _fields_ = [("size", ctypes.c_uint32), ("class_guid", guid_type), ("instance", ctypes.c_uint32), ("reserved", ctypes.c_size_t)]
        setup = ctypes.WinDLL("setupapi", use_last_error=True)
        setup.SetupDiGetClassDevsW.argtypes = [ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_void_p, ctypes.c_uint32]
        setup.SetupDiGetClassDevsW.restype = ctypes.c_void_p
        setup.SetupDiEnumDeviceInfo.argtypes = [ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(DeviceInfo)]
        setup.SetupDiEnumDeviceInfo.restype = ctypes.c_int
        setup.SetupDiGetDeviceInstanceIdW.argtypes = [ctypes.c_void_p, ctypes.POINTER(DeviceInfo), ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32)]
        setup.SetupDiGetDeviceInstanceIdW.restype = ctypes.c_int
        setup.SetupDiOpenDevRegKey.argtypes = [ctypes.c_void_p, ctypes.POINTER(DeviceInfo), ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32]
        setup.SetupDiOpenDevRegKey.restype = ctypes.c_void_p
        setup.SetupDiDestroyDeviceInfoList.argtypes = [ctypes.c_void_p]
        setup.SetupDiDestroyDeviceInfoList.restype = ctypes.c_int
        devices = setup.SetupDiGetClassDevsW(ctypes.byref(guid), None, None, RUNTIME_WIN32_DEVICE_PRESENT)
        if devices in (None, ctypes.c_void_p(-1).value):
            raise ctypes.WinError(ctypes.get_last_error())
        result = []
        try:
            index = 0
            while True:
                device = DeviceInfo()
                device.size = ctypes.sizeof(device)
                if not setup.SetupDiEnumDeviceInfo(devices, index, ctypes.byref(device)):
                    error = ctypes.get_last_error()
                    if error != RUNTIME_WIN32_ERROR_NO_MORE_ITEMS:
                        raise ctypes.WinError(error)
                    break
                index += 1
                required = ctypes.c_uint32()
                setup.SetupDiGetDeviceInstanceIdW(devices, ctypes.byref(device), None, 0, ctypes.byref(required))
                if not required.value:
                    raise ctypes.WinError(ctypes.get_last_error())
                identity = ctypes.create_unicode_buffer(required.value)
                if not setup.SetupDiGetDeviceInstanceIdW(devices, ctypes.byref(device), identity, len(identity), ctypes.byref(required)):
                    raise ctypes.WinError(ctypes.get_last_error())
                handle = setup.SetupDiOpenDevRegKey(devices, ctypes.byref(device), RUNTIME_WIN32_DEVICE_SCOPE_GLOBAL, 0, RUNTIME_WIN32_DEVICE_DRIVER_KEY, winreg.KEY_READ)
                if handle in (None, ctypes.c_void_p(-1).value):
                    raise ctypes.WinError(ctypes.get_last_error())
                with winreg.HKEYType(handle) as key:
                    version = str(winreg.QueryValueEx(key, "DriverVersion")[0])
                    if not version:
                        raise OSError("显示驱动版本不可识别")
                    result.append({"device": identity.value, "driver": version})
            return sorted(result, key=lambda value: value["device"])
        finally:
            setup.SetupDiDestroyDeviceInfoList(devices)

    def _graphics_identity(self):
        try:
            adapters = self._graphics_adapters()
            if not adapters:
                return ""
            files = {}
            for path in (self.emulator, self.emulator.parent / "source.properties", self.image / "source.properties"):
                if path == self.emulator or path.is_file():
                    information = path.stat()
                    files[str(path.resolve())] = {"size": information.st_size, "modified_ns": information.st_mtime_ns}
            value = {"adapters": adapters, "components": files, "system": platform.version(), "architecture": platform.machine(), "image": self.IMAGE_PACKAGE}
            return hashlib.sha256(json.dumps(value, sort_keys=True).encode("utf-8")).hexdigest()
        except (OSError, AttributeError, ValueError, ImportError) as exc:
            self.log("graphics_identity_unavailable", error=str(exc))
            return ""

    def _load_graphics_profile(self):
        self.gpu_mode = "host"
        self._graphics_identity_value = self._graphics_identity()
        record = read_json(self._graphics_profile_path, {})
        if self._graphics_identity_value and isinstance(record, dict) and record.get("verified") is True and record.get("identity") == self._graphics_identity_value and record.get("mode") in {"host", "auto", "software"}:
            self.gpu_mode = record["mode"]
            self.log("graphics_profile_reused", mode=self.gpu_mode)

    def _save_graphics_profile(self):
        if not self.owned or not self.booted or not self._graphics_identity_value:
            return
        try:
            atomic_json(safe_workspace_file(self.base, self._graphics_profile_path), {"verified": True, "identity": self._graphics_identity_value, "mode": self.gpu_mode})
        except Exception as exc:
            self.log("graphics_profile_save_failed", error=str(exc))

    def _boot_fingerprint(self):
        components = {}
        for name, path in self._critical_files().items():
            info = path.stat()
            components[name] = {"path": str(path), "size": info.st_size, "modified_ns": info.st_mtime_ns}
        configuration = {"image": self.IMAGE_PACKAGE, "components": components, "memory_mb": self.memory_mb, "cores": self.cores, "gpu": self.gpu_mode, "acceleration": self.acceleration, "config": hashlib.sha256((self.avd / "config.ini").read_bytes()).hexdigest()}
        return hashlib.sha256(json.dumps(configuration, sort_keys=True).encode("utf-8")).hexdigest()

    def _launch(self, cancel):
        check_cancel(cancel)
        if self._closed:
            raise Cancelled("安卓运行环境正在关闭")
        available = available_memory_mb()
        spare = max(RUNTIME_IMAGE_RESOURCE_RESERVE_MB, math.ceil(self.memory_mb / RUNTIME_ANDROID_HEAP_MEMORY_DIVISOR))
        if not self._minimum_memory_mb() <= self.memory_mb <= RUNTIME_EMULATOR_MAX_MEMORY_MB:
            raise ComponentFailure("resources", "模拟器内存预算不满足当前系统镜像的官方运行范围")
        if available < self.memory_mb + spare:
            raise ComponentFailure("resources", "可用内存不足以启动安卓模拟器，并同时为 Windows 保留空间")
        required_disk = max(RUNTIME_ANDROID_MIN_FREE_DISK_BYTES, self.memory_mb * RUNTIME_BYTES_PER_MIB + runtime_disk_reserve(self.root))
        if shutil.disk_usage(self.root).free < required_disk:
            raise ComponentFailure("resources", "安卓模拟器启动所需磁盘空间不足，正在等待存储资源并自动重试")
        if self._emulator_job is not None:
            self._emulator_job.close()
            self._emulator_job = None
        if self.adb_process is None or self.adb_process.poll() is not None:
            self.adb_port = None
        self._start_adb(cancel)
        self._choose_acceleration(cancel)
        self._configure_avd()
        previous_boot = read_json(self.avd / "gameai-boot.json", {})
        self._snapshot_signature = self._boot_fingerprint()
        self._snapshot_enabled = self.acceleration == "on" and self.gpu_mode in ("host", "auto")
        snapshot = self.avd / "snapshots" / "default_boot" / "snapshot.pb"
        clean_snapshot = bool(isinstance(previous_boot, dict) and previous_boot.get("clean_snapshot") is True and previous_boot.get("running") is False and previous_boot.get("signature") == self._snapshot_signature and snapshot.is_file() and not path_is_link(snapshot))
        quick_boot = self._snapshot_enabled and clean_snapshot and not self._force_cold_boot
        self._boot_mode = "quick" if quick_boot else "cold"
        self.console_port = self._free_console_pair()
        self.serial = "emulator-" + str(self.console_port)
        self.booted = False
        self.env = self._make_env()
        self._disconnect_console()
        self._touches.clear()
        self._input_layout = None
        self._geometry_dirty = True
        args = [str(self.emulator), "-avd", self.avd_name, "-no-window", "-no-boot-anim", "-screen", "multi-touch", "-port", str(self.console_port), "-memory", str(self.memory_mb), "-cores", str(self.cores), "-gpu", self.gpu_mode, "-accel", self.acceleration]
        if not self._snapshot_enabled:
            args.append("-no-snapshot")
        elif not quick_boot:
            args.append("-no-snapshot-load")
        self._launch_wall_ns = time.time_ns()
        self._launched_avd = self.avd
        atomic_json(self.avd / "gameai-boot.json", {"running": True, "clean_snapshot": False, "signature": self._snapshot_signature, "started_ns": self._launch_wall_ns, "boot_mode": self._boot_mode})
        check_cancel(cancel)
        if self._closed:
            raise Cancelled("安卓运行环境正在关闭")
        handle = self._open_log("emulator.log")
        try:
            self.process = subprocess.Popen(args, stdin=subprocess.DEVNULL, stdout=handle, stderr=handle, cwd=str(self.sdk), env=self.env, creationflags=self._flags(), shell=False)
        finally:
            handle.close()
        try:
            self._emulator_job = _AndroidProcessJob(self.process)
        except Exception as exc:
            self.log("android_process_job_error", process="emulator", error=str(exc))
        self.log("android_start", pid=self.process.pid, port=self.console_port, adb_port=self.adb_port, acceleration=self.acceleration, gpu=self.gpu_mode, memory_mb=self.memory_mb, cores=self.cores, boot_mode=self._boot_mode)
        self.status("正在恢复安卓快速启动快照" if quick_boot else "安卓正在启动" if self.acceleration == "on" else "安卓正在软件模拟模式下启动，请等待")

    def _wait_for_device(self, cancel, seconds=None):
        started = time.monotonic()
        operation = "discovery:" + str(self.acceleration)
        deadline = started + self.measurements.timeout(operation, RUNTIME_BOOTSTRAP_DISCOVERY_SECONDS if seconds is None else seconds)
        last_status = None
        failures = 0
        restarted = False
        last_registered = 0.0
        while time.monotonic() < deadline:
            check_cancel(cancel)
            if self._closed:
                raise Cancelled("安卓运行环境正在关闭")
            if self.process is None or self.process.poll() is not None:
                raise RuntimeError("安卓进程在设备连接前退出")
            state = None
            try:
                if time.monotonic() - last_registered >= self.measurements.timeout("adb_connect", RUNTIME_BOOTSTRAP_DEVICE_REGISTRATION_SECONDS):
                    self._notify_owned_emulator(cancel)
                    last_registered = time.monotonic()
                output = self._adb_host("host:devices-l", cancel, timeout=RUNTIME_BOOTSTRAP_HOST_TIMEOUT_SECONDS)
                failures = 0
                entries = output.decode("utf-8", "replace").splitlines()
                states = {parts[0]: parts[1] for line in entries if len(parts := line.split()) >= 2 and parts[0].startswith("emulator-")}
                state = states.get(self.serial)
            except Cancelled:
                raise
            except (OSError, RuntimeError, TimeoutError) as exc:
                failures += 1
                self.log("android_adb_connect_error", failures=failures, error=str(exc))
                if failures >= RUNTIME_STARTUP_ERROR_CONFIRMATIONS:
                    if restarted:
                        raise ComponentFailure("android", "ADB 独立服务重启后仍连续无法连接") from exc
                    self._restart_adb(cancel)
                    restarted = True
                    failures = 0
            if state == "device":
                self.measurements.observe(operation, time.monotonic() - started)
                self.log("android_adb_connected", serial=self.serial, server_port=self.adb_port)
                return
            if state != last_status:
                last_status = state
                self.log("android_adb_wait", serial=self.serial, state=state or "not_found")
            self._wait(cancel, self.measurements.estimate("adb_connect", RUNTIME_SOCKET_POLL_SECONDS))
        self.measurements.observe(operation, time.monotonic() - started, success=False)
        raise TimeoutError("ADB 无法发现模拟器：" + str(self.serial))

    def ensure_running(self, cancel=None):
        check_cancel(cancel)
        if self._closed:
            raise RuntimeError("安卓运行环境已关闭")
        if not self._prepared:
            self.prepare(cancel)
        if self._external:
            try:
                if self.booted and time.monotonic() - self._last_health < RUNTIME_HEALTH_SUCCESS_CACHE_SECONDS:
                    return
                output, error, code = self._shell(["getprop", "sys.boot_completed"], cancel=cancel, timeout=RUNTIME_ADB_HEALTH_TIMEOUT_SECONDS, check=False)
                if code or output.strip() != b"1":
                    raise RuntimeError("已选本地模拟器尚未完成启动")
                if not self.booted:
                    self._boot_setup(cancel)
                self.booted = True
                self._last_health = time.monotonic()
                self.status("本地模拟器已连接 · " + str(self.serial))
                return
            except BaseException:
                self.booted = False
                self._prepared = False
                raise
        if self.adb_process is not None and self.adb_process.poll() is not None:
            self._restart_adb(cancel)
            if self.process is not None and self.process.poll() is None:
                self._wait_for_device(cancel, seconds=RUNTIME_BOOTSTRAP_DISCOVERY_SECONDS)
        if self.process is not None and self.process.poll() is None and self.booted:
            if time.monotonic() - self._last_health < RUNTIME_HEALTH_SUCCESS_CACHE_SECONDS:
                return
            for attempt in range(RUNTIME_ADB_RECOVERY_CONFIRMATIONS):
                try:
                    output, _, code = self._shell(["getprop", "sys.boot_completed"], cancel=cancel, timeout=RUNTIME_ADB_HEALTH_TIMEOUT_SECONDS, check=False)
                    if code == 0 and output.strip() == b"1":
                        self._last_health = time.monotonic()
                        return
                except Cancelled:
                    raise
                except Exception as exc:
                    self.log("android_adb_health_failure", attempt=attempt + 1, error=str(exc))
                if attempt == 0:
                    self._restart_adb(cancel)
            self.booted = False
        if self.process is None or self.process.poll() is not None:
            if self.process is not None:
                self._failures += 1
                if self._boot_mode == "quick":
                    self._force_cold_boot = True
                else:
                    self._next_graphics_backend("模拟器退出：" + str(self.process.returncode))
                self.log("android_exit", code=self.process.returncode, retry=self._failures)
            self._launch(cancel)
            try:
                self._wait_for_device(cancel, seconds=RUNTIME_BOOTSTRAP_SOFTWARE_DISCOVERY_SECONDS if self.acceleration == "off" else RUNTIME_BOOTSTRAP_DISCOVERY_SECONDS)
            except Cancelled:
                raise
            except Exception as exc:
                if self._boot_mode == "quick":
                    self._force_cold_boot = True
                    self._stop_emulator()
                    self.log("android_snapshot_fallback", error=str(exc))
                else:
                    self._next_graphics_backend(exc)
                raise
        boot_operation = "boot:" + str(self.acceleration) + ":" + self._boot_mode
        boot_started = time.monotonic()
        deadline = boot_started + self.measurements.timeout(boot_operation, RUNTIME_BOOTSTRAP_SOFTWARE_BOOT_SECONDS if self.acceleration == "off" else RUNTIME_BOOTSTRAP_COLD_BOOT_SECONDS)
        last_status = 0.0
        adb_failures = 0
        restarted = False
        while time.monotonic() < deadline:
            check_cancel(cancel)
            if self._closed:
                raise Cancelled("安卓运行环境正在关闭")
            if self.process.poll() is not None:
                tail = self._log_tail("emulator.log", RUNTIME_DIAGNOSTIC_TAIL_BYTES)
                if any(any(word in line for word in ("whpx", "hypervisor", "acceleration", "haxm")) and any(word in line for word in ("error", "failed", "not usable", "not supported", "not installed", "unavailable")) for line in tail.lower().splitlines()):
                    self.acceleration = "off"
                if self._boot_mode == "quick":
                    self._force_cold_boot = True
                else:
                    self._next_graphics_backend("安卓启动中退出")
                raise RuntimeError("安卓进程退出：" + tail[-RUNTIME_MAX_MESSAGE_CHARACTERS:])
            try:
                output, error, code = self._shell(["getprop", "sys.boot_completed"], cancel=cancel, timeout=RUNTIME_ADB_HEALTH_TIMEOUT_SECONDS, check=False)
                if code:
                    raise RuntimeError((output + error).decode("utf-8", "replace")[-RUNTIME_MAX_MESSAGE_CHARACTERS:] or "ADB getprop 失败")
                adb_failures = 0
                if output.strip() == b"1":
                    self._boot_setup(cancel)
                    self.booted = True
                    self.measurements.observe(boot_operation, time.monotonic() - boot_started)
                    with contextlib.suppress(OSError):
                        self.measurements.save()
                    self._force_cold_boot = False
                    self._last_health = time.monotonic()
                    graphics_log = self._log_tail("emulator.log", RUNTIME_GPU_LOG_BYTES)
                    graphics_lines = [line.strip()[:RUNTIME_MAX_MESSAGE_CHARACTERS] for line in graphics_log.splitlines() if any(word in line.lower() for word in ("renderer", "swiftshader", "llvmpipe", "vulkan", "opengl"))]
                    self.log("android_graphics_ready", requested=self.gpu_mode, evidence=graphics_lines, boot_mode=self._boot_mode)
                    self.status("安卓已启动")
                    return
            except Cancelled:
                raise
            except (OSError, RuntimeError, TimeoutError) as exc:
                adb_failures += 1
                if time.monotonic() - last_status > RUNTIME_BOOT_STATUS_SECONDS:
                    self.log("android_boot_wait", detail=str(exc), adb_failures=adb_failures)
                if adb_failures >= RUNTIME_STARTUP_ERROR_CONFIRMATIONS:
                    if restarted:
                        raise ComponentFailure("android", "ADB 连续超时，重启服务后仍不可用") from exc
                    self.status("ADB 失去响应，正在重启独立连接服务")
                    self._restart_adb(cancel)
                    restarted = True
                    adb_failures = 0
            if time.monotonic() - last_status > RUNTIME_BOOT_STATUS_SECONDS:
                last_status = time.monotonic()
                self.status("正在等待安卓完成启动" if self.acceleration == "on" else "软件模拟仍在启动，AI 将自动继续重试")
            self._wait(cancel, self.measurements.estimate("shell:getprop", RUNTIME_STATUS_REFRESH_SECONDS))
        self.measurements.observe(boot_operation, time.monotonic() - boot_started, success=False)
        self._stop_emulator()
        if self._boot_mode == "quick":
            self._force_cold_boot = True
            self.log("android_snapshot_fallback", error="安卓启动超时")
        else:
            self._next_graphics_backend("安卓启动超时")
        raise TimeoutError("安卓启动超时，将自动重新尝试")

    def _boot_setup(self, cancel):
        self._input_verified = False
        probes = (("size", "wm size"), ("keyboard", "ime list -s"), ("abis", "getprop ro.product.cpu.abilist"), ("native_bridge", "getprop ro.dalvik.vm.native.bridge"), ("api", "getprop ro.build.version.sdk"), ("longpress", "settings get secure long_press_timeout"), ("inputhelp", "input"))
        command = "; ".join("printf '\\n__GAMEAI_" + key + "__\\n'; " + probe for key, probe in probes)
        output, error, _ = self._shell(["sh", "-c", command], cancel=cancel, timeout=RUNTIME_BOOTSTRAP_COMMAND_TIMEOUT_SECONDS, check=False)
        text = output.decode("utf-8", "replace")
        sections = dict(re.findall(r"(?:^|\n)__GAMEAI_(\w+)__\r?\n(.*?)(?=\n__GAMEAI_\w+__\r?\n|\Z)", text, flags=re.S))
        sizes = re.findall(r"(\d+)x(\d+)", sections.get("size", ""))
        if sizes:
            self.width, self.height = map(int, sizes[-1])
        self._existing_unicode_ime = "com.android.adbkeyboard/.AdbIME" in sections.get("keyboard", "")
        input_help = sections.get("inputhelp", "") + "\n" + error.decode("utf-8", "replace")
        self._input_commands = set(re.findall(r"(?m)^\s*(tap|swipe|keyevent|text|motionevent)\b", input_help.lower()))
        self._motion_event = "motionevent" in self._input_commands
        self.abis = [value.strip() for value in sections.get("abis", "").strip().split(",") if value.strip()]
        self.native_bridge = sections.get("native_bridge", "").strip()
        api = sections.get("api", "").strip()
        if not api.isdecimal():
            raise RuntimeError("已连接安卓设备没有返回有效 API 版本")
        self.device_api_level = int(api)
        if self._external:
            self.IMAGE_PACKAGE = "system-images;android-" + str(self.device_api_level) + ";external;" + (self.abis[0] if self.abis else "unknown")
        longpress = sections.get("longpress", "").strip()
        if longpress.isdecimal() and int(longpress) > 0:
            self._long_press_ms = int(longpress)
        if self.owned:
            self._shell(["input", "keyevent", "KEYCODE_WAKEUP"], cancel=cancel, check=False)
            result, _, _ = self._shell(["getevent", "-lp"], cancel=cancel, timeout=RUNTIME_BOOTSTRAP_COMMAND_TIMEOUT_SECONDS, check=False)
            self._input_layout = self._parse_input_layout(result.decode("utf-8", "replace"))
        if not self.owned or self._input_layout is None:
            self._input_backend = "adb_motionevent" if self._motion_event else "adb_gesture"
            self._input_layout = {"slot_min": 0, "slot_max": 0, "device": "android_input", "name": self._input_backend}
        else:
            self._input_backend = "emulator_console"
            try:
                self._read_display_geometry(cancel)
            except Cancelled:
                raise
            except (OSError, RuntimeError, TimeoutError, ValueError) as exc:
                self.log("android_geometry_unavailable", error=str(exc), fallback="android_input")
                self._input_backend = "adb_motionevent" if self._motion_event else "adb_gesture"
                self._input_layout = {"slot_min": 0, "slot_max": 0, "device": "android_input", "name": self._input_backend}
        display, _, _ = self._shell(["dumpsys", "display"], cancel=cancel, check=False)
        rates = [float(value) for value in re.findall(r"(?:refreshRate|renderFrameRate|fps)\s*[=: ]\s*(\d+(?:\.\d+)?)", display.decode("utf-8", "replace"))]
        rates = [value for value in rates if math.isfinite(value) and value > 0]
        if rates:
            self._refresh_hz = max(rates)
        try:
            self.release_touches(cancel)
        except Cancelled:
            raise
        except (OSError, RuntimeError, TimeoutError, ValueError) as exc:
            if self._input_backend != "emulator_console":
                raise
            self.log("emulator_console_unavailable", error=str(exc), fallback="android_input")
            self._disconnect_console()
            self._touches.clear()
            self._input_backend = "adb_motionevent" if self._motion_event else "adb_gesture"
            self._input_layout = {"slot_min": 0, "slot_max": 0, "device": "android_input", "name": self._input_backend}
            self.release_touches(cancel)
        if self._input_backend == "emulator_console" and (self._geometry_thread is None or not self._geometry_thread.is_alive()):
            self._geometry_thread = threading.Thread(target=self._geometry_loop, daemon=True, name="AndroidDisplayGeometry")
            self._geometry_thread.start()
        self.log("android_ready", width=self.width, height=self.height, abis=self.abis, native_bridge=self.native_bridge, input_backend=self._input_backend, image_package=self.IMAGE_PACKAGE, owned=self.owned)

    def screenshot(self, cancel=None):
        with self._capture_lock:
            output = self._adb_exec(["screencap", "-p"], cancel=cancel)
            prefix = len(RUNTIME_PNG_SIGNATURE)
            dimensions_at = prefix + RUNTIME_PNG_CHUNK_PREFIX.size
            if len(output) < dimensions_at + RUNTIME_PNG_DIMENSIONS.size or not output.startswith(RUNTIME_PNG_SIGNATURE):
                raise RuntimeError("安卓未返回有效截图")
            _, kind = RUNTIME_PNG_CHUNK_PREFIX.unpack_from(output, prefix)
            if kind != b"IHDR":
                raise RuntimeError("安卓截图缺少尺寸信息")
            width, height = RUNTIME_PNG_DIMENSIONS.unpack_from(output, dimensions_at)
            pixel_bytes = width * height * ctypes.sizeof(ctypes.c_uint32)
            if width <= 0 or height <= 0 or pixel_bytes > available_memory_mb() * RUNTIME_BYTES_PER_MIB:
                raise RuntimeError("安卓截图尺寸超出当前内存可处理范围")
            with self._geometry_lock:
                if (self.width, self.height) != (width, height):
                    self._geometry_dirty = True
                self.width, self.height = width, height
            return output

    def hierarchy(self, cancel=None, timeout=None, fresh=False):
        check_cancel(cancel)
        if not fresh and time.monotonic() < self._next_hierarchy:
            return self._hierarchy_cache
        if fresh:
            self._acquire_lock(self._hierarchy_lock, cancel)
        elif not self._hierarchy_lock.acquire(blocking=False):
            return self._hierarchy_cache
        started = time.monotonic()
        try:
            target = "/data/local/tmp/gameagent_window_" + str(os.getpid()) + ".xml"
            self._shell(["rm", "-f", target], cancel=cancel)
            capture_started = time.monotonic()
            self._shell(["uiautomator", "dump", "--compressed", target], cancel=cancel, timeout=self.measurements.timeout("hierarchy", RUNTIME_BOOTSTRAP_HIERARCHY_SECONDS if timeout is None else timeout))
            output = self._adb_exec(["cat", target], cancel=cancel, max_bytes=min(RUNTIME_ADB_INITIAL_OUTPUT_BYTES, available_memory_mb() * RUNTIME_BYTES_PER_MIB))
            text = output.decode("utf-8", "replace")
            start = text.find("<?xml")
            if start < 0:
                start = text.find("<hierarchy")
            if start < 0:
                raise ValueError("无界面树")
            text = text[start:]
            root = ET.fromstring(text)
            if self._tag(root) != "hierarchy":
                raise ValueError("界面树根节点无效")
            self._hierarchy_cache = text
            self.hierarchy_started_at = capture_started
            self.hierarchy_finished_at = time.monotonic()
            self._hierarchy_failures = 0
            self.measurements.observe("hierarchy", time.monotonic() - started)
            self._next_hierarchy = time.monotonic() + self.measurements.estimate("hierarchy", self.input_interval())
            return text
        except Cancelled:
            raise
        except Exception:
            self._hierarchy_failures += 1
            self.measurements.observe("hierarchy", time.monotonic() - started, success=False)
            self._hierarchy_cache = "<hierarchy/>"
            self.hierarchy_started_at = 0.0
            self.hierarchy_finished_at = 0.0
            self._next_hierarchy = time.monotonic() + self.measurements.timeout("hierarchy", RUNTIME_BOOTSTRAP_HIERARCHY_SECONDS) * (1 + math.log1p(self._hierarchy_failures))
            return self._hierarchy_cache
        finally:
            with contextlib.suppress(Exception):
                self._shell(["rm", "-f", target], timeout=RUNTIME_BOOTSTRAP_CONNECT_TIMEOUT_SECONDS, check=False)
            self._hierarchy_lock.release()

    def ui_snapshot(self, cancel=None, fresh=False):
        self._acquire_lock(self._hierarchy_lock, cancel)
        try:
            nodes = self.visible_ui_nodes(cancel, fresh=fresh)
            return {"nodes": nodes, "nodes_started_at": self.hierarchy_started_at, "nodes_at": self.hierarchy_finished_at}
        finally:
            self._hierarchy_lock.release()

    def visible_ui_nodes(self, cancel=None, limit=None, fresh=False):
        root = ET.fromstring(self.hierarchy(cancel, fresh=fresh))
        result = []
        width, height = self.screen_size()
        pending = [(root, ())]
        while pending:
            check_cancel(cancel)
            element, tree_path = pending.pop()
            pending.extend((child, tree_path + (index,)) for index, child in reversed(list(enumerate(element))))
            if self._tag(element) != "node":
                continue
            attributes = element.attrib
            if attributes.get("visible-to-user") == "false":
                continue
            text = str(attributes.get("text", "")).strip()
            description = str(attributes.get("content-desc", "")).strip()
            resource_id = str(attributes.get("resource-id", ""))
            enabled = attributes.get("enabled") != "false"
            clickable = attributes.get("clickable") == "true" and enabled
            scrollable = attributes.get("scrollable") == "true" and enabled
            long_clickable = attributes.get("long-clickable") == "true" and enabled
            focused = attributes.get("focused") == "true"
            checkable = attributes.get("checkable") == "true"
            if not text and not description and not (clickable or scrollable or long_clickable or focused or checkable):
                continue
            match = re.fullmatch(r"\[(-?\d+),(-?\d+)\]\[(-?\d+),(-?\d+)\]", str(attributes.get("bounds", "")))
            if match is None:
                continue
            left, top, right, bottom = map(int, match.groups())
            left, right = max(0, left), min(width, right)
            top, bottom = max(0, top), min(height, bottom)
            if right <= left or bottom <= top:
                continue
            result.append({"text": text or description, "content_desc": description, "id": resource_id.rsplit("/", 1)[-1], "resource_id": resource_id, "package": str(attributes.get("package", "")), "class": str(attributes.get("class", "")), "clickable": clickable, "scrollable": scrollable, "long_clickable": long_clickable, "focused": focused, "checkable": checkable, "checked": attributes.get("checked") == "true", "enabled": enabled, "selected": attributes.get("selected") == "true", "bounds": [left, top, right, bottom], "tree_path": "/".join(map(str, tree_path))})
            if limit is not None and len(result) >= max(1, int(limit)):
                break
        return result

    @staticmethod
    def _parse_input_layout(text):
        choices = []
        for block in re.split(r"(?m)(?=^add device\s+\d+:)", str(text)):
            axes = {}
            names = {"002f": "ABS_MT_SLOT", "0030": "ABS_MT_TOUCH_MAJOR", "0035": "ABS_MT_POSITION_X", "0036": "ABS_MT_POSITION_Y", "0039": "ABS_MT_TRACKING_ID", "003a": "ABS_MT_PRESSURE"}
            pattern = r"\b(ABS_MT_[A-Z_]+|002f|0030|0035|0036|0039|003a)(?:\s+\([0-9a-fA-F]{4}\))?\s*:[^\r\n]*?\bmin\s+(-?\d+)\s*,\s*max\s+(-?\d+)"
            for name, low, high in re.findall(pattern, block, flags=re.IGNORECASE):
                axes[names.get(name.lower(), name.upper())] = (int(low), int(high))
            required = {"ABS_MT_SLOT", "ABS_MT_TRACKING_ID", "ABS_MT_POSITION_X", "ABS_MT_POSITION_Y"}
            if not required.issubset(axes):
                continue
            sx, ex = axes["ABS_MT_POSITION_X"]
            sy, ey = axes["ABS_MT_POSITION_Y"]
            ss, es = axes["ABS_MT_SLOT"]
            tracking_min, tracking_max = axes["ABS_MT_TRACKING_ID"]
            tracking_min = max(0, tracking_min)
            slots = es - ss + 1
            if ex <= sx or ey <= sy or ss < 0 or slots < 1 or tracking_max - tracking_min + 1 < slots:
                continue
            device = re.search(r"add device\s+\d+:\s*(\S+)", block)
            name = re.search(r'name:\s*"([^"]+)"', block)
            layout = {"x_min": sx, "x_max": ex, "y_min": sy, "y_max": ey, "slot_min": ss, "slot_max": es, "tracking_min": tracking_min, "tracking_max": tracking_max, "pressure_min": axes.get("ABS_MT_PRESSURE", (0, 0))[0], "pressure_max": axes.get("ABS_MT_PRESSURE", (0, 0))[1], "touch_major_min": axes.get("ABS_MT_TOUCH_MAJOR", (0, 0))[0], "touch_major_max": axes.get("ABS_MT_TOUCH_MAJOR", (0, 0))[1], "device": device.group(1) if device else "", "name": name.group(1) if name else ""}
            preferred = bool(re.search(r"goldfish|qemu|virtio.*touch", layout["name"], re.I))
            choices.append(((preferred, slots), layout))
        return max(choices, key=lambda pair: pair[0])[1] if choices else None

    def _read_display_geometry(self, cancel=None):
        with self.measurements.measure("geometry"):
            with self._geometry_lock:
                self._geometry_requested += 1
                query = self._geometry_requested
                serial = self.serial
            output, _, _ = self._shell(["dumpsys", "input"], cancel=cancel)
            text = output.decode("utf-8", "replace")
            viewports = re.findall(r"[^\n]*(?:Viewport|DisplayViewport)[^\n]*", text)
            selected = next((line for line in viewports if re.search(r"displayId\s*=\s*0\b", line)), "")
            rotation = re.search(r"\borientation\s*=\s*([0-3])\b", selected)
            if rotation is None:
                rotation = re.search(r"SurfaceOrientation:\s*([0-3])\b", text)
            logical = re.search(r"logicalFrame\s*=\s*\[\s*(-?\d+)\s*,\s*(-?\d+)\s*,\s*(-?\d+)\s*,\s*(-?\d+)\s*\]", selected)
            if rotation is None:
                output, _, _ = self._shell(["dumpsys", "display"], cancel=cancel)
                rotation = re.search(r"\brotation\s+([0-3])\b", output.decode("utf-8", "replace"))
            if rotation is None:
                raise RuntimeError("无法读取安卓屏幕旋转方向")
            with self._geometry_lock:
                if serial != self.serial or query < self._geometry_applied:
                    return
                previous = self._display_rotation, self._display_size
                self._display_rotation = int(rotation.group(1))
                if logical:
                    left, top, right, bottom = map(int, logical.groups())
                    if right <= left or bottom <= top:
                        raise RuntimeError("安卓逻辑屏幕范围无效")
                    self._display_size = (right - left, bottom - top)
                else:
                    self._display_size = self.screen_size()
                self._geometry_dirty = self._display_size != self.screen_size()
                self._geometry_at = time.monotonic()
                self._geometry_applied = query
                self._geometry_changes += int(previous != (self._display_rotation, self._display_size))

    def _geometry_loop(self):
        while not self._geometry_stop.wait(self.geometry_interval()):
            if not self.booted or self._input_backend != "emulator_console":
                continue
            try:
                self._read_display_geometry(self._geometry_stop)
            except Cancelled:
                return
            except Exception:
                continue

    def _logical_to_raw(self, x, y):
        layout = self._input_layout
        if layout is None:
            raise RuntimeError("多点触控范围尚未准备")
        with self._geometry_lock:
            width, height, rotation = self.width, self.height, self._display_rotation
        u = max(0.0, min(1.0, float(x) / max(1, width - 1)))
        v = max(0.0, min(1.0, float(y) / max(1, height - 1)))
        if rotation == 1:
            u, v = 1.0 - v, u
        elif rotation == RUNTIME_ROTATION_HALF_TURN:
            u, v = 1.0 - u, 1.0 - v
        elif rotation == RUNTIME_ROTATION_THREE_QUARTER_TURN:
            u, v = v, 1.0 - u
        return (round(layout["x_min"] + u * (layout["x_max"] - layout["x_min"])), round(layout["y_min"] + v * (layout["y_max"] - layout["y_min"])))

    def _disconnect_console(self):
        with self._console_lock:
            connection, self._console_socket = self._console_socket, None
            self._console_buffer.clear()
            if connection is not None:
                with contextlib.suppress(OSError):
                    connection.shutdown(socket.SHUT_RDWR)
                with contextlib.suppress(OSError):
                    connection.close()

    def _console_reply(self, cancel=None, timeout=RUNTIME_BOOTSTRAP_CONSOLE_TIMEOUT_SECONDS):
        deadline = time.monotonic() + timeout
        lines = []
        size = 0
        while True:
            check_cancel(cancel)
            while b"\n" in self._console_buffer:
                line, _, remaining = self._console_buffer.partition(b"\n")
                self._console_buffer = bytearray(remaining)
                text = line.rstrip(b"\r").decode("utf-8", "replace")
                if text == "OK":
                    return "\n".join(lines)
                if text.startswith("KO:") or text == "KO":
                    raise RuntimeError("模拟器控制指令被拒绝：" + text[:RUNTIME_MAX_MESSAGE_CHARACTERS])
                lines.append(text)
                size += len(line)
            if time.monotonic() >= deadline:
                raise TimeoutError("模拟器控制通道响应超时")
            if size + len(self._console_buffer) > RUNTIME_CONSOLE_RESPONSE_BYTES:
                raise RuntimeError("模拟器控制通道返回内容异常")
            try:
                chunk = self._console_socket.recv(io.DEFAULT_BUFFER_SIZE)
            except socket.timeout:
                continue
            if not chunk:
                raise ConnectionError("模拟器控制通道已断开")
            self._console_buffer.extend(chunk)

    def _console_command_locked(self, command, cancel=None, timeout=None):
        check_cancel(cancel)
        if "\n" in command or "\r" in command:
            raise ValueError("模拟器控制指令不能包含换行")
        operation = "console:" + command.split(maxsplit=1)[0]
        selected_timeout = self.measurements.timeout(operation, RUNTIME_BOOTSTRAP_CONSOLE_TIMEOUT_SECONDS)
        if timeout is not None:
            selected_timeout = max(selected_timeout, float(timeout))
        with self.measurements.measure(operation):
            self._console_socket.sendall(command.encode("ascii") + b"\n")
            return self._console_reply(cancel, selected_timeout)

    def _release_command(self):
        layout = self._input_layout
        fields = []
        if layout is not None:
            for slot in range(layout["slot_min"], layout["slot_max"] + 1):
                fields.extend((runtime_input_event("slot", slot), runtime_input_event("tracking", -1)))
                if layout.get("pressure_max", 0) > 0:
                    fields.append(runtime_input_event("pressure", 0))
        fields.extend((runtime_input_event("contact", 0), runtime_input_event("sync", 0)))
        return "event send " + " ".join(fields)

    def _console_connect(self, cancel=None):
        if self._console_socket is not None:
            return
        check_cancel(cancel)
        if not self.console_port or self.process is None or self.process.poll() is not None:
            raise RuntimeError("模拟器触控通道尚未启动")
        try:
            self._console_socket = socket.create_connection(("127.0.0.1", self.console_port), timeout=RUNTIME_BOOTSTRAP_CONNECT_TIMEOUT_SECONDS)
            self._console_socket.settimeout(RUNTIME_SOCKET_POLL_SECONDS)
            self._console_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            self._console_buffer.clear()
            greeting = self._console_reply(cancel)
            if "Authentication required" in greeting:
                found = re.search(r"'([^'\r\n]+\.emulator_console_auth_token)'", greeting)
                candidates = [Path(found.group(1))] if found else []
                candidates.extend((self.profile / ".emulator_console_auth_token", self.user_home / ".emulator_console_auth_token"))
                native_profile = Path.home()
                if os.name == "nt":
                    buffer = ctypes.create_unicode_buffer(RUNTIME_WIN32_MAX_PATH_CHARACTERS)
                    shell = ctypes.WinDLL("shell32", use_last_error=True)
                    shell.SHGetFolderPathW.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_wchar_p]
                    shell.SHGetFolderPathW.restype = ctypes.c_long
                    if shell.SHGetFolderPathW(None, RUNTIME_WIN32_PROFILE_FOLDER, None, 0, buffer) == 0:
                        native_profile = Path(buffer.value)
                native_token = (native_profile / ".emulator_console_auth_token").resolve()
                candidates.append(native_token)
                token = ""
                for path in candidates:
                    resolved = path.resolve()
                    if (not resolved.is_relative_to(self.base.resolve()) and resolved != native_token) or not path.is_file() or path_is_link(path):
                        continue
                    token = path.read_text(encoding="utf-8").strip()
                    if re.fullmatch(r"[A-Za-z0-9+/_=-]{1,256}", token):
                        break
                    token = ""
                if not token:
                    raise RuntimeError("未找到当前用户的模拟器控制凭据")
                self._console_command_locked("auth " + token, cancel)
            self._touches.clear()
            if self._input_layout is not None:
                self._console_command_locked(self._release_command(), cancel)
        except Exception:
            self._disconnect_console()
            raise

    def touch_frame(self, pointers, cancel=None):
        try:
            with self.measurements.measure("touch"):
                return self._touch_frame(pointers, cancel)
        except BaseException:
            with contextlib.suppress(Exception):
                self.release_touches()
            raise

    def _touch_frame(self, pointers, cancel=None):
        check_cancel(cancel)
        if pointers and not self._input_verified:
            raise ComponentFailure("android", "触控通道尚未通过就绪验证")
        if self._input_backend != "emulator_console":
            return self._external_touch_frame(pointers, cancel)
        if not isinstance(pointers, (list, tuple)):
            raise ValueError("触点必须是列表")
        with self._action_lock:
            layout = self._input_layout
            if layout is None:
                raise RuntimeError("多点触控尚未准备")
            desired = {}
            identifiers = set()
            for pointer in pointers:
                if not isinstance(pointer, dict):
                    raise ValueError("触点格式错误")
                identifier = int(pointer.get("id", pointer.get("identifier", 0)))
                if identifier in identifiers:
                    raise ValueError("触点编号重复")
                identifiers.add(identifier)
                pressure = float(pointer.get("pressure", 1.0))
                if not math.isfinite(pressure):
                    raise ValueError("触点压力无效")
                if pressure <= 0:
                    continue
                x, y = float(pointer["x"]), float(pointer["y"])
                if not math.isfinite(x) or not math.isfinite(y):
                    raise ValueError("触点坐标无效")
                desired[identifier] = {"x": x, "y": y, "pressure": min(1.0, pressure)}
            if len(desired) > layout["slot_max"] - layout["slot_min"] + 1:
                raise ValueError("触点数量超出安卓设备能力")
            if desired and (self._geometry_dirty or time.monotonic() - self._geometry_at > self.geometry_interval()):
                self._read_display_geometry(cancel)
            if desired and self._geometry_dirty:
                raise GeometryPending("屏幕正在切换方向，等待下一帧确认坐标映射")
            with self._console_lock:
                try:
                    self._console_connect(cancel)
                    before = dict(self._touches)
                    available = set(range(layout["slot_min"], layout["slot_max"] + 1))
                    available.difference_update(value["slot"] for key, value in before.items() if key in desired)
                    fields = []
                    for identifier, previous in before.items():
                        if identifier not in desired:
                            fields.extend((runtime_input_event("slot", previous["slot"]), runtime_input_event("tracking", -1)))
                            if layout.get("pressure_max", 0) > 0:
                                fields.append(runtime_input_event("pressure", 0))
                    occupied_ids = {value["tracking"] for key, value in before.items() if key in desired}
                    after = {}
                    for identifier, point in desired.items():
                        previous = before.get(identifier)
                        slot = previous["slot"] if previous else min(available)
                        available.discard(slot)
                        fields.append(runtime_input_event("slot", slot))
                        if previous is None:
                            while True:
                                tracking_min = layout.get("tracking_min", 0)
                                self._touch_tracking_id = tracking_min + (self._touch_tracking_id - tracking_min + 1) % (layout["tracking_max"] - tracking_min + 1)
                                if self._touch_tracking_id not in occupied_ids:
                                    break
                            tracking = self._touch_tracking_id
                            occupied_ids.add(tracking)
                            fields.append(runtime_input_event("tracking", tracking))
                        else:
                            tracking = previous["tracking"]
                        x, y = self._logical_to_raw(point["x"], point["y"])
                        fields.extend((runtime_input_event("x", x), runtime_input_event("y", y)))
                        if layout.get("pressure_max", 0) > 0:
                            minimum = max(1, layout.get("pressure_min", 0))
                            fields.append(runtime_input_event("pressure", round(minimum + point["pressure"] * (layout["pressure_max"] - minimum))))
                        if layout.get("touch_major_max", 0) > 0:
                            pixel_span = min((layout["x_max"] - layout["x_min"]) / max(1, self.width), (layout["y_max"] - layout["y_min"]) / max(1, self.height))
                            contact = max(1, layout.get("touch_major_min", 0), round(pixel_span * math.sqrt(point["pressure"])))
                            fields.append(runtime_input_event("major", min(contact, layout["touch_major_max"])))
                        after[identifier] = {"slot": slot, "tracking": tracking, **point}
                    fields.extend((runtime_input_event("contact", bool(after)), runtime_input_event("sync", 0)))
                    self._console_command_locked("event send " + " ".join(fields), cancel)
                    self._touches = after
                    return {"submitted": True, "kind": "touch", "pointers": len(after), "capabilities": self.capabilities()}
                except BaseException:
                    self._disconnect_console()
                    raise

    def release_touches(self, cancel=None):
        if self._input_backend != "emulator_console":
            return self._release_external_touches(cancel)
        with self._action_lock:
            with self._console_lock:
                if self.process is None or self.process.poll() is not None:
                    self._touches.clear()
                    self._disconnect_console()
                    return
                try:
                    self._console_connect(cancel)
                    self._console_command_locked(self._release_command(), cancel, timeout=RUNTIME_BOOTSTRAP_CONNECT_TIMEOUT_SECONDS)
                    self._touches.clear()
                except Exception as first_error:
                    self._disconnect_console()
                    try:
                        self._adb_command(["emu"] + self._release_command().split(), timeout=RUNTIME_BOOTSTRAP_CONSOLE_TIMEOUT_SECONDS)
                        self._touches.clear()
                    except Exception:
                        raise first_error

    def game_context(self, cancel=None, fresh=False):
        check_cancel(cancel)
        if not fresh and time.monotonic() - self._last_context_at < self.measurements.estimate("shell:dumpsys", RUNTIME_STATUS_REFRESH_SECONDS):
            return dict(self._last_context)
        serial = self.serial
        output, _, _ = self._shell(["dumpsys", "activity", "activities"], cancel=cancel, timeout=RUNTIME_BOOTSTRAP_CONTEXT_SECONDS, check=False)
        if serial != self.serial:
            return {"package": "", "activity": "", "abis": list(self.abis), "size": list(self.screen_size()), "rotation": self._display_rotation}
        value = output.decode("utf-8", "replace")
        match = re.search(r"(?:mResumedActivity|topResumedActivity|mFocusedActivity|mCurrentFocus|mFocusedApp)[^\n]*?\s([A-Za-z0-9_]+(?:\.[A-Za-z0-9_]+)+)/([^\s}]+)", value)
        if match is None:
            try:
                fallback, _, _ = self._shell(["dumpsys", "window", "windows"], cancel=cancel, timeout=RUNTIME_BOOTSTRAP_CONTEXT_SECONDS, check=False)
                match = re.search(r"(?:mCurrentFocus|mFocusedApp|mObscuringWindow)[^\n]*?\s([A-Za-z0-9_]+(?:\.[A-Za-z0-9_]+)+)/([^\s}]+)", fallback.decode("utf-8", "replace"))
            except Cancelled:
                raise
            except (OSError, RuntimeError, TimeoutError):
                pass
        context = {"package": match.group(1) if match else "", "activity": match.group(2) if match else "", "abis": list(self.abis), "size": list(self.screen_size()), "rotation": self._display_rotation, "capabilities": self.capabilities()}
        if context.get("package") != self._last_context.get("package"):
            with self._hierarchy_lock:
                self._hierarchy_cache = "<hierarchy/>"
                self.hierarchy_started_at = 0.0
                self.hierarchy_finished_at = 0.0
                self._next_hierarchy = 0
        self._last_context = context
        self._last_context_at = time.monotonic()
        return dict(context)

    def user_packages(self, cancel=None, refresh=False):
        with self._package_lock:
            if not refresh and time.monotonic() - self._user_packages_at < self.measurements.timeout("shell:pm", RUNTIME_BOOTSTRAP_COMMAND_TIMEOUT_SECONDS):
                return set(self._user_packages)
            output, error, code = self._shell(["pm", "list", "packages", "-3"], cancel=cancel, timeout=RUNTIME_PACKAGE_LIST_TIMEOUT_SECONDS, check=False)
            if code:
                raise RuntimeError("读取已安装应用失败：" + (output + error).decode("utf-8", "replace")[-RUNTIME_MAX_MESSAGE_CHARACTERS:])
            packages = set()
            for line in output.decode("utf-8", "replace").splitlines():
                if line.startswith("package:"):
                    name = line[len("package:"):].strip()
                    if re.fullmatch(r"[A-Za-z0-9_]+(?:\.[A-Za-z0-9_]+)+", name) and name != "com.android.adbkeyboard":
                        packages.add(name)
            self._user_packages = packages
            self._user_packages_at = time.monotonic()
            return set(packages)

    def launch_package(self, package, cancel=None):
        package = str(package)
        if not re.fullmatch(r"[A-Za-z0-9_]+(?:\.[A-Za-z0-9_]+)+", package):
            raise ValueError("安卓应用包名无效")
        self.release_touches(cancel)
        output, error, code = self._shell(["monkey", "-p", package, "-c", "android.intent.category.LAUNCHER", "1"], cancel=cancel, timeout=RUNTIME_APP_LAUNCH_TIMEOUT_SECONDS, check=False)
        if code or b"No activities found" in output + error:
            raise RuntimeError("无法启动安卓应用：" + (output + error).decode("utf-8", "replace")[-RUNTIME_MAX_MESSAGE_CHARACTERS:])
        self._last_context_at = 0.0
        return {"submitted": True, "kind": "launch", "package": package}

    def screen_size(self):
        return self.width, self.height

    def install_apk(self, path, cancel=None):
        files = selected_apk_files(path)
        groups = {}
        native_abis = {}
        for file in files:
            check_cancel(cancel)
            metadata = apk_package_info(file)
            compatibility = apk_compatibility(file)
            if compatibility.get("min_sdk") and self.device_api_level and compatibility["min_sdk"] > self.device_api_level:
                raise ValueError("APK " + file.name + " 最低需要 Android API " + str(compatibility["min_sdk"]) + "，当前设备为 " + str(self.device_api_level))
            groups.setdefault(metadata["package"], []).append((file, metadata))
            native_abis.setdefault(metadata["package"], set()).update(compatibility["native_abis"])
        for package, items in groups.items():
            for file, metadata in items:
                file_abis = set(apk_compatibility(file)["native_abis"])
                if file_abis and self.abis and file_abis.isdisjoint(self.abis):
                    raise ValueError("APK 分包 " + file.name + " 的原生库 " + ", ".join(sorted(file_abis)) + " 与设备实际报告的 ABI 不兼容；不能只凭原生桥接程序名称推断支持")
            if native_abis[package] and self.abis and native_abis[package].isdisjoint(self.abis):
                raise ValueError("APK " + package + " 只包含 " + ", ".join(sorted(native_abis[package])) + " 原生库，当前设备支持 " + ", ".join(self.abis) + "；无法在该设备上直接运行")
            splits = [metadata["split"] for file, metadata in items]
            versions = {(metadata["version_code_major"], metadata["version_code"]) for file, metadata in items}
            if len(splits) != len(set(splits)):
                raise ValueError("同一应用包含重复 base APK 或重复 split：" + package)
            if len(versions) > 1:
                raise ValueError("同一应用的 base 与 split 版本不一致：" + package)
            if "" not in splits:
                raise ValueError("分包缺少 base APK：" + package)
        self.last_installed_packages = []
        results = []
        with self._action_lock:
            for package, items in groups.items():
                check_cancel(cancel)
                items.sort(key=lambda item: (bool(item[1]["split"]), item[1]["split"]))
                remote_paths = []
                session_id = None
                try:
                    for file, metadata in items:
                        remote = "/data/local/tmp/gameagent_" + uuid.uuid4().hex + ".apk"
                        remote_paths.append(remote)
                        self._sync_push(file, remote, cancel)
                    total_bytes = sum(file.stat().st_size for file, metadata in items)
                    timeout = max(RUNTIME_BOOTSTRAP_INSTALL_SECONDS, total_bytes / max(1, RUNTIME_BOOTSTRAP_INSTALL_BYTES_PER_SECOND))
                    if len(items) == 1:
                        output, error, code = self._shell(["pm", "install", "-r", remote_paths[0]], cancel=cancel, timeout=timeout, check=False)
                    else:
                        output, error, code = self._shell(["pm", "install-create", "-r", "-S", total_bytes], cancel=cancel, timeout=timeout, check=False)
                        response = (output + error).decode("utf-8", "replace")
                        match = re.search(r"Success.*\[(\d+)\]", response)
                        if code or not match:
                            raise RuntimeError("创建 APK 分包安装会话失败：" + response)
                        session_id = int(match.group(1))
                        for (file, metadata), remote in zip(items, remote_paths):
                            output, error, code = self._shell(["pm", "install-write", "-S", file.stat().st_size, session_id, (metadata["split"] or "base") + ".apk", remote], cancel=cancel, timeout=timeout, check=False)
                            response = (output + error).decode("utf-8", "replace")
                            if code or "Success" not in response:
                                raise RuntimeError("写入 APK 分包失败：" + response)
                        output, error, code = self._shell(["pm", "install-commit", session_id], cancel=cancel, timeout=timeout, check=False)
                    response = (output + error).decode("utf-8", "replace").strip()
                    if code or not re.search(r"(?:^|\n)Success(?:\s|$)", response):
                        raise RuntimeError("APK 安装失败：" + response[-RUNTIME_MAX_MESSAGE_CHARACTERS:])
                    session_id = None
                    self.last_installed_packages.append(package)
                    results.append(package + ": " + response)
                    self.log("apk_installed", package=package, names=[file.name for file, metadata in items], split_count=len(items), offline=True)
                finally:
                    if session_id is not None:
                        with contextlib.suppress(Exception):
                            self._shell(["pm", "install-abandon", session_id], timeout=RUNTIME_BOOTSTRAP_CONNECT_TIMEOUT_SECONDS, check=False)
                    if remote_paths:
                        with contextlib.suppress(Exception):
                            self._shell(["rm", "-f", *remote_paths], timeout=RUNTIME_BOOTSTRAP_CONNECT_TIMEOUT_SECONDS, check=False)
            self._user_packages_at = 0
        return "\n".join(results)

    def act(self, action, cancel=None):
        with self._action_lock:
            check_cancel(cancel)
            if not self._input_verified:
                raise ComponentFailure("android", "输入通道尚未通过就绪验证")
            kind = str(action.get("kind", action.get("action", ""))).lower()
            width, height = self.screen_size()
            clamp_x = lambda value: max(0, min(width - 1, int(value)))
            clamp_y = lambda value: max(0, min(height - 1, int(value)))
            if kind in ("tap", "click", "long_press", "long_click", "swipe", "scroll", "drag", "touch") and self._input_backend == "adb_gesture":
                return self._simple_gesture(action, cancel)
            if kind in ("tap", "click", "long_press", "long_click", "swipe", "scroll", "drag", "touch"):
                if kind == "touch":
                    points = action.get("pointers", [])
                    duration = float(action.get("ms", action.get("duration_ms", action.get("duration", self.default_action_ms(kind, points))))) / RUNTIME_MILLISECONDS_PER_SECOND
                elif kind in ("tap", "click"):
                    points = [{"id": 0, "x": action["x"], "y": action["y"]}]
                    duration = float(action.get("ms", self.default_action_ms("tap", points))) / RUNTIME_MILLISECONDS_PER_SECOND
                elif kind in ("long_press", "long_click"):
                    points = [{"id": 0, "x": action["x"], "y": action["y"]}]
                    duration = float(action.get("ms", self.default_action_ms("long_press", points))) / RUNTIME_MILLISECONDS_PER_SECOND
                else:
                    x = action["x"] if "x" in action else action["x1"]
                    y = action["y"] if "y" in action else action["y1"]
                    points = [{"id": 0, "x": x, "y": y, "x2": action["x2"], "y2": action["y2"]}]
                    duration = float(action.get("ms", action.get("duration_ms", action.get("duration", self.default_action_ms(kind, points))))) / RUNTIME_MILLISECONDS_PER_SECOND
                if not math.isfinite(duration) or duration < 0:
                    raise ValueError("触控时长无效")
                if not isinstance(points, (list, tuple)):
                    raise ValueError("触点必须是列表")
                held = [{"id": identifier, "x": item["x"], "y": item["y"], "pressure": item.get("pressure", 1.0)} for identifier, item in self._touches.items()]
                used_ids = {item["id"] for item in held}
                trajectories = []
                for index, point in enumerate(points):
                    if not isinstance(point, dict):
                        raise ValueError("触点格式错误")
                    x, y = float(point["x"]), float(point["y"])
                    x2, y2 = float(point.get("x2", x)), float(point.get("y2", y))
                    if not all(math.isfinite(number) for number in (x, y, x2, y2)):
                        raise ValueError("触点坐标无效")
                    requested_id = int(point.get("id", point.get("identifier", index)))
                    while requested_id in used_ids:
                        requested_id += 1
                    used_ids.add(requested_id)
                    trajectories.append({"id": requested_id, "x": x, "y": y, "x2": x2, "y2": y2, "pressure": point.get("pressure", 1.0)})
                if self._input_layout is not None and len(held) + len(trajectories) > self._input_layout["slot_max"] - self._input_layout["slot_min"] + 1:
                    raise ValueError("当前连续触控和临时动作的触点总数超出设备能力")
                try:
                    started = time.monotonic()
                    moving = any(point["x"] != point["x2"] or point["y"] != point["y2"] for point in trajectories)
                    self.touch_frame(held + [{key: point[key] for key in ("id", "x", "y", "pressure")} for point in trajectories], cancel)
                    if moving and duration > 0:
                        while True:
                            remaining = duration - (time.monotonic() - started)
                            if remaining <= 0:
                                break
                            self._wait(cancel, min(self.input_interval(), remaining))
                            ratio = min(1.0, (time.monotonic() - started) / duration)
                            self.touch_frame(held + [{"id": point["id"], "x": point["x"] + (point["x2"] - point["x"]) * ratio, "y": point["y"] + (point["y2"] - point["y"]) * ratio, "pressure": point["pressure"]} for point in trajectories], cancel)
                        self.touch_frame(held + [{"id": point["id"], "x": point["x2"], "y": point["y2"], "pressure": point["pressure"]} for point in trajectories], cancel)
                    else:
                        self._wait(cancel, max(0, duration - (time.monotonic() - started)))
                    check_cancel(cancel)
                    elapsed = time.monotonic() - started
                    self.measurements.observe("gesture:" + kind, elapsed)
                    motion = max((math.hypot(point["x2"] - point["x"], point["y2"] - point["y"]) for point in trajectories), default=0) / max(1, math.hypot(width, height))
                    if motion > 0:
                        self.measurements.observe("gesture_motion", elapsed, units=motion)
                    return {"submitted": True, "kind": kind, "pointers": len(trajectories), "ms": round(elapsed * RUNTIME_MILLISECONDS_PER_SECOND), "requested_ms": round(duration * RUNTIME_MILLISECONDS_PER_SECOND)}
                finally:
                    if held and (cancel is None or not cancel.is_set()):
                        self.touch_frame(held)
                    else:
                        self.release_touches()
            if kind in ("back", "home", "enter", "recent", "recents"):
                key = {"back": "KEYCODE_BACK", "home": "KEYCODE_HOME", "enter": "KEYCODE_ENTER", "recent": "KEYCODE_APP_SWITCH", "recents": "KEYCODE_APP_SWITCH"}[kind]
                args = ["input", "keyevent", key]
            elif kind in ("key", "keyevent"):
                key = str(action.get("key", action.get("text", ""))).strip().upper()
                if not re.fullmatch(r"(?:KEYCODE_[A-Z0-9_]+|[0-9]+)", key):
                    raise ValueError("无效的安卓按键代码")
                args = ["input", "keyevent", key]
            elif kind in ("type", "text", "type_text"):
                return self._type_text(action, cancel)
            elif kind in ("wait", "observe"):
                seconds = float(action["ms"]) / RUNTIME_MILLISECONDS_PER_SECOND if "ms" in action else float(action.get("seconds", self.measurements.estimate("exec:screencap", self.input_interval())))
                if not math.isfinite(seconds) or seconds < 0:
                    raise ValueError("观察时长无效")
                self._wait(cancel, seconds)
                return {"submitted": True, "kind": kind, "seconds": seconds}
            elif kind in ("launch", "open_app"):
                return self.launch_package(action.get("package", ""), cancel)
            elif kind in ("release", "release_touches"):
                self.release_touches(cancel)
                return {"submitted": True, "kind": "release"}
            else:
                raise ValueError("不支持的安卓动作：" + kind)
            self.release_touches(cancel)
            output, error, _ = self._shell(args, cancel=cancel, timeout=RUNTIME_APP_LAUNCH_TIMEOUT_SECONDS)
            return {"submitted": True, "kind": kind, "detail": (output + error).decode("utf-8", "replace")[-RUNTIME_MAX_MESSAGE_CHARACTERS:]}

    def _log_tail(self, name, limit):
        try:
            path = self.logs / name
            with path.open("rb") as stream:
                stream.seek(max(0, path.stat().st_size - limit))
                return stream.read(limit).decode("utf-8", "replace")
        except OSError:
            return ""

    def diagnostics(self, cancel=None):
        check_cancel(cancel)
        result = {"ready": self.ready(cancel), "runtime_ready": self.alive(), "owned": self.owned, "serial": self.serial, "adb_port": self.adb_port, "device_api_level": self.device_api_level, "abis": self.abis, "native_bridge": self.native_bridge, "image_package": self.IMAGE_PACKAGE, "screen": list(self.screen_size()), "capabilities": self.capabilities(), "memory_mb": self.memory_mb, "cores": self.cores, "acceleration": self.acceleration, "gpu": self.gpu_mode, "boot_mode": self._boot_mode, "measurements": self.measurements.snapshot(), "adb_recent_log": self._log_tail("adb.log", RUNTIME_DIAGNOSTIC_TAIL_BYTES), "emulator_recent_log": self._log_tail("emulator.log", RUNTIME_DIAGNOSTIC_TAIL_BYTES)}
        if self.booted:
            for key, command in (("activity", ["dumpsys", "activity", "activities"]), ("logcat", ["logcat", "-d", "-t", str(RUNTIME_LOGCAT_LINES)])):
                try:
                    output, error, _ = self._shell(command, cancel=cancel, timeout=RUNTIME_PACKAGE_LIST_TIMEOUT_SECONDS, check=False)
                    result[key] = (output + error).decode("utf-8", "replace")[-RUNTIME_DIAGNOSTIC_TEXT_BYTES:]
                except Cancelled:
                    raise
                except Exception as exc:
                    result[key + "_error"] = str(exc)
        return result

    def state_paths(self):
        return [self.marker, self._connection_marker, self._graphics_profile_path, self.measurements.path, self.avd / "config.ini", self.avd / "gameai-boot.json", self.avd_home / (self.avd_name + ".ini"), self.logs / "emulator.log", self.logs / "adb.log", self.logs / "adb-native.log"]

    def _kill_owned(self, process):
        if process is None:
            return
        job = self._emulator_job if process is self.process else self._adb_job if process is self.adb_process else None
        if job is not None:
            with contextlib.suppress(Exception):
                job.close()
        if process.poll() is None:
            with contextlib.suppress(ProcessLookupError):
                process.kill()
        try:
            process.wait(timeout=RUNTIME_PROCESS_REAP_SECONDS)
        except subprocess.TimeoutExpired:
            self.log("owned_process_reap_pending", pid=process.pid)

    def _stop_emulator(self, save_snapshot=False):
        self._input_verified = False
        if self._external:
            with contextlib.suppress(Exception):
                self.release_touches()
            self._disconnect_adb_streams()
            self.booted = False
            self._touches.clear()
            self._input_layout = None
            return
        with contextlib.suppress(Exception):
            self.release_touches()
        self._disconnect_adb_streams()
        process = self.process
        booted = self.booted
        graceful = False
        if process is not None and process.poll() is None:
            try:
                with self._console_lock:
                    self._console_connect()
                    self._console_command_locked("kill", timeout=RUNTIME_BOOTSTRAP_CONSOLE_TIMEOUT_SECONDS)
            except Exception:
                with contextlib.suppress(Exception):
                    self._adb_command(["emu", "kill"], timeout=RUNTIME_BOOTSTRAP_CONSOLE_TIMEOUT_SECONDS, check=False)
            self._disconnect_console()
            try:
                shutdown_started = time.monotonic()
                code = process.wait(timeout=self.measurements.timeout("snapshot_save", RUNTIME_BOOTSTRAP_SNAPSHOT_SAVE_SECONDS) if save_snapshot and self._snapshot_enabled and booted else self.measurements.timeout("shutdown", RUNTIME_BOOTSTRAP_SHUTDOWN_SECONDS))
                graceful = code == 0
                self.measurements.observe("snapshot_save" if save_snapshot else "shutdown", time.monotonic() - shutdown_started, success=graceful)
            except subprocess.TimeoutExpired:
                self.log("android_shutdown_timeout", snapshot_requested=bool(save_snapshot))
                self._kill_owned(process)
        self._disconnect_console()
        if process is not None and self._launched_avd is not None:
            snapshot = self._launched_avd / "snapshots" / "default_boot" / "snapshot.pb"
            clean_snapshot = False
            if save_snapshot and graceful and booted and self._snapshot_enabled:
                with contextlib.suppress(OSError):
                    clean_snapshot = snapshot.is_file() and not path_is_link(snapshot) and snapshot.stat().st_mtime_ns >= self._launch_wall_ns
            with contextlib.suppress(OSError):
                atomic_json(self._launched_avd / "gameai-boot.json", {"running": False, "clean_snapshot": clean_snapshot, "signature": self._snapshot_signature, "closed_ns": time.time_ns()})
            self.log("android_shutdown", graceful=graceful, quick_boot_saved=clean_snapshot)
        if self._emulator_job is not None:
            self._emulator_job.close()
            self._emulator_job = None
        self.process = None
        self.booted = False
        self._touches.clear()
        self._input_layout = None
        self._last_context_at = 0.0
        self._last_context = {}

    def force_recycle(self):
        self._input_verified = False
        if self._external:
            with contextlib.suppress(Exception):
                self.release_touches()
            self._disconnect_adb_streams()
            self.booted = False
            self._prepared = False
            self._touches.clear()
            self._input_layout = None
            self._last_context = {}
            self._last_context_at = 0
            self._last_health = 0
            return
        self._force_cold_boot = True
        self._disconnect_adb_streams()
        current_emulator, current_adb = self.process, self.adb_process
        self._kill_owned(current_emulator)
        self._kill_owned(current_adb)
        if self.process is current_emulator:
            self.process = None
        if self.adb_process is current_adb:
            self.adb_process = None
        self.booted = False
        self._disconnect_console()
        self._touches.clear()
        self._input_layout = None
        self._last_context_at = 0.0
        self._last_context = {}
        self.serial = None
        self._last_health = 0.0
        if self._emulator_job is not None:
            self._emulator_job.close()
            self._emulator_job = None
        if self._adb_job is not None:
            self._adb_job.close()
            self._adb_job = None

    def close(self):
        self._geometry_stop.set()
        with contextlib.suppress(Exception):
            self.release_touches()
        self._stop_emulator(save_snapshot=True)
        self._disconnect_adb_streams()
        if self.adb_process is not None:
            self._kill_owned(self.adb_process)
        if self._adb_job is not None:
            self._adb_job.close()
            self._adb_job = None
        self.adb_process = None
        self._closed = True
        if self._geometry_thread is not None and self._geometry_thread is not threading.current_thread():
            self._geometry_thread.join(timeout=RUNTIME_MINIMUM_PROCESS_STOP_SECONDS)
        with contextlib.suppress(OSError):
            self.measurements.save()

    def input_interval(self):
        frame_period = 1 / max(1, self._refresh_hz)
        return max(frame_period, self.measurements.estimate("touch", frame_period))

    def geometry_interval(self):
        return max(self.input_interval(), self.measurements.estimate("geometry", RUNTIME_STATUS_REFRESH_SECONDS))

    def validate_input(self, cancel=None):
        check_cancel(cancel)
        self._input_verified = False
        if not (self.owned and not self._external or self._external and self._local_authorized):
            raise ComponentFailure("android", "当前输入通道没有绑定已验证的本地游戏模拟器")
        if not self.alive():
            raise ComponentFailure("android", "输入通道验证前安卓实例已离线")
        backend = self._input_backend
        if backend == "emulator_console":
            layout = self._input_layout or {}
            if layout.get("slot_max", -1) < layout.get("slot_min", 0):
                raise ComponentFailure("android", "模拟器未提供可验证的触控槽位")
            self.release_touches(cancel)
        elif backend in {"adb_motionevent", "adb_gesture"}:
            required = {"tap", "swipe", "keyevent"}
            if backend == "adb_motionevent":
                required.add("motionevent")
            if not required.issubset(self._input_commands):
                raise ComponentFailure("android", "安卓 input 帮助未确认必要操作：" + ", ".join(sorted(required - self._input_commands)))
            self.release_touches(cancel)
        else:
            raise ComponentFailure("android", "没有经过验证的游戏输入通道")
        check_cancel(cancel)
        if not self.alive():
            raise ComponentFailure("android", "输入通道验证期间安卓实例已离线")
        self._input_verified = True
        capabilities = self.capabilities()
        return {"verified": True, "backend": backend, "touch_slots": capabilities["touch_slots"], "actions": capabilities["actions"], "evidence": "console_release_acknowledged" if backend == "emulator_console" else "android_input_supported_commands", "owned": self.owned, "local_authorized": self._local_authorized}

    def capabilities(self):
        layout = self._input_layout or {}
        verified = bool(self._input_verified and (self.owned and not self._external or self._external and self._local_authorized))
        slots = max(0, layout.get("slot_max", -1) - layout.get("slot_min", 0) + 1) if verified else 0
        continuous = slots if self._input_backend in {"emulator_console", "adb_motionevent"} else 0
        actions = set()
        if verified:
            actions.add("wait")
            if self._input_backend == "emulator_console" or "tap" in self._input_commands:
                actions.add("tap")
            if self._input_backend == "emulator_console" or "swipe" in self._input_commands:
                actions.update({"long_press", "swipe", "touch"})
            if "keyevent" in self._input_commands:
                actions.update({"back", "home", "recents", "enter", "keyevent"})
            if "text" in self._input_commands or self._existing_unicode_ime:
                actions.add("type")
            if continuous:
                actions.update({"touch_begin", "touch_update", "touch_end", "touch_release_all"})
        return {"verified": verified, "touch_slots": slots, "continuous_touch_slots": continuous, "refresh_hz": self._refresh_hz, "long_press_ms": self._long_press_ms, "input_latency_seconds": self.measurements.estimate("touch", self.input_interval()), "input_backend": self._input_backend, "buffered_manual_gestures": verified and self._input_backend == "adb_gesture", "unicode_text": self._existing_unicode_ime, "owned": self.owned, "actions": [kind for kind in AI_ACTION_KINDS if kind in actions]}

    def default_action_ms(self, kind, points):
        frame_ms = self.input_interval() * RUNTIME_MILLISECONDS_PER_SECOND
        if kind in ("tap", "click"):
            return max(frame_ms * RUNTIME_BOOTSTRAP_TAP_FRAMES, self.measurements.estimate("gesture:tap", 0) * RUNTIME_MILLISECONDS_PER_SECOND)
        if kind in ("long_press", "long_click"):
            return self._long_press_ms + frame_ms
        distance = max((math.hypot(float(point.get("x2", point["x"])) - float(point["x"]), float(point.get("y2", point["y"])) - float(point["y"])) for point in points if isinstance(point, dict) and "x" in point and "y" in point), default=0)
        fraction = distance / max(1, math.hypot(self.width, self.height))
        seconds_per_screen = self.measurements.estimate("gesture_motion:per_unit", self._long_press_ms / RUNTIME_MILLISECONDS_PER_SECOND)
        return max(frame_ms, fraction * seconds_per_screen * RUNTIME_MILLISECONDS_PER_SECOND)

    def configure_visual_budget(self, pixel_budget=None):
        if self._external or self.booted or self.process is not None and self.process.poll() is None:
            return {"changed": False, "screen": list(self.screen_size()), "source": "active_device"}
        if (self.avd / "config.ini").is_file():
            return {"changed": False, "screen": list(self.screen_size()), "source": "existing_device"}
        width, height, refresh = runtime_default_display(pixel_budget, self.memory_mb)
        changed = (width, height) != self.screen_size()
        self.width, self.height, self._refresh_hz = width, height, refresh
        self._display_size = width, height
        self._geometry_dirty = True
        result = {"changed": changed, "screen": [width, height], "source": "desktop_and_memory" if pixel_budget is None else "visual_budget", "pixel_budget": pixel_budget, "memory_mb": self.memory_mb}
        self.log("android_visual_budget", **result)
        return result

    @staticmethod
    def _acquire_lock(lock, cancel=None):
        while not lock.acquire(timeout=RUNTIME_SOCKET_POLL_SECONDS):
            check_cancel(cancel)
        try:
            check_cancel(cancel)
        except BaseException:
            lock.release()
            raise

    def _local_sdk_roots(self):
        candidates = [self.root / "sdk"]
        saved = read_json(self.marker, {})
        if isinstance(saved, dict) and isinstance(saved.get("sdk_directory"), str) and saved["sdk_directory"]:
            candidates.append(Path(saved["sdk_directory"]))
        for name in ("ANDROID_SDK_ROOT", "ANDROID_HOME"):
            value = os.environ.get(name)
            if value:
                candidates.append(Path(value))
        local = os.environ.get("LOCALAPPDATA")
        if local:
            candidates.append(Path(local) / "Android" / "Sdk")
        candidates.append(Path.home() / "AppData" / "Local" / "Android" / "Sdk")
        for binary in (shutil.which("adb.exe"), shutil.which("adb"), shutil.which("emulator.exe"), shutil.which("emulator")):
            if binary:
                path = Path(binary)
                candidates.append(path.parent.parent)
        if os.name == "nt":
            try:
                import winreg
                for hive in (winreg.HKEY_CURRENT_USER, winreg.HKEY_LOCAL_MACHINE):
                    for key_name in (r"SOFTWARE\Android SDK Tools", r"SOFTWARE\WOW6432Node\Android SDK Tools"):
                        try:
                            with winreg.OpenKey(hive, key_name) as key:
                                value, _ = winreg.QueryValueEx(key, "Path")
                                if isinstance(value, str):
                                    candidates.append(Path(value))
                        except OSError:
                            continue
            except ImportError:
                pass
        result = []
        seen = set()
        for candidate in candidates:
            try:
                if os.name == "nt" and str(candidate).startswith("\\\\"):
                    continue
                path = candidate.expanduser().resolve()
                key = os.path.normcase(str(path))
                if key not in seen and path.is_dir():
                    seen.add(key)
                    result.append(path)
            except OSError:
                continue
        return result

    def _system_image_choice(self, sdk, image, minimum_sdk=0):
        try:
            sdk, image = Path(sdk).expanduser().resolve(), Path(image).expanduser().resolve()
            image.relative_to(sdk / "system-images")
            api_match = re.fullmatch(r"android-(\d+)", image.parent.parent.name)
            architectures = {"x86_64", "x86"} if os.name == "nt" and platform.machine().casefold() in {"amd64", "x86_64", "x64"} else {"x86_64", "x86", "arm64-v8a", "armeabi-v7a"}
            if image.name not in architectures or not api_match or int(api_match.group(1)) < minimum_sdk:
                return None
            executable = "emulator.exe" if os.name == "nt" else "emulator"
            adb_name = "adb.exe" if os.name == "nt" else "adb"
            emulator, adb = sdk / "emulator" / executable, sdk / "platform-tools" / adb_name
            required = (emulator, adb, image / "system.img", image / "userdata.img", image / "ramdisk.img")
            kernels = (image / "kernel-ranchu", image / "kernel-ranchu-64")
            if not all(path.is_file() and path.stat().st_size > 0 for path in required):
                return None
            if not any(path.is_file() and path.stat().st_size > 0 for path in kernels):
                return None
            return int(api_match.group(1)), str(image), sdk, emulator, adb, image
        except (OSError, ValueError):
            return None

    def _cached_system_image(self, record):
        if not isinstance(record, dict) or record.get("mode") != "local_components":
            return None
        sdk, image = record.get("sdk_directory"), record.get("image_directory")
        if not isinstance(sdk, str) or not sdk or not isinstance(image, str) or not image:
            return None
        return self._system_image_choice(sdk, image)

    def _local_system_images(self, minimum_sdk=0, cancel=None):
        from concurrent.futures import ThreadPoolExecutor, as_completed
        def inspect(sdk):
            found = []
            check_cancel(cancel)
            try:
                for image in (sdk / "system-images").glob("android-*/*/*"):
                    check_cancel(cancel)
                    choice = self._system_image_choice(sdk, image, minimum_sdk)
                    if choice is not None:
                        found.append(choice)
            except OSError as exc:
                self.log("local_sdk_probe_error", sdk=str(sdk), error=str(exc))
            return found
        roots = self._local_sdk_roots()
        if not roots:
            return []
        if len(roots) == 1:
            choices = inspect(roots[0])
        else:
            choices = []
            with ThreadPoolExecutor(max_workers=min(len(roots), runtime_io_capacity()), thread_name_prefix="LocalAndroidProbe") as executor:
                futures = [executor.submit(inspect, sdk) for sdk in roots]
                try:
                    for future in as_completed(futures):
                        check_cancel(cancel)
                        choices.extend(future.result())
                except BaseException:
                    for future in futures:
                        future.cancel()
                    raise
        return sorted(choices, key=lambda value: (value[-1].name == "x86_64", value[-1].name == "x86", value[0], value[1]), reverse=True)

    def _local_adb_executables(self):
        roots = self._local_sdk_roots()
        discovered = []
        names = ("adb.exe",) if os.name == "nt" else ("adb",)
        for sdk in roots:
            for name in names:
                discovered.append(sdk / "platform-tools" / name)
        for name in names:
            candidate = shutil.which(name)
            if candidate:
                discovered.append(Path(candidate))
        for variable in ("ProgramFiles", "ProgramFiles(x86)", "LOCALAPPDATA"):
            base = os.environ.get(variable)
            if not base:
                continue
            parent = Path(base)
            for vendor in RUNTIME_LOCAL_ANDROID_VENDOR_FOLDERS:
                folder = parent / vendor
                for tail in (folder, folder / "bin", folder / "shell"):
                    for name in RUNTIME_LOCAL_ANDROID_ADB_FILENAMES:
                        discovered.append(tail / name)
                if folder.is_dir():
                    for child in folder.iterdir():
                        if not child.is_dir():
                            continue
                        for tail in (child, child / "bin", child / "shell"):
                            for name in RUNTIME_LOCAL_ANDROID_ADB_FILENAMES:
                                discovered.append(tail / name)
        unique = set()
        result = []
        for candidate in discovered:
            try:
                path = candidate.resolve()
                name = os.path.normcase(str(path))
                if name not in unique and path.is_file() and not path_is_link(path):
                    unique.add(name)
                    result.append(path)
            except OSError:
                continue
        return result

    @staticmethod
    def _local_port_listening(port):
        try:
            with socket.create_connection(("127.0.0.1", port), timeout=RUNTIME_SOCKET_POLL_SECONDS):
                return True
        except OSError:
            return False

    def _attach_local_emulator(self, cancel=None):
        check_cancel(cancel)
        candidates = self._local_adb_executables()
        if not candidates:
            return False
        remembered = read_json(self._connection_marker, {})
        known_adb = remembered.get("adb") if isinstance(remembered, dict) else None
        if isinstance(known_adb, str):
            try:
                preferred_adb = Path(known_adb).resolve()
                candidates.sort(key=lambda path: path != preferred_adb)
            except (OSError, ValueError):
                pass
        port = remembered.get("loopback_port") if isinstance(remembered, dict) else None
        ports = list(dict.fromkeys(([port] if type(port) is int and port in RUNTIME_LOCAL_ANDROID_ADB_PORTS else []) + list(RUNTIME_LOCAL_ANDROID_ADB_PORTS)))
        if not any(self._local_port_listening(number) for number in ports):
            return False
        self.adb = candidates[0]
        self._external = True
        self.owned = False
        self._local_authorized = False
        self._prepared = False
        self.serial = None
        self.adb_port = None
        try:
            self._start_adb(cancel)
            for number in ports:
                check_cancel(cancel)
                if not self._local_port_listening(number):
                    continue
                address = "127.0.0.1:" + str(number)
                try:
                    answer = self._adb_host("host:connect:" + address, cancel, timeout=RUNTIME_LOCAL_ANDROID_ADB_PROBE_SECONDS).decode("utf-8", "replace")
                    if not any(word in answer.casefold() for word in ("connected", "already connected")):
                        continue
                    self.serial = address
                    fields = []
                    for key in ("sys.boot_completed", "ro.kernel.qemu", "ro.hardware", "ro.product.model", "ro.product.manufacturer"):
                        output, error, code = self._shell(["getprop", key], cancel=cancel, timeout=RUNTIME_LOCAL_ANDROID_ADB_PROBE_SECONDS, check=False)
                        fields.append(output.decode("utf-8", "replace").strip() if code == 0 else "")
                    if fields[0] != "1" or not (fields[1] == "1" or any(hint in " ".join(fields[2:]).casefold() for hint in RUNTIME_LOCAL_ANDROID_VIRTUAL_HINTS)):
                        continue
                    self._local_authorized = True
                    self._prepared = True
                    self._closed = False
                    self._input_verified = False
                    self._last_health = 0.0
                    self._connection_marker.parent.mkdir(parents=True, exist_ok=True)
                    atomic_json(self._connection_marker, {"mode": "verified_local_emulator", "loopback_port": number, "adb": str(self.adb), "verified_virtual_device": True})
                    self.log("verified_local_emulator", port=number, evidence=fields, adb=str(self.adb), scope="loopback_only")
                    self.status("已复用当前电脑运行中的本地安卓模拟器 · " + address)
                    return True
                except Cancelled:
                    raise
                except (OSError, TimeoutError, ValueError, RuntimeError) as exc:
                    self.log("local_emulator_probe_failed", port=number, reason=str(exc)[:RUNTIME_MAX_MESSAGE_CHARACTERS])
                finally:
                    if not self._local_authorized:
                        self.serial = None
        except Cancelled:
            raise
        except (OSError, TimeoutError, ValueError, RuntimeError) as exc:
            self.log("local_emulator_attach_failed", error=str(exc))
        if self.adb_process is not None:
            self._kill_owned(self.adb_process)
            self.adb_process = None
        if self._adb_job is not None:
            self._adb_job.close()
            self._adb_job = None
        self._external = False
        self.owned = True
        self._local_authorized = False
        self.adb_port = None
        self.serial = None
        return False

    def _select_local_image(self, choice):
        api, _, sdk, emulator, adb, image = choice
        self.sdk, self.emulator, self.adb, self.image = sdk, emulator, adb, image
        self.IMAGE_PACKAGE = "system-images;android-" + str(api) + ";" + image.parent.name + ";" + image.name
        legacy_name = "GameAI_API" + str(api)
        legacy_config = self.avd_home / (legacy_name + ".avd") / "config.ini"
        legacy_matches = False
        if legacy_config.is_file():
            try:
                values = dict(line.split("=", 1) for line in legacy_config.read_text(encoding="utf-8-sig").splitlines() if "=" in line)
                legacy_matches = values.get("tag.id", "").strip() == image.parent.name and values.get("abi.type", "x86_64").strip() == image.name
            except (OSError, ValueError):
                pass
        suffix = re.sub(r"[^A-Za-z0-9_]", "_", image.parent.name + "_" + image.name)
        self.avd_name = legacy_name if legacy_matches or not (self.avd_home / (legacy_name + ".avd")).exists() else legacy_name + "_" + suffix
        self.avd = self.avd_home / (self.avd_name + ".avd")
        self.avd.mkdir(parents=True, exist_ok=True)
        self.owned = True
        self._external = False
        self._local_authorized = False
        atomic_json(safe_workspace_file(self.base, self.marker), {"image_package": self.IMAGE_PACKAGE, "image_directory": str(self.image), "sdk_directory": str(self.sdk), "mode": "local_components", "installed_files": {name: {"size": path.stat().st_size, "mtime_ns": path.stat().st_mtime_ns} for name, path in self._critical_files().items()}})
        self._prepared = True
        self._load_graphics_profile()
        self.log("local_android_components", sdk=str(sdk), system_image=str(image), api=api, owned=True)

    def alive(self):
        if self._closed or not self.booted or not self.serial or self.adb_port is None:
            return False
        if self._external:
            return True
        return self.process is not None and self.process.poll() is None and self.adb_process is not None and self.adb_process.poll() is None

    def _external_touch_frame(self, pointers, cancel=None):
        check_cancel(cancel)
        if not isinstance(pointers, (list, tuple)):
            raise ValueError("触点必须是列表")
        desired = [point for point in pointers if float(point.get("pressure", 1)) > 0]
        if len(desired) > 1:
            raise ValueError("当前本地设备输入通道只支持单指，未发送多点动作")
        with self._action_lock:
            if self._pending_external_release:
                self._release_external_touches()
            previous = next(iter(self._touches.values()), None)
            point = None
            if desired:
                value = desired[0]
                coordinates = float(value["x"]), float(value["y"])
                if not all(math.isfinite(number) for number in coordinates):
                    raise ValueError("触点坐标必须是有限数")
                point = {"id": int(value.get("id", 0)), "x": max(0, min(self.width - 1, round(coordinates[0]))), "y": max(0, min(self.height - 1, round(coordinates[1]))), "pressure": 1}
            if self._motion_event:
                if previous and (point is None or point["id"] != previous["id"]):
                    self._shell(["input", "touchscreen", "motionevent", "UP", previous["x"], previous["y"]], cancel=cancel)
                    self._touches.clear()
                    previous = None
                if point and (previous is None or (point["x"], point["y"]) != (previous["x"], previous["y"])):
                    self._touches = {point["id"]: point}
                    try:
                        self._shell(["input", "touchscreen", "motionevent", "MOVE" if previous else "DOWN", point["x"], point["y"]], cancel=cancel)
                    except BaseException:
                        with contextlib.suppress(Exception):
                            self._release_external_touches()
                        raise
                return {"submitted": True, "kind": "touch", "pointers": len(self._touches), "input_backend": self._input_backend}
            if point:
                if previous and previous["id"] != point["id"]:
                    raise ValueError("单指手势尚未释放，不能切换触点编号")
                point["start_x"] = previous["start_x"] if previous else point["x"]
                point["start_y"] = previous["start_y"] if previous else point["y"]
                point["started"] = previous["started"] if previous else time.monotonic()
                self._touches = {point["id"]: point}
                return {"submitted": False, "buffered": True, "kind": "touch", "pointers": 1, "input_backend": self._input_backend}
            self._touches.clear()
            if previous:
                duration_ms = max(1, round((time.monotonic() - previous["started"]) * RUNTIME_MILLISECONDS_PER_SECOND))
                if (previous["x"], previous["y"]) == (previous["start_x"], previous["start_y"]) and duration_ms < self._long_press_ms:
                    self._shell(["input", "touchscreen", "tap", previous["x"], previous["y"]], cancel=cancel)
                else:
                    self._shell(["input", "touchscreen", "swipe", previous["start_x"], previous["start_y"], previous["x"], previous["y"], duration_ms], cancel=cancel, timeout=duration_ms / RUNTIME_MILLISECONDS_PER_SECOND + RUNTIME_BOOTSTRAP_SHELL_TIMEOUT_SECONDS)
            return {"submitted": bool(previous), "kind": "touch", "pointers": 0, "input_backend": self._input_backend}

    def _release_external_touches(self, cancel=None):
        with self._action_lock:
            previous = next(iter(self._touches.values()), None) or self._pending_external_release
            if previous is None:
                return
            if not self._motion_event and self._pending_external_release is None:
                self._touches.clear()
                return
            self._pending_external_release = dict(previous)
            self._touches.clear()
            if not self.serial or self.adb_port is None:
                raise ConnectionError("触点释放尚未确认，正在等待原输入通道恢复")
            self._shell(["input", "touchscreen", "motionevent", "UP", previous["x"], previous["y"]], cancel=cancel, timeout=RUNTIME_BOOTSTRAP_CONNECT_TIMEOUT_SECONDS, check=True)
            self._pending_external_release = None

    def _simple_gesture(self, action, cancel=None):
        kind = str(action.get("kind", action.get("action", ""))).lower()
        if kind == "touch":
            points = action.get("pointers", [])
            if len(points) != 1:
                raise ValueError("该输入通道仅支持单指手势")
            point = points[0]
        else:
            point = {"x": action.get("x", action.get("x1")), "y": action.get("y", action.get("y1")), "x2": action.get("x2", action.get("x", action.get("x1"))), "y2": action.get("y2", action.get("y", action.get("y1")))}
        x, y = float(point["x"]), float(point["y"])
        x2, y2 = float(point.get("x2", x)), float(point.get("y2", y))
        if not all(math.isfinite(value) for value in (x, y, x2, y2)):
            raise ValueError("手势坐标必须是有限数")
        x, x2 = (max(0, min(self.width - 1, round(value))) for value in (x, x2))
        y, y2 = (max(0, min(self.height - 1, round(value))) for value in (y, y2))
        duration = float(action.get("ms", action.get("duration_ms", action.get("duration", self.default_action_ms(kind, [point])))))
        if not math.isfinite(duration) or duration < 0:
            raise ValueError("手势时长无效")
        self.release_touches(cancel)
        started = time.monotonic()
        args = ["input", "touchscreen", "tap", x, y] if kind in ("tap", "click") else ["input", "touchscreen", "swipe", x, y, x2, y2, max(1, round(duration))]
        self._shell(args, cancel=cancel, timeout=duration / RUNTIME_MILLISECONDS_PER_SECOND + RUNTIME_BOOTSTRAP_SHELL_TIMEOUT_SECONDS)
        elapsed = time.monotonic() - started
        self.measurements.observe("gesture:" + kind, elapsed)
        return {"submitted": True, "kind": kind, "pointers": 1, "ms": round(elapsed * RUNTIME_MILLISECONDS_PER_SECOND), "input_backend": self._input_backend}

    def _type_text(self, action, cancel=None):
        text = str(action.get("text", ""))
        if not text:
            return {"submitted": False, "kind": "type", "characters": 0}
        if not text.isascii() and not self._existing_unicode_ime:
            raise ValueError("当前设备没有已安装的 Unicode ADB 输入法；未下载或安装输入组件")
        self.release_touches(cancel)
        if "x" in action and "y" in action:
            self.act({"kind": "tap", "x": action["x"], "y": action["y"]}, cancel)
        if self._existing_unicode_ime:
            original, _, _ = self._shell(["settings", "get", "secure", "default_input_method"], cancel=cancel)
            original_ime = original.decode("utf-8", "replace").strip()
            changed = original_ime != "com.android.adbkeyboard/.AdbIME"
            try:
                if changed:
                    self._shell(["ime", "set", "com.android.adbkeyboard/.AdbIME"], cancel=cancel)
                if action.get("clear"):
                    self._shell(["am", "broadcast", "-a", "ADB_CLEAR_TEXT", "-p", "com.android.adbkeyboard"], cancel=cancel)
                payload = base64.b64encode(text.encode("utf-8")).decode("ascii")
                output, error, code = self._shell(["am", "broadcast", "-a", "ADB_INPUT_B64", "-p", "com.android.adbkeyboard", "--es", "msg", payload], cancel=cancel)
                if code:
                    raise RuntimeError((output + error).decode("utf-8", "replace"))
            finally:
                if changed and original_ime and original_ime != "null":
                    self._shell(["ime", "set", original_ime], timeout=RUNTIME_BOOTSTRAP_CONNECT_TIMEOUT_SECONDS, check=False)
        else:
            if any(ord(character) < ord(" ") for character in text):
                raise ValueError("系统文本输入只接受可打印 ASCII 字符")
            if action.get("clear"):
                hierarchy = ET.fromstring(self.hierarchy(cancel, fresh=True))
                focused = next((node for node in hierarchy.iter() if node.get("focused") == "true" and node.get("password") != "true" and "EditText" in node.get("class", "")), None)
                if focused is None:
                    raise ValueError("当前输入框原文不可读取，未猜测清空长度")
                existing = focused.get("text", "")
                if existing:
                    self._shell(["input", "keyevent", "KEYCODE_MOVE_END"], cancel=cancel)
                    for character in existing:
                        self._shell(["input", "keyevent", "KEYCODE_DEL"], cancel=cancel)
            for index, part in enumerate(text.split("%")):
                if index:
                    self._shell(["input", "text", "%"], cancel=cancel)
                if part:
                    self._shell(["input", "text", part.replace(" ", "%s")], cancel=cancel)
        return {"submitted": True, "kind": "type", "characters": len(text)}

    def _sync_push(self, path, remote, cancel=None):
        file = Path(path)
        size = file.stat().st_size
        transfer_seconds = max(RUNTIME_BOOTSTRAP_INSTALL_SECONDS, size / max(1, RUNTIME_BOOTSTRAP_INSTALL_BYTES_PER_SECOND))
        connection, deadline = self._open_adb_stream("sync:", cancel, transfer_seconds)
        try:
            target = (str(remote) + "," + str(ANDROID_SYNC_FILE_MODE)).encode("utf-8")
            self._adb_send_all(connection, ANDROID_SYNC_HEADER.pack(b"SEND", len(target)) + target, deadline, cancel)
            with file.open("rb") as handle:
                while True:
                    check_cancel(cancel)
                    block = handle.read(ANDROID_SYNC_DATA_BYTES)
                    if not block:
                        break
                    self._adb_send_all(connection, ANDROID_SYNC_HEADER.pack(b"DATA", len(block)) + block, deadline, cancel)
            self._adb_send_all(connection, ANDROID_SYNC_HEADER.pack(b"DONE", int(file.stat().st_mtime) & RUNTIME_DWORD_MASK), deadline, cancel)
            status, length = ANDROID_SYNC_HEADER.unpack(self._adb_read(connection, ANDROID_SYNC_HEADER.size, deadline, cancel))
            if status != b"OKAY" or length:
                if status == b"FAIL" and length <= RUNTIME_ADB_INITIAL_PACKET_BYTES:
                    message = self._adb_read(connection, length, deadline, cancel).decode("utf-8", "replace")
                    raise RuntimeError("APK 传输失败：" + message)
                raise RuntimeError("APK 传输未返回有效确认")
            self._adb_send_all(connection, ANDROID_SYNC_HEADER.pack(b"QUIT", 0), deadline, cancel)
        finally:
            self._close_adb_stream(connection)

    @staticmethod
    def _adb_send_all(connection, content, deadline, cancel=None):
        view = memoryview(content)
        while view:
            check_cancel(cancel)
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise TimeoutError("本地 ADB 写入超时")
            connection.settimeout(min(RUNTIME_SOCKET_POLL_SECONDS, remaining))
            try:
                count = connection.send(view)
            except socket.timeout:
                continue
            if count <= 0:
                raise OSError("本地 ADB 连接已关闭")
            view = view[count:]


AI_RGBA_CHANNELS = 4


AI_PNG_PROPERTIES_END = 29


AI_PNG_GRAYSCALE = 0


AI_PNG_TRUECOLOR = 2


AI_PNG_INDEXED = 3


AI_PNG_GRAYSCALE_ALPHA = 4


AI_PNG_TRUECOLOR_ALPHA = 6


AI_PNG_FILTER_SUB = 1


AI_PNG_FILTER_UP = 2


AI_PNG_FILTER_AVERAGE = 3


AI_PNG_FILTER_PAETH = 4


AI_PNG_BITS_PER_CHANNEL = 8


AI_PNG_MIN_IMAGE_BYTES = 45


AI_PNG_PALETTE_MAX_BYTES = 768


AI_COM_RELEASE_VTABLE_INDEX = 2


AI_GDIP_IMAGE_LOCK_READ = 1


AI_GDIP_PIXEL_FORMAT_ARGB = 2498570


AI_INFERENCE_TIMING_SAMPLES = 30


AI_PNG_CHUNK_FRAMING_BYTES = 12


AI_PNG_UINT_BYTES = 4


AI_PNG_CHUNK_HEADER_BYTES = 8


AI_BOUNDING_BOX_COMPONENTS = 4


AI_SPATIAL_DIMENSIONS = 2


AI_HEXADECIMAL_DIGITS_PER_BYTE = 2


AI_PNG_GRAY_ALPHA_CHANNELS = 2


AI_TERMINAL_CONFIRMATION_FRAMES = 2


AI_SAMPLING_NEIGHBOR_RADIUS = 1


AI_BYTES_PER_MEBIBYTE = 1048576


AI_MILLISECONDS_PER_SECOND = 1000


AI_COORDINATE_SCALE = 1000


AI_ANDROID_TAP_INITIAL_MS = 60


AI_ANDROID_LONG_PRESS_INITIAL_MS = 700


AI_ANDROID_SWIPE_INITIAL_MS = 250


AI_ANDROID_WAIT_INITIAL_MS = 250


AI_TEXT_FIELD_LIMIT = 1200


AI_LABEL_FIELD_LIMIT = 120


AI_STATE_FIELD_LIMIT = 320


AI_HASH_PREFIX_BYTES = 12


AI_MEMORY_BUSY_SECONDS = 15


AI_MEMORY_BACKUP_PAGES = 256


AI_MEMORY_BACKUP_YIELD_SECONDS = 0.05


AI_MEMORY_DEFAULT_RECALL = 8


AI_MEMORY_DIAGNOSTIC_LIMIT = 32


AI_MEMORY_EVENT_RECORDS = 50000


AI_MEMORY_TRANSITION_RECORDS = 100000


AI_MEMORY_ARCHIVE_BATCH = 10000


AI_MEMORY_ARCHIVE_FREE_SHARE = 80


AI_MEMORY_ARCHIVE_MAX_BYTES = 1073741824


AI_ACTION_KINDS = ("tap", "long_press", "swipe", "touch", "touch_begin", "touch_update", "touch_end", "touch_release_all", "back", "home", "recents", "enter", "keyevent", "type", "wait")


AI_PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


AI_PNG_END = b"\x00\x00\x00\x00IEND\xaeB`\x82"


AI_PNG_DIMENSION_OFFSET = 16


AI_PNG_DIMENSION_END = 24


AI_PNG_HEADER_BYTES = 33


AI_PNG_MAX_DIMENSION = 8192


AI_RGB_CHANNELS = 3


AI_BYTE_MAX = 255


AI_PERCEPTION_CACHE_FRAMES = 6


AI_PERCEPTION_MAX_SAMPLES = 16384


AI_PERCEPTION_MAX_DECODE_BYTES = 67108864


AI_PRECONDITION_KINDS = ("package", "activity", "visible_text", "node_ref", "node_enabled", "node_state", "active_pointer", "available_pointer")


class AI_OnlineEstimate:
    def __init__(self, state=None):
        state = state if isinstance(state, dict) else {}
        values = (state.get("count", 0), state.get("mean", 0), state.get("m2", 0))
        valid = all(type(value) in (int, float) and math.isfinite(value) and value >= 0 for value in values)
        self.count, self.mean, self.m2 = (int(values[0]), float(values[1]), float(values[2])) if valid else (0, 0.0, 0.0)

    def update(self, value):
        if type(value) not in (int, float) or not math.isfinite(value) or value < 0:
            return False
        self.count += 1
        difference = value - self.mean
        self.mean += difference / self.count
        self.m2 += difference * (value - self.mean)
        return True

    def upper(self, initial):
        if not self.count:
            return initial
        variance = self.m2 / max(1, self.count - 1)
        return self.mean + math.sqrt(max(0.0, variance)) + self.mean / math.sqrt(self.count)

    def state(self):
        return {"count": self.count, "mean": self.mean, "m2": self.m2}


def AI_node_reference(node):
    identity = local_agent_node_key(node)
    duplicate_order = node.get("_agent_duplicate_order")
    if type(duplicate_order) is int and duplicate_order >= 0:
        identity = hashlib.sha256((identity + ":" + str(duplicate_order)).encode("ascii")).hexdigest()
    return "node:" + identity[:AI_HASH_PREFIX_BYTES * AI_HEXADECIMAL_DIGITS_PER_BYTE]


def AI_disambiguate_nodes(nodes):
    result = [dict(node) for node in nodes if isinstance(node, dict)]
    grouped = collections.defaultdict(list)
    for node in result:
        node.pop("_agent_duplicate_order", None)
        grouped[local_agent_node_key(node)].append(node)
    for duplicates in grouped.values():
        if len(duplicates) < AI_SPATIAL_DIMENSIONS:
            continue
        ordered = sorted(duplicates, key=lambda node: (tuple(node.get("bounds", ())), str(node.get("tree_path", ""))))
        for index, node in enumerate(ordered):
            node["_agent_duplicate_order"] = index
    return result


def local_agent_legacy_node_key(node):
    resource = str(node.get("resource_id") or node.get("id") or "").strip()
    label = local_agent_label(node.get("text") or node.get("content_desc") or node.get("description") or "")
    label = re.sub(r"[-+]?\d+(?:\.\d+)?", "#", label)
    identity = (resource, str(node.get("class", "")), label, str(node.get("tree_path", "")))
    payload = json.dumps(identity, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def AI_legacy_node_reference(node):
    return "node:" + local_agent_legacy_node_key(node)[:AI_HASH_PREFIX_BYTES * AI_HEXADECIMAL_DIGITS_PER_BYTE]


def AI_matching_nodes(nodes, reference):
    matching = [node for node in nodes if isinstance(node, dict) and reference in (AI_node_reference(node), AI_legacy_node_reference(node))]
    if len(matching) == 1:
        return matching
    return [node for node in AI_disambiguate_nodes(nodes) if reference in (AI_node_reference(node), AI_legacy_node_reference(node))]


def AI_visible_text(observation):
    labels = []
    for node in observation.get("nodes", []):
        if isinstance(node, dict):
            labels.extend(str(node.get(name, "")) for name in ("text", "content_desc", "description"))
    return "\n".join(value.strip() for value in labels if value.strip()).casefold()


AI_CONTEXT_CJK_WINDOW_MIN = 2


AI_CONTEXT_CJK_WINDOW_MAX = 3


def AI_context_tokens(features):
    values = [features.get("objective", ""), features.get("situation", ""), features.get("mode", ""), features.get("turn", "")]
    values.extend(features.get("anchors", []) if isinstance(features.get("anchors"), list) else [])
    tokens = set()
    for segment in re.findall(r"[\u4e00-\u9fff]+|[^\W\u4e00-\u9fff]+", " ".join(str(value) for value in values).casefold()):
        if not "\u4e00" <= segment[0] <= "\u9fff":
            tokens.add(segment)
            continue
        if len(segment) < AI_CONTEXT_CJK_WINDOW_MIN:
            tokens.add(segment)
        for width in range(AI_CONTEXT_CJK_WINDOW_MIN, AI_CONTEXT_CJK_WINDOW_MAX + 1):
            tokens.update(segment[index:index + width] for index in range(max(0, len(segment) - width + 1)))
    return tokens


def AI_context_similarity(first, second):
    if str(first.get("phase", "unknown")) != str(second.get("phase", "unknown")):
        return 0.0
    left, right = AI_context_tokens(first), AI_context_tokens(second)
    if not left or not right:
        return 0.0
    return len(left & right) / len(left | right)


def AI_posterior(successes, failures):
    alpha = max(0.0, successes) + 1
    beta = max(0.0, failures) + 1
    total = alpha + beta
    probability = alpha / total
    deviation = math.sqrt(alpha * beta / (total * total * (total + 1)))
    return probability, deviation


def AI_action_identity(action):
    return json.dumps(action_signature(action), ensure_ascii=False, sort_keys=True, separators=(",", ":"))


import heapq


LOCAL_AGENT_SCHEMA_VERSION = 1
LOCAL_AGENT_HOEFFDING_FACTOR = 2
LOCAL_AGENT_COLOR_LEVELS = math.isqrt(AI_BYTE_MAX + 1)
LOCAL_AGENT_HALTON_BASES = (2, 3)
LOCAL_AGENT_DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
LOCAL_AGENT_WIN_LABELS = frozenset(("victory", "you win", "you won", "winner", "victory royale", "战斗胜利", "对局胜利", "游戏胜利", "胜利", "获胜", "挑战成功"))
LOCAL_AGENT_LOSS_LABELS = frozenset(("defeat", "you lose", "you lost", "defeated", "战斗失败", "对局失败", "游戏失败", "失败", "挑战失败"))
LOCAL_AGENT_LOADING_LABELS = frozenset(("loading", "please wait", "正在加载", "加载中", "请稍候", "正在连接"))
LOCAL_AGENT_SELF_TURN_LABELS = frozenset(("your turn", "your move", "your round", "你的回合", "轮到你了", "请出牌", "轮到我方", "该你出牌", "你来行动"))
LOCAL_AGENT_OTHER_TURN_LABELS = frozenset(("opponent's turn", "enemy turn", "waiting for opponent", "对方回合", "等待对手", "对手出牌中", "等待其他玩家", "等待对方出牌", "敌方回合"))
LOCAL_AGENT_NAVIGATION_LABELS = frozenset(("play", "start", "start game", "play game", "continue", "next", "retry", "restart", "play again", "resume", "resume game", "开始", "开始游戏", "进入游戏", "继续", "继续游戏", "下一步", "重试", "重新开始", "再来一局", "再来一次", "返回游戏", "确定"))
LOCAL_AGENT_SCORE_NAMES = frozenset(("score", "points", "current_score", "game_score", "player_score", "得分", "分数", "本局得分", "当前得分", "我的得分", "我方得分", "我的分数", "我方分数", "玩家得分", "玩家分数", "本局积分", "当前积分"))
LOCAL_AGENT_LIMITATION = "单文件离线视觉、原生控件和跨场景在线学习；尚不能无监督理解所有游戏规则与胜负语义，复杂游戏和竞技水平需真机评测。"
AI_VISION_GRID_MULTIPLIER = math.isqrt(AI_RGBA_CHANNELS)
AI_VISION_STATE_LEVELS = math.isqrt(LOCAL_AGENT_COLOR_LEVELS)
AI_VISION_MIN_REGION_CELLS = AI_SPATIAL_DIMENSIONS
AI_VISION_REGION_AREA_LIMIT = 1 / AI_RGBA_CHANNELS
AI_VISION_MAX_REGIONS = math.isqrt(AI_PERCEPTION_MAX_SAMPLES)
AI_VISION_REGION_SPACING = AI_SAMPLING_NEIGHBOR_RADIUS
AI_VISION_NEIGHBORS = LOCAL_AGENT_DIRECTIONS + tuple((dx, dy) for dx in (-AI_VISION_REGION_SPACING, AI_VISION_REGION_SPACING) for dy in (-AI_VISION_REGION_SPACING, AI_VISION_REGION_SPACING))
AI_VISUAL_FEEDBACK_WEIGHT = 1 / AI_RGB_CHANNELS
AI_VISUAL_CONTROL_PRIOR = 1 / AI_SPATIAL_DIMENSIONS
LOCAL_AGENT_AFFORDANCE_GRID = LOCAL_AGENT_COLOR_LEVELS
LOCAL_AGENT_AFFORDANCE_WEIGHT = AI_VISUAL_FEEDBACK_WEIGHT
LOCAL_AGENT_AFFORDANCE_RECALL = AI_MEMORY_DEFAULT_RECALL * AI_SPATIAL_DIMENSIONS
LOCAL_AGENT_SMART_OVERLAY_LIMIT = AI_MEMORY_DEFAULT_RECALL * AI_SPATIAL_DIMENSIONS
LOCAL_AGENT_ATTENTION_PER_QUADRANT = AI_SPATIAL_DIMENSIONS
LOCAL_AGENT_EFFECT_MINIMUM = 1 / AI_BYTE_MAX
LOCAL_AGENT_PLANNING_BACKUP_LIMIT = AI_MEMORY_DEFAULT_RECALL * AI_SPATIAL_DIMENSIONS
LOCAL_AGENT_PLANNING_STALE_RATIO = AI_RGBA_CHANNELS
LOCAL_AGENT_CANDIDATE_EXPLORATION_LIMIT = LOCAL_AGENT_SMART_OVERLAY_LIMIT
LOCAL_AGENT_TERMINAL_TEMPLATE_MIN_EPISODES = AI_SPATIAL_DIMENSIONS
LOCAL_AGENT_TERMINAL_TEMPLATE_SIMILARITY = 1 - 1 / (AI_RGB_CHANNELS * LOCAL_AGENT_COLOR_LEVELS)
LOCAL_AGENT_TERMINAL_TEMPLATE_RECALL = AI_MEMORY_DEFAULT_RECALL * AI_SPATIAL_DIMENSIONS
LOCAL_AGENT_TERMINAL_TEMPLATE_MARGIN = LOCAL_AGENT_EFFECT_MINIMUM
LOCAL_AGENT_PROGRESS_DIRECTIONS = {
    "我方击杀": 1, "击杀数": 1, "player_kills": 1, "my_kills": 1,
    "我方推塔": 1, "已摧毁防御塔": 1, "towers_destroyed": 1,
    "星数": 1, "获得星星": 1, "earned_stars": 1,
    "已占领据点": 1, "captured_outposts": 1,
    "剩余敌方防御塔": -1, "enemy_towers_remaining": -1,
}
LOCAL_AGENT_GAME_SIGNATURES = (
    ("honor_of_kings", ("sgame", "honorofkings")),
    ("clash_of_clans", ("clashofclans",)),
    ("clash_royale", ("clashroyale",)),
    ("boom_beach", ("boombeach",)),
    ("minecraft", ("minecraftpe", "survivalcraft")),
    ("million_lords", ("millionlords",)),
    ("happy_poker", ("hlddz", "dou_dizhu", "doudizhu", "landlords")),
    ("art_of_war_3", ("geargames.aow", "artofwar3")),
)
LOCAL_AGENT_GAME_OBJECTIVES = {
    "honor_of_kings": "观察操作区、我方状态和可核实的战斗目标",
    "clash_of_clans": "区分基地界面、部署区和可核实的战斗结果",
    "clash_royale": "区分手牌、战场部署区和可核实的对局结果",
    "boom_beach": "区分部队部署、战场与结果界面",
    "minecraft": "区分视角、移动和交互控制，并记录可验证结果",
    "million_lords": "区分单位、领地和战略部署操作",
    "happy_poker": "优先识别手牌、出牌控件、回合与对局结果",
    "art_of_war_3": "区分单位选择、移动和战场目标",
}


def local_agent_number(value, default=0.0):
    return float(value) if type(value) in (int, float) and math.isfinite(value) else float(default)


def local_agent_label(value):
    return re.sub(r"\s+", " ", str(value)).strip().strip("!！。.:：").casefold()


def local_agent_node_key(node):
    resource = str(node.get("resource_id") or node.get("id") or "").strip()
    category = str(node.get("class", ""))
    label = local_agent_label(node.get("text") or node.get("content_desc") or node.get("description") or "")
    label = re.sub(r"[-+]?\d+(?:\.\d+)?", "#", label)
    identity = (resource, category, label) if resource or label else (category, str(node.get("tree_path", "")))
    return hashlib.sha256(json.dumps(identity, ensure_ascii=False, separators=(",", ":")).encode("utf-8")).hexdigest()


def local_agent_ui_target(node, nodes):
    labels = [str(node.get(name) or "").strip() for name in ("text", "content_desc", "description")]
    labels = list(dict.fromkeys(label for label in labels if label))
    if not labels:
        path = str(node.get("tree_path") or "")
        bounds = node.get("bounds", ())
        if path and len(bounds) == AI_BOUNDING_BOX_COMPONENTS:
            left, top, right, bottom = bounds
            for child in nodes:
                if child.get("clickable") is True or not str(child.get("tree_path") or "").startswith(path + "/"):
                    continue
                child_bounds = child.get("bounds", ())
                if not isinstance(child_bounds, (list, tuple)) or len(child_bounds) != AI_BOUNDING_BOX_COMPONENTS or any(type(value) is not int for value in child_bounds):
                    continue
                if not left <= child_bounds[0] < child_bounds[2] <= right or not top <= child_bounds[1] < child_bounds[3] <= bottom:
                    continue
                labels.extend(str(child.get(name) or "").strip() for name in ("text", "content_desc", "description") if str(child.get(name) or "").strip())
            labels = list(dict.fromkeys(labels))
    resource = str(node.get("resource_id") or node.get("id") or "").rsplit("/", 1)[-1]
    resource_label = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", resource)
    resource_label = local_agent_label(re.sub(r"[_\-]+", " ", resource_label))
    resource_label = re.sub(r"^(?:button|btn|action|menu)\s+", "", resource_label)
    evidence = next((label for label in labels if local_agent_label(label) in LOCAL_AGENT_NAVIGATION_LABELS), "")
    return {"label": " · ".join(labels) if labels else resource or "可点击控件", "navigation": bool(evidence) or resource_label in LOCAL_AGENT_NAVIGATION_LABELS, "evidence": evidence, "semantic": bool(labels)}


def local_agent_absolute_action(action, size):
    if not isinstance(action, dict) or not isinstance(size, (list, tuple)) or len(size) != AI_SPATIAL_DIMENSIONS:
        raise ValueError("已学控制缺少有效坐标")
    result = dict(action)
    for key in ("x", "x2", "y", "y2"):
        if key not in result:
            continue
        value = result[key]
        if type(value) not in (int, float) or not math.isfinite(value) or not 0 <= value <= AI_COORDINATE_SCALE:
            raise ValueError("已学控制坐标无效")
        extent = size[0] if key.startswith("x") else size[1]
        if type(extent) is not int or extent <= 0:
            raise ValueError("已学控制画面尺寸无效")
        result[key] = round(value * (extent - 1) / AI_COORDINATE_SCALE)
    if "pointers" in result:
        if not isinstance(result["pointers"], list):
            raise ValueError("已学控制触点格式无效")
        result["pointers"] = [local_agent_absolute_action(point, size) for point in result["pointers"]]
    return result


def local_agent_halton(index, base):
    fraction = 1.0
    value = 0.0
    while index:
        index, remainder = divmod(index, base)
        fraction /= base
        value += fraction * remainder
    return value


LOCAL_AGENT_TIMED_ACTIONS = frozenset(("long_press", "swipe", "touch", "touch_begin", "touch_update"))
LOCAL_AGENT_DURATION_QUANTUM_MS = AI_ANDROID_TAP_INITIAL_MS


def local_agent_learning_signature(action, node=None):
    signature = action_signature(action)
    if not isinstance(signature, dict):
        raise ValueError("学习动作签名必须是对象")
    kind = signature.get("kind")
    milliseconds = signature.pop("ms", None)
    if kind in LOCAL_AGENT_TIMED_ACTIONS and type(milliseconds) in (int, float) and math.isfinite(milliseconds) and milliseconds >= 0:
        signature["duration_ticks"] = max(1, round(milliseconds / LOCAL_AGENT_DURATION_QUANTUM_MS))
    if node is not None:
        identity = {"kind": kind, "node": local_agent_node_key(node)}
        duplicate_order = node.get("_agent_duplicate_order")
        if type(duplicate_order) is int and duplicate_order >= 0:
            identity["duplicate_order"] = duplicate_order
        if "duration_ticks" in signature:
            identity["duration_ticks"] = signature["duration_ticks"]
        return identity
    return signature


def local_agent_memory_action_key(action):
    grid = math.isqrt(AI_COORDINATE_SCALE)
    def compact(value):
        if isinstance(value, dict):
            result = {key: round(number * grid / AI_COORDINATE_SCALE) if key in {"x", "y", "x2", "y2"} and type(number) in (int, float) and math.isfinite(number) else compact(number) for key, number in value.items() if key not in {"ms", "note", "target", "repeat", "interval_ms", "text_redacted", "text_length"}}
            milliseconds = value.get("ms")
            if value.get("kind") in LOCAL_AGENT_TIMED_ACTIONS and type(milliseconds) in (int, float) and math.isfinite(milliseconds) and milliseconds >= 0:
                result["duration_ticks"] = max(1, round(milliseconds / LOCAL_AGENT_DURATION_QUANTUM_MS))
            return result
        if isinstance(value, list):
            return [compact(item) for item in value]
        return value
    return json.dumps(compact(action), ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def local_agent_restore_action(relative, conditions, observation):
    if not isinstance(relative, dict) or not isinstance(conditions, list):
        raise ValueError("已存学习动作内容无效")
    size = observation.get("size", (observation.get("width"), observation.get("height")))
    action = local_agent_absolute_action(relative, size)
    references = [condition.get("value") for condition in conditions if isinstance(condition, dict) and condition.get("kind") == "node_enabled"]
    if len(references) > 1:
        raise ValueError("已存控件绑定不是唯一目标")
    if references:
        reference = references[0]
        matches = AI_matching_nodes(observation.get("nodes", ()), reference)
        if len(matches) != 1:
            raise ValueError("已存控件不在当前画面")
        action["target"] = reference
    return normalize_action(action, observation)


LOCAL_AGENT_RECURRENT_STATES = AI_MEMORY_DEFAULT_RECALL * AI_MEMORY_DEFAULT_RECALL
LOCAL_AGENT_RECURRENT_SIMILARITY = 0.96
LOCAL_AGENT_PROFILE_PRIOR = 0.85
LOCAL_AGENT_PROFILE_SECONDARY_PRIOR = LOCAL_AGENT_PROFILE_PRIOR / AI_SPATIAL_DIMENSIONS
LOCAL_AGENT_PROFILE_TOUCH_FRACTION = AI_COORDINATE_SCALE
LOCAL_AGENT_EFFECT_NEIGHBOR_DIVISOR = 12
LOCAL_AGENT_EFFECT_AMBIENT_SHARE = 1 / AI_SPATIAL_DIMENSIONS
LOCAL_AGENT_EFFECT_ATTENUATION = 1 / AI_RGB_CHANNELS
LOCAL_AGENT_REWARD_EXPLORATION_ATTENUATION = 1 / AI_SPATIAL_DIMENSIONS
LOCAL_AGENT_DEMONSTRATION_PRIOR = LOCAL_AGENT_PROFILE_PRIOR * AI_SPATIAL_DIMENSIONS
LOCAL_AGENT_MANUAL_DRAG_FRACTION = 0.03
LOCAL_AGENT_GENRE_SIGNATURES = (
    ("moba", ("sgame", "honorofkings", "mobilelegends", "wildrift", "arenaofvalor")),
    ("card_battle", ("clashroyale", "royale", "cardbattle")),
    ("sandbox", ("minecraftpe", "minecraft", "survivalcraft")),
    ("cards", ("doudizhu", "dou_dizhu", "hlddz", "ddz", "landlords", "poker")),
    ("strategy", ("clashofclans", "boombeach", "millionlords", "artofwar3", "geargames.aow", "strategy")),
)
LOCAL_AGENT_GENRE_LABELS = {
    "moba": "实时竞技与虚拟摇杆", "realtime": "实时双区触控", "card_battle": "卡牌拖放竞技",
    "sandbox": "沙盒与视角控制", "cards": "回合式卡牌", "strategy": "策略与单位部署", "generic": "通用未知玩法",
}
LOCAL_AGENT_GENRE_ANCHORS = {
    "moba": {"move": (180, 790), "action": (850, 800), "center": (500, 480)},
    "realtime": {"move": (180, 790), "action": (850, 800), "center": (500, 480)},
    "sandbox": {"move": (190, 780), "action": (870, 760), "center": (520, 440)},
    "card_battle": {"hand": (460, 875), "arena": (490, 420), "action": (810, 865)},
    "cards": {"hand": (490, 855), "action": (840, 765), "center": (480, 540)},
    "strategy": {"unit": (380, 635), "target": (630, 405), "center": (500, 500)},
}
LOCAL_AGENT_GENRE_MOTION_DIRECTIONS = LOCAL_AGENT_DIRECTIONS
LOCAL_AGENT_UI_HYPOTHESIS_SPAN = 90
LOCAL_AGENT_GAME_INTENTS = {
    "cards": (("出牌", "play cards", "submit cards", "确认出牌"), ("提示", "hint", "选择", "select")),
    "card_battle": (("部署", "deploy", "使用卡牌", "play card"), ("下一步", "next")),
    "strategy": (("攻击", "attack", "采集", "collect", "训练", "train"), ("建造", "build", "升级", "upgrade")),
    "moba": (("升级技能", "level up", "增加技能", "learn skill"), ("技能", "skill", "攻击", "attack")),
    "realtime": (("攻击", "attack", "射击", "fire"), ("技能", "skill")),
    "sandbox": (("交互", "interact", "合成", "craft", "挖掘", "mine"), ("背包", "inventory", "放置", "place")),
}
LOCAL_AGENT_SEMANTIC_BONUS = LOCAL_AGENT_PROFILE_PRIOR / AI_SPATIAL_DIMENSIONS


def local_agent_game_profile(descriptor):
    package = str(descriptor.get("package", "")).casefold()
    genre = "generic"
    identified_by = "unclassified_gameplay"
    for candidate, signatures in LOCAL_AGENT_GENRE_SIGNATURES:
        if any(token in package for token in signatures):
            genre, identified_by = candidate, "package_layout_hint"
            break
    game_id = next((name for name, tokens in LOCAL_AGENT_GAME_SIGNATURES if any(token in package for token in tokens)), "unclassified")
    width, height = descriptor["size"]
    regions = [item for item in descriptor.get("regions", ()) if isinstance(item, dict)]
    movement = [item for item in regions if item.get("kind") == "movement_control" and item.get("x", width) < width / AI_SPATIAL_DIMENSIONS]
    actions = [item for item in regions if item.get("kind") == "action_control" and item.get("x", 0) >= width / AI_SPATIAL_DIMENSIONS]
    if genre == "generic" and movement and actions and descriptor.get("phase") in {"playing", "unknown"}:
        genre, identified_by = "realtime", "visual_control_regions"
    anchors = dict(LOCAL_AGENT_GENRE_ANCHORS.get(genre, {}))
    dynamic_targets = (("move", movement), ("action", actions)) if genre in {"moba", "realtime", "sandbox"} else ()
    if genre in {"cards", "card_battle"}:
        hand_regions = [item for item in regions if item.get("kind") in {"visual_target", "action_control"} and item.get("y", 0) >= height * (AI_SPATIAL_DIMENSIONS / AI_RGB_CHANNELS)]
        dynamic_targets = (("hand", hand_regions),)
    if genre == "strategy":
        unit_regions = [item for item in regions if item.get("kind") in {"visual_target", "action_control"} and item.get("y", 0) >= height / AI_SPATIAL_DIMENSIONS]
        dynamic_targets = (("unit", unit_regions),)
    for key, candidates in dynamic_targets:
        if candidates:
            selected = max(candidates, key=lambda item: local_agent_number(item.get("strength")) + local_agent_number(item.get("motion")))
            anchors[key] = (round(selected["x"] * LOCAL_AGENT_PROFILE_TOUCH_FRACTION / max(1, width - 1)), round(selected["y"] * LOCAL_AGENT_PROFILE_TOUCH_FRACTION / max(1, height - 1)))
            if identified_by == "package_layout_hint":
                identified_by = "package_hint_plus_visual_regions"
    annotations = []
    if descriptor.get("phase") == "playing":
        names = {"move": "移动控制候选", "action": "技能/操作区候选", "hand": "卡牌区域候选", "arena": "部署区域候选", "center": "视角/交互区域候选", "unit": "单位区域候选", "target": "目标区域候选"}
        for role, (rx, ry) in anchors.items():
            x = round(rx * (width - 1) / LOCAL_AGENT_PROFILE_TOUCH_FRACTION)
            y = round(ry * (height - 1) / LOCAL_AGENT_PROFILE_TOUCH_FRACTION)
            radius_x = max(1, width * LOCAL_AGENT_UI_HYPOTHESIS_SPAN // LOCAL_AGENT_PROFILE_TOUCH_FRACTION)
            radius_y = max(1, height * LOCAL_AGENT_UI_HYPOTHESIS_SPAN // LOCAL_AGENT_PROFILE_TOUCH_FRACTION)
            annotations.append({"source": "layout_hypothesis", "kind": "control_hypothesis", "bounds": [max(0, x - radius_x), max(0, y - radius_y), min(width, x + radius_x), min(height, y + radius_y)], "x": x, "y": y, "label": names.get(role, "操作区域候选"), "role": role})
    return {"genre": genre, "game_id": game_id, "objective": LOCAL_AGENT_GAME_OBJECTIVES.get(game_id, "从可验证画面反馈中学习操作效果"), "label": LOCAL_AGENT_GENRE_LABELS[genre], "evidence": identified_by, "anchors": anchors, "annotations": annotations, "rule_understood": False}


def local_agent_semantic_actions(descriptor):
    if descriptor.get("phase") != "playing" or descriptor.get("turn") == "opponent":
        return []
    profile = descriptor.get("profile", {})
    genre = profile.get("genre", "generic")
    intents = LOCAL_AGENT_GAME_INTENTS.get(genre, ())
    if not intents:
        return []
    width, height = descriptor["size"]
    candidates = []
    selected_cards = any(node.get("selected") is True for node in descriptor.get("nodes", ()) if isinstance(node, dict))
    for node in descriptor.get("clickable", ()):
        label = local_agent_label(node.get("text") or node.get("content_desc") or "")
        resource = local_agent_label(str(node.get("resource_id") or node.get("id") or "").rsplit("/", 1)[-1].replace("_", " "))
        if not label and not resource:
            continue
        for priority, group in enumerate(intents):
            if label in group or resource in group:
                bounds = node["bounds"]
                x, y = (bounds[0] + bounds[2] - 1) // AI_SPATIAL_DIMENSIONS, (bounds[1] + bounds[3] - 1) // AI_SPATIAL_DIMENSIONS
                prior = LOCAL_AGENT_PROFILE_PRIOR + LOCAL_AGENT_SEMANTIC_BONUS / (priority + 1)
                if genre == "cards" and label in {"出牌", "play cards", "submit cards", "确认出牌"} and not selected_cards:
                    prior = LOCAL_AGENT_PROFILE_SECONDARY_PRIOR
                candidates.append(({"kind": "tap", "x": x, "y": y}, "游戏专用可访问控件 · " + (label or resource), prior, node))
                break
    if genre == "cards" and descriptor.get("turn") == "self" and not selected_cards:
        for node in descriptor.get("clickable", ()):
            bounds = node["bounds"]
            if node.get("selected") is True or bounds[1] < height * AI_RGB_CHANNELS // AI_RGBA_CHANNELS:
                continue
            target = descriptor.get("targets", {}).get(AI_node_reference(node), {})
            if target.get("navigation"):
                continue
            label = local_agent_label(node.get("text") or node.get("content_desc") or "")
            if not label or label in LOCAL_AGENT_NAVIGATION_LABELS:
                continue
            x, y = (bounds[0] + bounds[2] - 1) // AI_SPATIAL_DIMENSIONS, (bounds[1] + bounds[3] - 1) // AI_SPATIAL_DIMENSIONS
            candidates.append(({"kind": "tap", "x": x, "y": y}, "本回合尝试选择未选中的可见手牌", LOCAL_AGENT_PROFILE_PRIOR, node))
    return candidates


def local_agent_profile_actions(descriptor, observation):
    profile = descriptor.get("profile") or local_agent_game_profile(descriptor)
    genre = profile["genre"]
    if descriptor.get("phase") != "playing" or genre == "generic":
        return []
    width, height = descriptor["size"]
    available = set(observation.get("capabilities", {}).get("actions", AI_ACTION_KINDS))
    active_points = {item["id"]: item for item in observation.get("active_touches", []) if isinstance(item, dict) and type(item.get("id")) is int and all(type(item.get(key)) is int for key in ("x", "y"))}
    active = set(active_points)
    count = int(local_agent_number(observation.get("capabilities", {}).get("continuous_touch_slots"), 0))
    free = next((number for number in range(count) if number not in active), None)
    cadence = GameAI._cadence(observation)
    ms = max(1, math.ceil(cadence * AI_MILLISECONDS_PER_SECOND))
    anchors = profile["anchors"]
    points = {key: (round(raw[0] * (width - 1) / LOCAL_AGENT_PROFILE_TOUCH_FRACTION), round(raw[1] * (height - 1) / LOCAL_AGENT_PROFILE_TOUCH_FRACTION)) for key, raw in anchors.items()}
    proposals = []
    def add(action, label, prior=LOCAL_AGENT_PROFILE_PRIOR):
        if action["kind"] in available:
            proposals.append((action, label, prior))
    if genre in {"moba", "realtime", "sandbox"}:
        x, y = points["move"]
        if not active and free is not None:
            add({"kind": "touch_begin", "pointers": [{"id": free, "x": x, "y": y}], "ms": ms}, "尝试虚拟摇杆持续控制")
        held = next((point for point in active_points.values() if abs(point["x"] - x) <= width // (AI_RGBA_CHANNELS * AI_SPATIAL_DIMENSIONS) and abs(point["y"] - y) <= height // (AI_RGBA_CHANNELS * AI_SPATIAL_DIMENSIONS)), None)
        if held is not None:
            step_x = max(1, width // (AI_RGB_CHANNELS * AI_RGBA_CHANNELS))
            step_y = max(1, height // (AI_RGB_CHANNELS * AI_RGBA_CHANNELS))
            for dx, dy in LOCAL_AGENT_GENRE_MOTION_DIRECTIONS:
                add({"kind": "touch_update", "pointers": [{"id": held["id"], "x": held["x"], "y": held["y"], "x2": max(0, min(width - 1, x + dx * step_x)), "y2": max(0, min(height - 1, y + dy * step_y))}], "ms": ms * AI_SPATIAL_DIMENSIONS}, "保持摇杆并探索可验证的移动方向", LOCAL_AGENT_PROFILE_SECONDARY_PRIOR)
        for dx, dy in LOCAL_AGENT_GENRE_MOTION_DIRECTIONS:
            step_x = max(1, width // (AI_RGB_CHANNELS * AI_RGB_CHANNELS))
            step_y = max(1, height // (AI_RGB_CHANNELS * AI_RGB_CHANNELS))
            add({"kind": "swipe", "x": x, "y": y, "x2": max(0, min(width - 1, x + dx * step_x)), "y2": max(0, min(height - 1, y + dy * step_y)), "ms": ms * AI_SPATIAL_DIMENSIONS}, "尝试移动方向", LOCAL_AGENT_PROFILE_SECONDARY_PRIOR)
        if "action" in points:
            x, y = points["action"]
            add({"kind": "tap", "x": x, "y": y, "ms": ms}, "尝试右侧操作区")
        if "center" in points and genre == "sandbox":
            x, y = points["center"]
            dx = max(1, width // AI_RGB_CHANNELS)
            add({"kind": "swipe", "x": x, "y": y, "x2": min(width - 1, x + dx), "y2": y, "ms": ms * AI_SPATIAL_DIMENSIONS}, "尝试调整视角")
    elif genre == "card_battle":
        sx, sy = points["hand"]
        tx, ty = points["arena"]
        for dx, dy in LOCAL_AGENT_GENRE_MOTION_DIRECTIONS:
            x = max(0, min(width - 1, sx + dx * width // (AI_RGB_CHANNELS * AI_RGB_CHANNELS)))
            destination = max(0, min(width - 1, tx + dx * width // (AI_RGB_CHANNELS * AI_RGB_CHANNELS)))
            add({"kind": "swipe", "x": x, "y": sy, "x2": destination, "y2": ty, "ms": ms * AI_SPATIAL_DIMENSIONS}, "尝试卡牌拖放到场上", LOCAL_AGENT_PROFILE_PRIOR)
        add({"kind": "tap", "x": sx, "y": sy, "ms": ms}, "尝试选择手牌", LOCAL_AGENT_PROFILE_SECONDARY_PRIOR)
    elif genre == "cards":
        x, y = points["hand"]
        for dx, dy in LOCAL_AGENT_GENRE_MOTION_DIRECTIONS:
            add({"kind": "tap", "x": max(0, min(width - 1, x + dx * width // (AI_RGB_CHANNELS * AI_RGB_CHANNELS))), "y": y, "ms": ms}, "尝试选择一张手牌")
        x, y = points["action"]
        add({"kind": "tap", "x": x, "y": y, "ms": ms}, "尝试操作按钮", LOCAL_AGENT_PROFILE_SECONDARY_PRIOR)
    elif genre == "strategy":
        x, y = points["unit"]
        tx, ty = points["target"]
        add({"kind": "tap", "x": x, "y": y, "ms": ms}, "尝试选择场景单位")
        add({"kind": "tap", "x": tx, "y": ty, "ms": ms}, "尝试部署或指定战场目标", LOCAL_AGENT_PROFILE_SECONDARY_PRIOR)
        add({"kind": "swipe", "x": x, "y": y, "x2": tx, "y2": ty, "ms": ms * AI_SPATIAL_DIMENSIONS}, "尝试单位部署或地图拖动")
    game_id = profile.get("game_id")
    if game_id == "honor_of_kings" and count >= AI_SPATIAL_DIMENSIONS and not active and "move" in points and "action" in points:
        mx, my = points["move"]
        ax, ay = points["action"]
        add({"kind": "touch", "pointers": [{"id": 0, "x": mx, "y": my}, {"id": 1, "x": ax, "y": ay}], "ms": ms}, "同步探索移动与技能控制", LOCAL_AGENT_PROFILE_SECONDARY_PRIOR)
    elif game_id in {"clash_of_clans", "boom_beach"} and "unit" in points and "target" in points:
        sx, sy = points["unit"]
        tx, ty = points["target"]
        for dx, dy in LOCAL_AGENT_GENRE_MOTION_DIRECTIONS:
            x = max(0, min(width - 1, tx + dx * width // (AI_RGB_CHANNELS * AI_RGBA_CHANNELS)))
            y = max(0, min(height - 1, ty + dy * height // (AI_RGB_CHANNELS * AI_RGBA_CHANNELS)))
            add({"kind": "tap", "x": x, "y": y, "ms": ms}, "尝试分区部署并观察部队响应", LOCAL_AGENT_PROFILE_SECONDARY_PRIOR)
            add({"kind": "swipe", "x": sx, "y": sy, "x2": x, "y2": y, "ms": ms * AI_SPATIAL_DIMENSIONS}, "尝试分区拖动部署", LOCAL_AGENT_PROFILE_SECONDARY_PRIOR)
    elif game_id == "clash_royale" and "hand" in points and "arena" in points:
        sx, sy = points["hand"]
        tx, ty = points["arena"]
        for delta in (-1, 1):
            x = max(0, min(width - 1, tx + delta * width // (AI_RGB_CHANNELS * AI_SPATIAL_DIMENSIONS)))
            add({"kind": "swipe", "x": sx, "y": sy, "x2": x, "y2": ty, "ms": ms * AI_SPATIAL_DIMENSIONS}, "尝试左右战场卡牌部署", LOCAL_AGENT_PROFILE_SECONDARY_PRIOR)
    elif game_id == "minecraft" and "center" in points:
        x, y = points["center"]
        add({"kind": "long_press", "x": x, "y": y, "ms": max(ms, math.ceil(local_agent_number(observation.get("capabilities", {}).get("long_press_ms"), AI_ANDROID_LONG_PRESS_INITIAL_MS)))}, "尝试持续交互并检查世界变化", LOCAL_AGENT_PROFILE_SECONDARY_PRIOR)
    elif game_id in {"million_lords", "art_of_war_3"} and "unit" in points and "target" in points:
        x, y = points["unit"]
        tx, ty = points["target"]
        add({"kind": "long_press", "x": x, "y": y, "ms": max(ms, math.ceil(local_agent_number(observation.get("capabilities", {}).get("long_press_ms"), AI_ANDROID_LONG_PRESS_INITIAL_MS)))}, "尝试选中单位或集结部队", LOCAL_AGENT_PROFILE_SECONDARY_PRIOR)
        add({"kind": "swipe", "x": x, "y": y, "x2": tx, "y2": ty, "ms": ms * AI_RGB_CHANNELS}, "尝试单位向目标区域移动", LOCAL_AGENT_PROFILE_SECONDARY_PRIOR)
    elif game_id == "happy_poker" and "hand" in points:
        x, y = points["hand"]
        for delta in (-1, 1):
            candidate_x = max(0, min(width - 1, x + delta * width // (AI_RGB_CHANNELS * AI_RGBA_CHANNELS)))
            add({"kind": "tap", "x": candidate_x, "y": y, "ms": ms}, "尝试选择其他手牌并等待明确回合反馈", LOCAL_AGENT_PROFILE_SECONDARY_PRIOR)
    return proposals


def local_agent_action_focus(first, second, size, action):
    if not first or not second or len(first) != len(second):
        return None
    width, height = size
    columns, rows = vision_sample_grid(width, height)
    if len(first) != columns * rows:
        return None
    points = []
    if "x" in action and "y" in action:
        points.append((action["x"], action["y"]))
        if "x2" in action and "y2" in action:
            points.append((action["x2"], action["y2"]))
    for pointer in action.get("pointers", ()): 
        if isinstance(pointer, dict) and "x" in pointer and "y" in pointer:
            points.append((pointer["x"], pointer["y"]))
    if not points:
        return None
    radius = max(1, min(columns, rows) // LOCAL_AGENT_EFFECT_NEIGHBOR_DIVISOR)
    focus = set()
    for x, y in points:
        column = max(0, min(columns - 1, int(x * columns / width)))
        row = max(0, min(rows - 1, int(y * rows / height)))
        focus.update(yy * columns + xx for yy in range(max(0, row - radius), min(rows, row + radius + 1)) for xx in range(max(0, column - radius), min(columns, column + radius + 1)))
    deltas = [sum(abs(left - right) for left, right in zip(a, b)) / (AI_RGB_CHANNELS * AI_BYTE_MAX) for a, b in zip(first, second)]
    focused = sum(deltas[index] for index in focus) / len(focus)
    ambient = sum(deltas[index] for index in range(len(deltas)) if index not in focus) / max(1, len(deltas) - len(focus))
    contrast = max(0.0, focused - ambient * LOCAL_AGENT_EFFECT_AMBIENT_SHARE)
    return {"focus_change": focused, "ambient_change": ambient, "local_contrast": contrast}


def local_agent_balanced_scene(controls, annotations, regions, learned=()):
    groups = (controls, learned, regions, annotations)
    indices = [0] * len(groups)
    result = []
    while len(result) < LOCAL_AGENT_SMART_OVERLAY_LIMIT:
        added = False
        for index, group in enumerate(groups):
            if indices[index] < len(group):
                result.append(group[indices[index]])
                indices[index] += 1
                added = True
                if len(result) >= LOCAL_AGENT_SMART_OVERLAY_LIMIT:
                    break
        if not added:
            break
    return result


def local_agent_detect_turn(labels):
    tokens = set(labels)
    self_turn = bool(tokens & LOCAL_AGENT_SELF_TURN_LABELS)
    other_turn = bool(tokens & LOCAL_AGENT_OTHER_TURN_LABELS)
    return "self" if self_turn and not other_turn else "opponent" if other_turn and not self_turn else "unknown"


def local_agent_affordance_bucket(relative):
    if not isinstance(relative, dict) or relative.get("kind") not in {"tap", "long_press", "swipe", "touch", "touch_begin", "touch_update"}:
        return ""
    points = relative.get("pointers") if relative.get("kind", "").startswith("touch") else [relative]
    if not isinstance(points, list) or not points:
        return ""
    grid = LOCAL_AGENT_AFFORDANCE_GRID
    elements = []
    for point in sorted(points, key=lambda item: item.get("id", 0)):
        if not isinstance(point, dict):
            return ""
        values = [point.get(axis) for axis in ("x", "y")]
        if any(type(value) not in (int, float) or not math.isfinite(value) or not 0 <= value <= AI_COORDINATE_SCALE for value in values):
            return ""
        cell = [min(grid - 1, int(value * grid / (AI_COORDINATE_SCALE + 1))) for value in values]
        direction = []
        for axis, origin in (("x2", "x"), ("y2", "y")):
            finish = point.get(axis, point.get(origin))
            if type(finish) not in (int, float) or not math.isfinite(finish) or not 0 <= finish <= AI_COORDINATE_SCALE:
                return ""
            distance = finish - point[origin]
            direction.append((distance > 0) - (distance < 0))
        elements.append((cell[0], cell[1], *direction))
    return json.dumps((relative["kind"], *elements), separators=(",", ":"))


def local_agent_attention_tiles(samples, size, previous=(), noise=0.0):
    if not samples or len(size) != AI_SPATIAL_DIMENSIONS:
        return []
    width, height = size
    columns, rows = vision_sample_grid(width, height)
    if len(samples) != columns * rows:
        return []
    tile_columns = max(1, math.isqrt(columns))
    tile_rows = max(1, math.isqrt(rows))
    cells = {}
    temporal = len(previous) == len(samples)
    for index, pixel in enumerate(samples):
        gy, gx = divmod(index, columns)
        tx, ty = min(tile_columns - 1, gx * tile_columns // columns), min(tile_rows - 1, gy * tile_rows // rows)
        cell = cells.setdefault((tx, ty), {"pixels": [], "motion": 0.0, "edges": 0.0})
        cell["pixels"].append(pixel)
        if temporal:
            cell["motion"] += sum(abs(a - b) for a, b in zip(pixel, previous[index])) / (AI_RGB_CHANNELS * AI_BYTE_MAX)
        if gx and gx * tile_columns // columns == (gx - 1) * tile_columns // columns:
            nearby = samples[index - 1]
            cell["edges"] += sum(abs(a - b) for a, b in zip(pixel, nearby)) / (AI_RGB_CHANNELS * AI_BYTE_MAX)
    results = []
    for (tx, ty), cell in cells.items():
        pixels = cell["pixels"]
        count = len(pixels)
        means = [sum(pixel[channel] for pixel in pixels) / count for channel in range(AI_RGB_CHANNELS)]
        variance = sum(sum(abs(pixel[channel] - means[channel]) for channel in range(AI_RGB_CHANNELS)) for pixel in pixels) / (count * AI_RGB_CHANNELS * AI_BYTE_MAX)
        motion = cell["motion"] / count
        texture = cell["edges"] / count
        score = variance + texture + max(0.0, motion - noise)
        left = tx * width // tile_columns
        top = ty * height // tile_rows
        right = min(width, (tx + 1) * width // tile_columns)
        bottom = min(height, (ty + 1) * height // tile_rows)
        results.append({"kind": "motion_target" if temporal and motion > max(noise, LOCAL_AGENT_EFFECT_MINIMUM) else "visual_target", "source": "local_attention", "label": "局部显著区域（未确认语义）", "bounds": [left, top, right, bottom], "x": (left + right - 1) // AI_SPATIAL_DIMENSIONS, "y": (top + bottom - 1) // AI_SPATIAL_DIMENSIONS, "strength": score, "motion": motion, "area": count})
    scores = [item["strength"] for item in results]
    if not scores:
        return []
    central = statistics.median(scores)
    threshold = max(LOCAL_AGENT_EFFECT_MINIMUM, central + statistics.median(abs(score - central) for score in scores) / AI_SPATIAL_DIMENSIONS)
    usage = collections.Counter()
    selected = []
    for item in sorted(results, key=lambda value: value["strength"], reverse=True):
        if item["strength"] < threshold:
            break
        quadrant = (int(item["x"] >= width / AI_SPATIAL_DIMENSIONS), int(item["y"] >= height / AI_SPATIAL_DIMENSIONS))
        if usage[quadrant] >= LOCAL_AGENT_ATTENTION_PER_QUADRANT:
            continue
        selected.append(item)
        usage[quadrant] += 1
    return selected


def local_agent_passive_scene(png, context=None, previous=None):
    width, height = frame_dimensions(png)
    context = context if isinstance(context, dict) else {}
    nodes = AI_disambiguate_nodes(context.get("nodes", ()))
    samples = visual_samples(png)
    regions = local_agent_visual_regions(samples, (width, height), previous if previous is not None else ()) if samples else []
    controls = [item for item in nodes if item.get("clickable") is True and isinstance(item.get("bounds"), (tuple, list)) and len(item["bounds"]) == AI_BOUNDING_BOX_COMPONENTS]
    scene = [{"kind": "ui_control", "source": "accessibility", "bounds": list(item["bounds"]), "node_ref": AI_node_reference(item), "package": str(context.get("package", "")), "activity": str(context.get("activity", "")), "enabled": item.get("enabled", True) is True, "label": str(item.get("text") or item.get("content_desc") or item.get("id") or "可交互控件")[:AI_LABEL_FIELD_LIMIT]} for item in controls]
    descriptor = {"package": str(context.get("package", "")), "size": (width, height), "phase": "menu" if controls else "unknown", "regions": regions}
    profile = local_agent_game_profile(descriptor)
    return {"game": descriptor["package"] or "安卓应用", "phase": descriptor["phase"], "scene_graph": local_agent_balanced_scene(scene, profile["annotations"], regions), "screen_size": [width, height], "game_profile": {key: value for key, value in profile.items() if key not in {"anchors", "annotations"}}, "controls": len(controls), "visual_regions": len(regions), "samples": samples}


class GameAI:
    def __init__(self, root, log, status=None):
        self.root = Path(root).resolve()
        self.log = log
        self.status = status if status is not None else lambda value: None
        self.model_name = "多尺度离线视觉 + 原生控件 + 跨场景控制记忆 + UCB/TD 规划"
        self.backend = "Python 标准库 · 本地 CPU"
        self._prepared = False
        self._started = False
        self._healthy = False
        self._validated = False
        self._last_engine_error = ""
        self._lock = threading.RLock()
        self._cancel_generation = 0
        self._deadline = 0.0
        self._db = None
        self._database_path = self.root / "data" / "local-policy.sqlite3"
        self._planning = []
        self._priorities = {}
        self._terminal_candidates = {}
        self._last_descriptors = {}
        self._sample_cache = collections.OrderedDict()
        self._motion_history = collections.OrderedDict()
        self._discount_cache = {}
        self._package_counts = {}
        self._aggregate_counts = None
        self._plan_serial = 0
        self._input_epoch_started_at = time.monotonic()
        self._stats = {"decisions": 0, "planning_backups": 0, "td_updates": 0}
        self.timings = collections.deque(maxlen=AI_INFERENCE_TIMING_SAMPLES)

    def _check(self, cancel=None, generation=None):
        check_cancel(cancel)
        if generation is not None and generation != self._cancel_generation:
            raise Cancelled()

    def prepare(self, cancel=None):
        self._check(cancel)
        with self._lock:
            if self._db is not None:
                self._prepared = True
                return True
            self._database_path.parent.mkdir(parents=True, exist_ok=True)
            safe_workspace_file(self.root, self._database_path)
            connection = sqlite3.connect(str(self._database_path), timeout=AI_MEMORY_BUSY_SECONDS, check_same_thread=False)
            connection.row_factory = sqlite3.Row
            try:
                connection.executescript("PRAGMA journal_mode=WAL; PRAGMA synchronous=NORMAL; CREATE TABLE IF NOT EXISTS agent_meta(key TEXT PRIMARY KEY,value TEXT NOT NULL); CREATE TABLE IF NOT EXISTS agent_states(package TEXT NOT NULL,state_key TEXT NOT NULL,features TEXT NOT NULL,visits INTEGER NOT NULL DEFAULT 0,value REAL NOT NULL DEFAULT 0,intrinsic_value REAL NOT NULL DEFAULT 0,last_seen TEXT NOT NULL,PRIMARY KEY(package,state_key)); CREATE TABLE IF NOT EXISTS agent_actions(package TEXT NOT NULL,state_key TEXT NOT NULL,action_key TEXT NOT NULL,action TEXT NOT NULL,visits INTEGER NOT NULL DEFAULT 0,reward_samples INTEGER NOT NULL DEFAULT 0,reward_sum REAL NOT NULL DEFAULT 0,intrinsic_sum REAL NOT NULL DEFAULT 0,q REAL NOT NULL DEFAULT 0,iq REAL NOT NULL DEFAULT 0,PRIMARY KEY(package,state_key,action_key)); CREATE TABLE IF NOT EXISTS agent_transitions(package TEXT NOT NULL,state_key TEXT NOT NULL,action_key TEXT NOT NULL,next_state TEXT NOT NULL,terminal INTEGER NOT NULL,visits INTEGER NOT NULL,reward_sum REAL NOT NULL,intrinsic_sum REAL NOT NULL,reward_samples INTEGER NOT NULL,seconds_sum REAL NOT NULL,PRIMARY KEY(package,state_key,action_key,next_state,terminal)); CREATE INDEX IF NOT EXISTS agent_predecessors ON agent_transitions(package,next_state); CREATE TABLE IF NOT EXISTS agent_observed(action_id TEXT PRIMARY KEY,package TEXT NOT NULL,episode TEXT NOT NULL,ordinal INTEGER NOT NULL,state_key TEXT NOT NULL,action_key TEXT NOT NULL,next_state TEXT NOT NULL,initial_next_state TEXT NOT NULL,terminal INTEGER NOT NULL,reward REAL NOT NULL,intrinsic REAL NOT NULL,verified INTEGER NOT NULL,applied_at REAL NOT NULL,nodes_at REAL NOT NULL,frame_id INTEGER NOT NULL,seconds REAL NOT NULL,evidence TEXT NOT NULL); CREATE INDEX IF NOT EXISTS agent_episode_actions ON agent_observed(package,episode,ordinal); CREATE TABLE IF NOT EXISTS agent_sessions(package TEXT PRIMARY KEY,episode TEXT NOT NULL,steps INTEGER NOT NULL,last_action TEXT NOT NULL,terminal_latched INTEGER NOT NULL DEFAULT 0); CREATE TABLE IF NOT EXISTS agent_outcomes(episode TEXT PRIMARY KEY,package TEXT NOT NULL,outcome TEXT NOT NULL,evidence TEXT NOT NULL,action_id TEXT NOT NULL,steps INTEGER NOT NULL,verified_at TEXT NOT NULL);")
                row = connection.execute("SELECT value FROM agent_meta WHERE key='schema'").fetchone()
                if row is not None and int(json.loads(row["value"])) != LOCAL_AGENT_SCHEMA_VERSION:
                    raise ValueError("本地经验数据库版本不兼容")
                columns = {row["name"] for row in connection.execute("PRAGMA table_info(agent_actions)")}
                for name, definition in (("source", "TEXT NOT NULL DEFAULT ''"), ("preconditions", "TEXT NOT NULL DEFAULT '[]'"), ("label", "TEXT NOT NULL DEFAULT ''"), ("effect_samples", "INTEGER NOT NULL DEFAULT 0"), ("effect_sum", "REAL NOT NULL DEFAULT 0"), ("demonstrations", "INTEGER NOT NULL DEFAULT 0")):
                    if name not in columns:
                        connection.execute("ALTER TABLE agent_actions ADD COLUMN " + name + " " + definition)
                connection.execute("CREATE TABLE IF NOT EXISTS agent_affordances(package TEXT NOT NULL,phase TEXT NOT NULL,bucket TEXT NOT NULL,action TEXT NOT NULL,attempts INTEGER NOT NULL DEFAULT 0,effect_samples INTEGER NOT NULL DEFAULT 0,effect_sum REAL NOT NULL DEFAULT 0,reward_samples INTEGER NOT NULL DEFAULT 0,reward_sum REAL NOT NULL DEFAULT 0,demonstrations INTEGER NOT NULL DEFAULT 0,last_seen TEXT NOT NULL,PRIMARY KEY(package,phase,bucket))")
                connection.execute("CREATE INDEX IF NOT EXISTS agent_affordance_transfer ON agent_affordances(package,phase,demonstrations DESC,reward_samples DESC,effect_samples DESC)")
                connection.execute("CREATE INDEX IF NOT EXISTS agent_states_recent ON agent_states(package,last_seen DESC)")
                connection.execute("CREATE INDEX IF NOT EXISTS agent_actions_recall ON agent_actions(package,state_key,demonstrations DESC,q DESC,visits DESC)")
                connection.execute("CREATE INDEX IF NOT EXISTS agent_actions_transfer ON agent_actions(package,reward_samples,visits)")
                connection.execute("CREATE TABLE IF NOT EXISTS agent_terminal_templates(package TEXT NOT NULL,outcome TEXT NOT NULL,screen TEXT NOT NULL,features TEXT NOT NULL,confirmations INTEGER NOT NULL,last_seen TEXT NOT NULL,PRIMARY KEY(package,outcome,screen,features))")
                connection.execute("CREATE INDEX IF NOT EXISTS agent_terminal_lookup ON agent_terminal_templates(package,screen,confirmations DESC)")
                connection.execute("INSERT OR IGNORE INTO agent_meta(key,value) VALUES('schema',?)", (json.dumps(LOCAL_AGENT_SCHEMA_VERSION),))
                row = connection.execute("SELECT value FROM agent_meta WHERE key='statistics'").fetchone()
                if row is not None:
                    saved = json.loads(row["value"])
                    if isinstance(saved, dict):
                        for key in self._stats:
                            self._stats[key] = max(0, int(local_agent_number(saved.get(key))))
                connection.commit()
            except BaseException:
                connection.close()
                raise
            self._db = connection
            self._prepared = True
            self.log("local_agent_prepared", algorithm=self.model_name, external_models=False, external_network=False, limitation=LOCAL_AGENT_LIMITATION)
            return True

    def start(self, cancel=None, sample_png=None):
        self._check(cancel)
        self.prepare(cancel)
        if sample_png is not None:
            self.verify_inference(sample_png, cancel)
        with self._lock:
            self._started = True
            self._healthy = True
            self._last_engine_error = ""
        return True

    def verify_inference(self, png, cancel=None):
        self._check(cancel)
        size = frame_dimensions(png)
        samples = visual_samples(png)
        if not samples:
            raise ValueError("无法解码设备截图，本地视觉感知未就绪")
        self._validated = True
        self.log("local_visual_verified", width=size[0], height=size[1], samples=len(samples), semantic_understanding=False)
        return True

    def validate_decision(self, observation, png, cancel=None):
        self._check(cancel)
        generation = self._cancel_generation
        with self._lock:
            if not self.alive():
                raise ComponentFailure("ai", "本地决策链尚未初始化")
            saved = {"_sample_cache": self._sample_cache.copy(), "_motion_history": self._motion_history.copy(), "_last_descriptors": dict(self._last_descriptors), "_discount_cache": dict(self._discount_cache), "_package_counts": {key: dict(value) for key, value in self._package_counts.items()}, "_aggregate_counts": dict(self._aggregate_counts) if self._aggregate_counts is not None else None, "_terminal_candidates": dict(self._terminal_candidates), "_planning": list(self._planning), "_priorities": dict(self._priorities), "_stats": dict(self._stats), "_plan_serial": self._plan_serial, "_deadline": self._deadline, "timings": self.timings.copy()}
            self._db.execute("SAVEPOINT agent_decision_validation")
            try:
                plan = self.plan(observation, png, cancel=cancel, _commit=False)
                actions = plan.get("actions", [])
                if not actions:
                    raise ValueError("当前设备没有可用的动作接口")
                for action in actions:
                    self._check(cancel, generation)
                    normalize_action(action, observation)
                evidence = plan["policy_evidence"]
                return {"verified": True, "size": list(frame_dimensions(png)), "phase": plan["phase"], "valid_candidates": evidence["valid_candidates"], "action_source": evidence["action_source"], "professional_skill_verified": False}
            finally:
                try:
                    self._db.execute("ROLLBACK TO agent_decision_validation")
                    self._db.execute("RELEASE agent_decision_validation")
                finally:
                    for name, value in saved.items():
                        setattr(self, name, value)
                    if self._cancel_generation != generation:
                        self._terminal_candidates.clear()

    def alive(self):
        return bool(self._started and self._db is not None)

    def preferred_host_budget(self, cancel=None):
        self._check(cancel)
        return math.ceil(AI_PERCEPTION_MAX_DECODE_BYTES / AI_BYTES_PER_MEBIBYTE)

    def cancel_request(self):
        self._cancel_generation += 1
        self._input_epoch_started_at = time.monotonic()
        self._terminal_candidates.clear()

    def active_request_deadline(self):
        return self._deadline

    def note_runtime_failure(self, error):
        self._last_engine_error = str(error)
        self.log("local_agent_error", error=self._last_engine_error)

    def remember_demonstration(self, observation, png, action):
        if not self.alive() or not isinstance(observation, dict) or not isinstance(action, dict):
            return {"recorded": False, "reason": "agent_not_ready"}
        if action.get("kind") not in {"tap", "swipe", "long_press"} or not observation.get("package"):
            return {"recorded": False, "reason": "not_a_game_gesture"}
        with self._lock, self._transaction():
            if self._db is None or not self._started:
                return {"recorded": False, "reason": "agent_stopped"}
            normalized = normalize_action(action, observation)
            descriptor = self._describe(observation, png)
            state = descriptor["state"]
            relative = relative_action(normalized, descriptor["size"])
            conditions = [{"kind": "package", "value": descriptor["package"]}]
            if descriptor["activity"]:
                conditions.append({"kind": "activity", "value": descriptor["activity"]})
            signature = local_agent_learning_signature(relative)
            label = "人工操作示教（只记录操作，不声称结果正确）"
            for node in descriptor["clickable"]:
                left, top, right, bottom = node["bounds"]
                if left <= normalized["x"] < right and top <= normalized["y"] < bottom and normalized["kind"] in {"tap", "long_press"}:
                    signature = local_agent_learning_signature(relative, node)
                    relative["target_position"] = [round(AI_COORDINATE_SCALE * (normalized["x"] - left) / max(1, right - left - 1)), round(AI_COORDINATE_SCALE * (normalized["y"] - top) / max(1, bottom - top - 1))]
                    conditions.append({"kind": "node_enabled", "value": AI_node_reference(node)})
                    label = "用户示教控件 · " + descriptor["targets"][AI_node_reference(node)]["label"][:AI_LABEL_FIELD_LIMIT]
                    break
            key = hashlib.sha256(json.dumps(signature, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()
            self._ensure_state(descriptor)
            inserted = self._db.execute("INSERT OR IGNORE INTO agent_actions(package,state_key,action_key,action,source,preconditions,label) VALUES(?,?,?,?,?,?,?)", (descriptor["package"], state, key, json.dumps(relative, ensure_ascii=False, separators=(",", ":")), "human_demonstration", json.dumps(conditions, ensure_ascii=False, separators=(",", ":")), label)).rowcount
            if inserted:
                self._adjust_counts(actions=inserted)
            self._db.execute("UPDATE agent_actions SET demonstrations=demonstrations+1,action=?,source='human_demonstration',preconditions=?,label=? WHERE package=? AND state_key=? AND action_key=?", (json.dumps(relative, ensure_ascii=False, separators=(",", ":")), json.dumps(conditions, ensure_ascii=False, separators=(",", ":")), label, descriptor["package"], state, key))
            self._db.execute("UPDATE agent_states SET visits=visits+1 WHERE package=? AND state_key=?", (descriptor["package"], state))
            self._adjust_counts(demonstrations=1)
            self._learn_affordance(descriptor["package"], descriptor["phase"], relative, demonstration=True)
            self._save_statistics()
            return {"recorded": True, "package": descriptor["package"], "kind": normalized["kind"], "state": state, "demonstrations": self._db.execute("SELECT demonstrations FROM agent_actions WHERE package=? AND state_key=? AND action_key=?", (descriptor["package"], state, key)).fetchone()[0], "source": "manual_gesture_without_outcome_claim"}

    def _learn_affordance(self, package, phase, relative, effect_measured=False, effect=0.0, reward_verified=False, reward=0.0, demonstration=False):
        if self._db is None or not package or phase not in {"playing", "unknown"}:
            return False
        bucket = local_agent_affordance_bucket(relative)
        if not bucket:
            return False
        measured = bool(effect_measured and math.isfinite(local_agent_number(effect)))
        verified = bool(reward_verified and math.isfinite(local_agent_number(reward)))
        visits = int(not demonstration)
        demonstrations = int(bool(demonstration))
        inserted = self._db.execute("INSERT OR IGNORE INTO agent_affordances(package,phase,bucket,action,last_seen) VALUES(?,?,?,?,?)", (package, phase, bucket, json.dumps(relative, ensure_ascii=False, separators=(",", ":")), utc_now())).rowcount
        self._db.execute("UPDATE agent_affordances SET action=?,attempts=attempts+?,effect_samples=effect_samples+?,effect_sum=effect_sum+?,reward_samples=reward_samples+?,reward_sum=reward_sum+?,demonstrations=demonstrations+?,last_seen=? WHERE package=? AND phase=? AND bucket=?", (json.dumps(relative, ensure_ascii=False, separators=(",", ":")), visits, int(measured), local_agent_number(effect) if measured else 0.0, int(verified), max(-1.0, min(1.0, local_agent_number(reward))) if verified else 0.0, demonstrations, utc_now(), package, phase, bucket))
        self._adjust_counts(affordance_cells=inserted, affordance_trials=visits, affordance_effect_samples=int(measured), affordance_reward_samples=int(verified), affordance_demonstrations=demonstrations)
        return True

    def _affordance_values(self, descriptor, candidates):
        package, phase = descriptor["package"], descriptor["phase"]
        if phase not in {"playing", "unknown"} or not package:
            return {}
        buckets = tuple({local_agent_affordance_bucket(item["relative"]) for item in candidates} - {""})
        result = {}
        batch_size = AI_MEMORY_DEFAULT_RECALL * AI_MEMORY_DEFAULT_RECALL
        for offset in range(0, len(buckets), batch_size):
            batch = buckets[offset:offset + batch_size]
            placeholders = ",".join("?" for _ in batch)
            for row in self._db.execute("SELECT bucket,attempts,effect_samples,effect_sum,reward_samples,reward_sum,demonstrations FROM agent_affordances WHERE package=? AND phase=? AND bucket IN (" + placeholders + ")", (package, phase, *batch)):
                result[row["bucket"]] = dict(row)
        return result

    def _affordance_annotations(self, package, phase, size):
        if self._db is None or not package or phase not in {"playing", "unknown"}:
            return []
        width, height = size
        annotated = []
        rows = self._db.execute("SELECT action,attempts,effect_samples,effect_sum,reward_samples,reward_sum,demonstrations FROM agent_affordances WHERE package=? AND phase=? AND (effect_sum>0 OR reward_samples>0 OR demonstrations>0) ORDER BY demonstrations DESC,reward_samples DESC,effect_sum DESC LIMIT ?", (package, phase, LOCAL_AGENT_AFFORDANCE_RECALL)).fetchall()
        for row in rows:
            try:
                action = local_agent_absolute_action(json.loads(row["action"]), size)
                positions = action.get("pointers", [action])
                if not positions or not isinstance(positions[0], dict) or not all(type(positions[0].get(axis)) is int for axis in ("x", "y")):
                    continue
                x, y = positions[0]["x"], positions[0]["y"]
                dx = max(1, math.ceil(width / LOCAL_AGENT_AFFORDANCE_GRID / AI_SPATIAL_DIMENSIONS))
                dy = max(1, math.ceil(height / LOCAL_AGENT_AFFORDANCE_GRID / AI_SPATIAL_DIMENSIONS))
                evidence = ("示教 " + str(row["demonstrations"]) + " 次") if row["demonstrations"] else ("结果反馈 " + str(row["reward_samples"]) + " 次") if row["reward_samples"] else "视觉响应 " + str(row["effect_samples"]) + " 次"
                annotated.append({"source": "learned_affordance", "kind": "learned_control", "bounds": [max(0, x - dx), max(0, y - dy), min(width, x + dx + 1), min(height, y + dy + 1)], "x": x, "y": y, "label": "跨画面已学控制 · " + evidence, "attempts": row["attempts"], "evidence": evidence})
            except (ValueError, TypeError, KeyError, OverflowError):
                continue
        return annotated

    def _save_statistics(self):
        self._db.execute("INSERT INTO agent_meta(key,value) VALUES('statistics',?) ON CONFLICT(key) DO UPDATE SET value=excluded.value", (json.dumps(self._stats, ensure_ascii=False),))

    @contextlib.contextmanager
    def _transaction(self, enabled=True):
        statistics, serial = dict(self._stats), self._plan_serial
        try:
            with (self._db if self._db is not None and enabled else contextlib.nullcontext()):
                yield
        except BaseException:
            self._stats = statistics
            self._plan_serial = serial
            self._aggregate_counts = None
            self._package_counts.clear()
            self._discount_cache.clear()
            self._terminal_candidates.clear()
            raise

    def _adjust_counts(self, **changes):
        if self._aggregate_counts is not None:
            for key, value in changes.items():
                self._aggregate_counts[key] += value

    def _package_samples(self, package):
        if package not in self._package_counts:
            self._package_counts[package] = dict(self._db.execute("SELECT COALESCE(SUM(reward_samples),0) AS rewards,COALESCE(SUM(visits),0) AS transitions FROM agent_actions WHERE package=?", (package,)).fetchone())
        return self._package_counts[package]

    def _record_sample_counts(self, package, transitions=0, rewards=0):
        self._adjust_counts(transition_samples=transitions, verified_reward_samples=rewards)
        if package in self._package_counts:
            self._package_counts[package]["transitions"] += transitions
            self._package_counts[package]["rewards"] += rewards

    def stop(self):
        self.cancel_request()
        with self._lock:
            self._started = False
            self._healthy = False
            if self._db is not None:
                try:
                    with self._db:
                        self._save_statistics()
                    self._db.execute("PRAGMA wal_checkpoint(PASSIVE)")
                finally:
                    self._db.close()
                    self._db = None
                    self._prepared = False
            self._planning.clear()
            self._priorities.clear()
            self._last_descriptors.clear()
            self._sample_cache.clear()
            self._motion_history.clear()
            self._discount_cache.clear()
            self._package_counts.clear()
            self._aggregate_counts = None

    @staticmethod
    def _preconditions_hold(conditions, observation):
        if not isinstance(conditions, list) or not isinstance(observation, dict):
            return False
        for condition in conditions:
            if not isinstance(condition, dict):
                return False
            kind, value = condition.get("kind"), str(condition.get("value", ""))
            if kind not in AI_PRECONDITION_KINDS:
                return False
            if kind in {"package", "activity"} and str(observation.get(kind, "")) != value:
                return False
            if kind in {"visible_text", "node_ref", "node_enabled", "node_state"}:
                started = observation.get("nodes_started_at")
                finished = observation.get("nodes_at")
                if any(type(moment) not in (int, float) or not math.isfinite(moment) for moment in (started, finished)) or not 0 <= started <= finished <= time.monotonic():
                    return False
            if kind == "visible_text" and value.casefold() not in AI_visible_text(observation):
                return False
            if kind in {"node_ref", "node_enabled", "node_state"}:
                matches = AI_matching_nodes(observation.get("nodes", []), value)
                if len(matches) != 1 or kind == "node_enabled" and matches[0].get("enabled", True) is not True:
                    return False
                if kind == "node_state":
                    field, expected = condition.get("field"), condition.get("expected")
                    if field not in {"checked", "selected", "focused"} or type(expected) is not bool or (matches[0].get(field) is True) != expected:
                        return False
            if kind == "active_pointer" and value not in {str(point.get("id")) for point in observation.get("active_touches", []) if isinstance(point, dict)}:
                return False
            if kind == "available_pointer" and value in {str(point.get("id")) for point in observation.get("active_touches", []) if isinstance(point, dict)}:
                return False
        return True

    @staticmethod
    def _score(node):
        label = str(node.get("text") or node.get("content_desc") or "").strip()
        name = str(node.get("resource_id") or node.get("id") or "").rsplit("/", 1)[-1].casefold()
        expression = r"([-+]?\d+(?:\.\d+)?)"
        indicators = LOCAL_AGENT_SCORE_NAMES | LOCAL_AGENT_PROGRESS_DIRECTIONS.keys()
        match = re.fullmatch(expression, label) if name in indicators else None
        if match is None:
            labels = "|".join(re.escape(value) for value in sorted(indicators, key=len, reverse=True))
            match = re.fullmatch(r"(?:" + labels + r")\s*[:：]?\s*" + expression, label, re.IGNORECASE)
        if match is None:
            return None
        number = float(match.group(1))
        return number if math.isfinite(number) else None

    @staticmethod
    def _score_direction(node):
        identity = str(node.get("resource_id") or node.get("id") or "").rsplit("/", 1)[-1].casefold()
        label = str(node.get("text") or node.get("content_desc") or "").casefold()
        label = re.sub(r"\s*[:：]?\s*[-+]?\d+(?:\.\d+)?\s*$", "", label).strip()
        return LOCAL_AGENT_PROGRESS_DIRECTIONS.get(identity, LOCAL_AGENT_PROGRESS_DIRECTIONS.get(label, 1))

    @classmethod
    def _paired_scores(cls, nodes):
        resolved = {}
        for label_node in nodes:
            label = local_agent_label(label_node.get("text") or label_node.get("content_desc") or "")
            if label not in LOCAL_AGENT_SCORE_NAMES and label not in LOCAL_AGENT_PROGRESS_DIRECTIONS or label_node.get("bounds") is None:
                continue
            bounds = label_node["bounds"]
            path = str(label_node.get("tree_path", ""))
            if not path or len(bounds) != AI_BOUNDING_BOX_COMPONENTS:
                continue
            parent = path.rpartition("/")[0]
            left, top, right, bottom = bounds
            candidates = []
            for node in nodes:
                if node is label_node or str(node.get("tree_path", "")).rpartition("/")[0] != parent:
                    continue
                value = str(node.get("text") or node.get("content_desc") or "").strip()
                if re.fullmatch(r"[-+]?\d+(?:\.\d+)?", value) is None or cls._score(node) is not None:
                    continue
                other = node.get("bounds")
                if not isinstance(other, (tuple, list)) or len(other) != AI_BOUNDING_BOX_COMPONENTS:
                    continue
                x0, y0, x1, y1 = other
                overlaps = y0 < bottom and y1 > top and x0 >= left
                below = y0 >= bottom and y0 - bottom <= max(1, bottom - top) and x1 > left and x0 < right
                if not overlaps and not below:
                    continue
                distance = abs((x0 + x1) - (left + right)) + abs((y0 + y1) - (top + bottom))
                candidates.append((distance, value))
            candidates.sort()
            if not candidates or len(candidates) > 1 and candidates[0][0] == candidates[1][0]:
                continue
            number = float(candidates[0][1])
            if math.isfinite(number):
                identity = AI_node_reference(label_node) if "_agent_duplicate_order" in label_node else local_agent_node_key(label_node)
                resolved[identity] = {"value": number, "label": label + " " + candidates[0][1], "id": str(label_node.get("resource_id") or label_node.get("id") or ""), "direction": cls._score_direction(label_node), "source": "paired_accessibility_text"}
        return resolved

    @staticmethod
    def _nodes_fresh(observation, applied_at=None):
        started, finished = observation.get("nodes_started_at"), observation.get("nodes_at")
        if any(type(value) not in (int, float) or not math.isfinite(value) for value in (started, finished)):
            return False
        if not 0 <= started <= finished <= time.monotonic():
            return False
        return applied_at is None or started > applied_at

    def _visual(self, png, width, height):
        if png is None:
            return (), (), ()
        digest = hashlib.sha256(png).hexdigest()
        cached = self._sample_cache.get(digest)
        if cached is not None:
            self._sample_cache.move_to_end(digest)
            return cached
        samples = visual_samples(png)
        if not samples:
            return (), (), ()
        columns, rows = vision_sample_grid(width, height)
        coarse_columns, coarse_rows = max(1, math.isqrt(columns)), max(1, math.isqrt(rows))
        cells = [[0.0] * (AI_RGB_CHANNELS + 1) for _ in range(coarse_columns * coarse_rows)]
        contrast = []
        mean = tuple(sum(pixel[channel] for pixel in samples) / len(samples) for channel in range(AI_RGB_CHANNELS))
        for index, pixel in enumerate(samples):
            row, column = divmod(index, columns)
            cell = cells[min(coarse_rows - 1, row * coarse_rows // rows) * coarse_columns + min(coarse_columns - 1, column * coarse_columns // columns)]
            for channel in range(AI_RGB_CHANNELS):
                cell[channel] += pixel[channel]
            cell[-1] += 1
            adjacent = []
            for dx, dy in LOCAL_AGENT_DIRECTIONS:
                nx, ny = column + dx, row + dy
                if 0 <= nx < columns and 0 <= ny < rows:
                    adjacent.append(samples[ny * columns + nx])
            edge = sum(sum(abs(a - b) for a, b in zip(pixel, neighbor)) for neighbor in adjacent) / max(1, len(adjacent) * AI_RGB_CHANNELS * AI_BYTE_MAX)
            color = sum(abs(a - b) for a, b in zip(pixel, mean)) / (AI_RGB_CHANNELS * AI_BYTE_MAX)
            contrast.append((edge + color, column, row))
        quantized = tuple(round(cell[channel] / max(1, cell[-1]) * (AI_VISION_STATE_LEVELS - 1) / AI_BYTE_MAX) for cell in cells for channel in range(AI_RGB_CHANNELS))
        candidates = sorted(contrast, key=lambda item: (-item[0], item[2], item[1]))
        selected = []
        occupied = set()
        for score, column, row in candidates:
            cell = (column * coarse_columns // columns, row * coarse_rows // rows)
            if cell in occupied:
                continue
            occupied.add(cell)
            selected.append((min(width - 1, (column * 2 + 1) * width // (columns * 2)), min(height - 1, (row * 2 + 1) * height // (rows * 2)), score))
        value = (quantized, tuple(selected), samples)
        self._sample_cache[digest] = value
        while len(self._sample_cache) > AI_PERCEPTION_CACHE_FRAMES:
            self._sample_cache.popitem(last=False)
        return value

    def _motion_targets(self, package, png, samples, width, height, noise, captured):
        if not package or png is None or not samples:
            return ()
        captured = local_agent_number(captured)
        digest = hashlib.sha256(png).digest()
        previous = self._motion_history.get(package)
        if previous is not None and captured <= previous["captured"]:
            return ()
        motion = ()
        if previous is not None and previous["digest"] != digest and previous["size"] == (width, height) and len(previous["samples"]) == len(samples):
            columns, rows = vision_sample_grid(width, height)
            threshold = max(1 / AI_BYTE_MAX, local_agent_number(noise))
            regions = {}
            coarse_columns = max(1, math.isqrt(columns))
            coarse_rows = max(1, math.isqrt(rows))
            for index, (first, second) in enumerate(zip(previous["samples"], samples)):
                change = sum(abs(left - right) for left, right in zip(first, second)) / (AI_RGB_CHANNELS * AI_BYTE_MAX)
                if change <= threshold:
                    continue
                y, x = divmod(index, columns)
                region = (x * coarse_columns // columns, y * coarse_rows // rows)
                existing = regions.get(region)
                if existing is None or change > existing[0]:
                    regions[region] = (change, x, y)
            motion = tuple((min(width - 1, (x * 2 + 1) * width // (columns * 2)), min(height - 1, (y * 2 + 1) * height // (rows * 2)), change) for change, x, y in sorted(regions.values(), reverse=True))
        self._motion_history[package] = {"digest": digest, "size": (width, height), "samples": samples, "captured": captured}
        self._motion_history.move_to_end(package)
        while len(self._motion_history) > AI_PERCEPTION_CACHE_FRAMES:
            self._motion_history.popitem(last=False)
        return motion

    @staticmethod
    def _feature_similarity(first, second):
        if not isinstance(first, dict) or not isinstance(second, dict) or first.get("phase") != second.get("phase"):
            return 0.0
        visual_a, visual_b = first.get("visual", ()), second.get("visual", ())
        visual_similarity = None
        if visual_a and visual_b and len(visual_a) == len(visual_b):
            difference = sum(abs(a - b) for a, b in zip(visual_a, visual_b))
            visual_similarity = max(0.0, 1 - difference / (len(visual_a) * max(1, AI_VISION_STATE_LEVELS - 1)))
        semantic_a = {json.dumps(node, ensure_ascii=False, separators=(",", ":")) for node in first.get("semantic", ())}
        semantic_b = {json.dumps(node, ensure_ascii=False, separators=(",", ":")) for node in second.get("semantic", ())}
        semantic_similarity = len(semantic_a & semantic_b) / len(semantic_a | semantic_b) if semantic_a or semantic_b else None
        if visual_similarity is None and semantic_similarity is None:
            return 0.0
        if visual_similarity is None:
            return semantic_similarity
        if semantic_similarity is None:
            return visual_similarity
        return (visual_similarity + semantic_similarity) / AI_SPATIAL_DIMENSIONS

    def _transfer_values(self, descriptor, candidates):
        lookup = {local_agent_memory_action_key(candidate["relative"]): candidate["key"] for candidate in candidates}
        if not lookup or not self._package_samples(descriptor["package"])["rewards"]:
            return {}
        records = self._db.execute("SELECT s.features,a.action,a.q,a.visits,a.reward_samples FROM agent_states s JOIN agent_actions a ON a.package=s.package AND a.state_key=s.state_key WHERE s.package=? AND s.state_key!=? AND (a.reward_samples>0 OR a.q!=0) AND a.visits>0 ORDER BY s.last_seen DESC LIMIT ?", (descriptor["package"], descriptor["state"], AI_MEMORY_DEFAULT_RECALL * AI_MEMORY_DEFAULT_RECALL)).fetchall()
        combined = {}
        for record in records:
            try:
                features = json.loads(record["features"])
                action = json.loads(record["action"])
            except (TypeError, ValueError):
                continue
            similarity = self._feature_similarity(descriptor["features"], features)
            if similarity <= 0:
                continue
            key = lookup.get(local_agent_memory_action_key(action))
            if key is None:
                continue
            supported_returns = max(record["reward_samples"], int(record["q"] != 0))
            evidence = supported_returns / (supported_returns + 1)
            strength = similarity * evidence * record["visits"] / (record["visits"] + 1)
            estimate = max(-1.0, min(1.0, local_agent_number(record["q"])))
            value, weight, matches = combined.get(key, (0.0, 0.0, 0))
            combined[key] = (value + estimate * strength, weight + strength, matches + 1)
        return {key: (value / max(1.0, weight), matches) for key, (value, weight, matches) in combined.items()}

    def _describe(self, observation, png=None):
        size = observation.get("size", (observation.get("width"), observation.get("height")))
        if not isinstance(size, (list, tuple)) or len(size) != AI_SPATIAL_DIMENSIONS or any(type(value) is not int or value <= 0 for value in size):
            raise ValueError("本地学习需要当前设备的真实画面尺寸")
        width, height = size
        if png is not None and frame_dimensions(png) != (width, height):
            raise ValueError("本地学习收到的截图和画面尺寸不一致")
        package, activity = str(observation.get("package", "")), str(observation.get("activity", ""))
        nodes = AI_disambiguate_nodes(observation.get("nodes", []))
        semantic, legacy_semantic, clickable, scores, labels = [], [], [], {}, []
        for node in nodes:
            label = local_agent_label(node.get("text") or node.get("content_desc") or node.get("description") or "")
            key = AI_node_reference(node) if "_agent_duplicate_order" in node else local_agent_node_key(node)
            score = self._score(node)
            if score is not None:
                scores[key] = {"value": score, "label": str(node.get("text") or node.get("content_desc") or ""), "id": str(node.get("resource_id") or node.get("id") or ""), "direction": self._score_direction(node)}
            semantic_fields = (re.sub(r"[-+]?\d+(?:\.\d+)?", "#", label), bool(node.get("clickable")), node.get("enabled", True) is True, node.get("selected") is True, node.get("checkable") is True, node.get("checked") is True)
            semantic.append((key, *semantic_fields))
            legacy_semantic.append((local_agent_legacy_node_key(node), *semantic_fields))
            if label:
                labels.append(label)
            bounds = node.get("bounds")
            if node.get("enabled", True) is not True or not isinstance(bounds, (list, tuple)) or len(bounds) != AI_BOUNDING_BOX_COMPONENTS or any(type(value) is not int for value in bounds):
                continue
            left, top, right, bottom = bounds
            if not 0 <= left < right <= width or not 0 <= top < bottom <= height:
                continue
            if node.get("clickable") is True:
                clickable.append(node)
        for key, record in self._paired_scores(nodes).items():
            scores.setdefault(key, record)
        wins = sorted(set(labels) & LOCAL_AGENT_WIN_LABELS)
        losses = sorted(set(labels) & LOCAL_AGENT_LOSS_LABELS)
        outcome = "win" if wins and not losses else "loss" if losses and not wins else "unknown"
        evidence = (wins if outcome == "win" else losses if outcome == "loss" else [""])[0]
        terminal_source = "accessibility" if outcome != "unknown" else ""
        loading = any(label in LOCAL_AGENT_LOADING_LABELS or re.fullmatch(r"(?:loading|正在加载|加载中)\s*[.…]*\s*\d*%?", label) for label in labels)
        perception = observation.get("perception", {})
        perception = perception if isinstance(perception, dict) else {}
        noise = max(1 / AI_BYTE_MAX, local_agent_number(perception.get("noise_floor"), 1 / AI_BYTE_MAX))
        drift = local_agent_number(perception.get("adaptive_drift"), noise)
        active_motion = local_agent_number(perception.get("motion")) > max(noise, drift)
        targets = {AI_node_reference(node): local_agent_ui_target(node, nodes) for node in clickable}
        navigation = any(target["navigation"] for target in targets.values())
        turn = local_agent_detect_turn(labels)
        continued_play = observation.get("previous_phase") == "playing" and not navigation
        active_control = bool(observation.get("active_touches"))
        phase = "result" if outcome != "unknown" else "loading" if loading else "menu" if navigation and not active_control else "playing" if scores or turn != "unknown" or active_motion or continued_play or active_control else "menu" if clickable else "unknown"
        visual, points, samples = self._visual(png, width, height)
        previous_visual = self._motion_history.get(package)
        previous_samples = previous_visual.get("samples", ()) if isinstance(previous_visual, dict) and previous_visual.get("size") == (width, height) and local_agent_number(observation.get("capture_started_at", observation.get("timestamp"))) > previous_visual.get("captured", 0) else ()
        regions = local_agent_visual_regions(samples, (width, height), previous_samples, noise)
        for attention in local_agent_attention_tiles(samples, (width, height), previous_samples, noise):
            if not any(region["bounds"][0] <= attention["x"] < region["bounds"][2] and region["bounds"][1] <= attention["y"] < region["bounds"][3] for region in regions):
                regions.append(attention)
        motion_points = self._motion_targets(package, png, samples, width, height, perception.get("noise_floor"), observation.get("capture_started_at", observation.get("timestamp")))
        if phase == "unknown" and not clickable and (motion_points or any(region["kind"] == "motion_target" for region in regions)):
            phase = "playing"
        if outcome == "unknown" and phase != "loading" and not scores and turn == "unknown" and visual:
            predicted, visual_evidence = self._visual_terminal_match(package, (width, height), visual)
            if predicted != "unknown":
                outcome, evidence, terminal_source, phase = predicted, visual_evidence, "learned_visual_template", "result"
        semantic_state = tuple(sorted(set(semantic)))
        semantic_ui = any(targets[AI_node_reference(node)]["semantic"] and (node["bounds"][2] - node["bounds"][0]) * (node["bounds"][3] - node["bounds"][1]) < width * height for node in clickable)
        score_state = tuple(sorted((key, record["value"]) for key, record in scores.items()))
        structure = (package, activity, phase, semantic_state, score_state, visual if phase == "playing" or not semantic_ui else ())
        if not nodes and not visual:
            cached = self._last_descriptors.get(package)
            if cached is not None and cached.get("capture_state") == observation.get("state"):
                return dict(cached)
            raise ValueError("缺少可访问节点及有效截图，不能伪造学习状态")
        state = hashlib.sha256(json.dumps(structure, ensure_ascii=False, separators=(",", ":")).encode("utf-8")).hexdigest()
        legacy_structure = (package, activity, phase, tuple(sorted(set(legacy_semantic))), visual if phase == "playing" or not semantic_ui else ())
        legacy_state = hashlib.sha256(json.dumps(legacy_structure, ensure_ascii=False, separators=(",", ":")).encode("utf-8")).hexdigest()
        features = {"package": package, "activity": activity, "phase": phase, "semantic": semantic_state, "visual": visual, "score_ids": sorted(scores), "score_values": sorted((key, record["value"]) for key, record in scores.items()), "outcome": outcome, "size": (width, height)}
        scene_nodes = [{"kind": "ui_control", "source": "accessibility", "bounds": list(node["bounds"]), "x": (node["bounds"][0] + node["bounds"][2]) // AI_SPATIAL_DIMENSIONS, "y": (node["bounds"][1] + node["bounds"][3]) // AI_SPATIAL_DIMENSIONS, "node_ref": AI_node_reference(node), "package": package, "activity": activity, "enabled": True, "label": targets[AI_node_reference(node)]["label"][:AI_LABEL_FIELD_LIMIT]} for node in clickable]
        descriptor = {"package": package, "activity": activity, "state": state, "legacy_state": legacy_state, "capture_state": observation.get("state"), "size": (width, height), "features": features, "nodes": nodes, "clickable": clickable, "targets": targets, "scores": scores, "phase": phase, "turn": turn, "outcome": outcome, "evidence": evidence, "terminal_source": terminal_source, "points": points, "motion_points": motion_points, "samples": samples, "regions": regions}
        profile = local_agent_game_profile(descriptor)
        descriptor["profile"] = profile
        descriptor["scene_graph"] = local_agent_balanced_scene(scene_nodes, profile["annotations"], regions, self._affordance_annotations(package, phase, (width, height)))
        descriptor["state_match"] = 0.0
        if self._db is not None and phase in {"playing", "unknown"} and visual:
            best_key, best_similarity = self._recurrent_state(features, state)
            descriptor["state_match"] = best_similarity
            if best_key is not None:
                descriptor["state"] = best_key
        return descriptor

    def _visual_terminal_match(self, package, size, visual):
        if self._db is None or not package or not visual:
            return "unknown", ""
        screen = json.dumps(list(size), separators=(",", ":"))
        rows = self._db.execute("SELECT outcome,features,confirmations FROM agent_terminal_templates WHERE package=? AND screen=? AND confirmations>=? ORDER BY confirmations DESC LIMIT ?", (package, screen, LOCAL_AGENT_TERMINAL_TEMPLATE_MIN_EPISODES, LOCAL_AGENT_TERMINAL_TEMPLATE_RECALL)).fetchall()
        estimates = []
        for row in rows:
            try:
                recorded = json.loads(row["features"])
            except (TypeError, ValueError):
                continue
            if not isinstance(recorded, list) or len(recorded) != len(visual):
                continue
            similarity = max(0.0, 1 - sum(abs(a - b) for a, b in zip(visual, recorded)) / (len(visual) * max(1, AI_VISION_STATE_LEVELS - 1)))
            estimates.append((similarity, row["outcome"], row["confirmations"]))
        if not estimates:
            return "unknown", ""
        similarity, outcome, verified_episodes = max(estimates)
        rivals = [score for score, rival, count in estimates if rival != outcome]
        if similarity < LOCAL_AGENT_TERMINAL_TEMPLATE_SIMILARITY or rivals and similarity - max(rivals) <= LOCAL_AGENT_TERMINAL_TEMPLATE_MARGIN:
            return "unknown", ""
        return outcome, "同游戏多局已验证结果画面匹配（" + str(verified_episodes) + " 局）"

    def _remember_terminal_template(self, descriptor):
        if descriptor.get("terminal_source") != "accessibility" or descriptor["outcome"] not in {"win", "loss"}:
            return
        visual = descriptor["features"].get("visual", ())
        if not visual:
            return
        package, outcome = descriptor["package"], descriptor["outcome"]
        screen = json.dumps(list(descriptor["size"]), separators=(",", ":"))
        rows = self._db.execute("SELECT features,confirmations FROM agent_terminal_templates WHERE package=? AND outcome=? AND screen=? ORDER BY confirmations DESC LIMIT ?", (package, outcome, screen, LOCAL_AGENT_TERMINAL_TEMPLATE_RECALL)).fetchall()
        match, best = None, 0.0
        for row in rows:
            try:
                recorded = json.loads(row["features"])
            except (TypeError, ValueError):
                continue
            if not isinstance(recorded, list) or len(recorded) != len(visual):
                continue
            similarity = max(0.0, 1 - sum(abs(a - b) for a, b in zip(visual, recorded)) / (len(visual) * max(1, AI_VISION_STATE_LEVELS - 1)))
            if similarity > best:
                match, best = row["features"], similarity
        if match is not None and best >= LOCAL_AGENT_TERMINAL_TEMPLATE_SIMILARITY:
            self._db.execute("UPDATE agent_terminal_templates SET confirmations=confirmations+1,last_seen=? WHERE package=? AND outcome=? AND screen=? AND features=?", (utc_now(), package, outcome, screen, match))
        else:
            self._db.execute("INSERT INTO agent_terminal_templates(package,outcome,screen,features,confirmations,last_seen) VALUES(?,?,?,?,?,?) ON CONFLICT(package,outcome,screen,features) DO UPDATE SET confirmations=confirmations+1,last_seen=excluded.last_seen", (package, outcome, screen, json.dumps(list(visual), separators=(",", ":")), 1, utc_now()))

    @staticmethod
    def _frame_fresh(observation):
        moment = observation.get("capture_started_at")
        frame = observation.get("frame_id")
        return type(moment) in (int, float) and math.isfinite(moment) and 0 < moment <= time.monotonic() and type(frame) is int and frame > 0

    def _recurrent_state(self, features, fresh_key):
        if self._db.execute("SELECT 1 FROM agent_states WHERE package=? AND state_key=?", (features["package"], fresh_key)).fetchone() is not None:
            return None, 1.0
        rows = self._db.execute("SELECT state_key,features FROM agent_states WHERE package=? AND state_key!=? ORDER BY last_seen DESC LIMIT ?", (features["package"], fresh_key, LOCAL_AGENT_RECURRENT_STATES)).fetchall()
        best_key, best_similarity = None, 0.0
        semantic_key = json.dumps(features["semantic"], ensure_ascii=False, separators=(",", ":"))
        for row in rows:
            try:
                prior = json.loads(row["features"])
            except (ValueError, TypeError):
                continue
            if prior.get("activity") != features["activity"] or prior.get("phase") != features["phase"] or prior.get("size") != list(features["size"]):
                continue
            if json.dumps(prior.get("semantic"), ensure_ascii=False, separators=(",", ":")) != semantic_key or prior.get("score_values", []) != [list(item) for item in features["score_values"]]:
                continue
            similarity = self._feature_similarity(features, prior)
            if similarity > best_similarity:
                best_key = row["state_key"] if similarity > LOCAL_AGENT_RECURRENT_SIMILARITY else None
                best_similarity = similarity
        return best_key, best_similarity

    def _ensure_state(self, descriptor):
        features, seen = json.dumps(descriptor["features"], ensure_ascii=False, separators=(",", ":")), utc_now()
        inserted = self._db.execute("INSERT OR IGNORE INTO agent_states(package,state_key,features,last_seen) VALUES(?,?,?,?)", (descriptor["package"], descriptor["state"], features, seen)).rowcount
        if inserted:
            self._adjust_counts(states=inserted)
        else:
            self._db.execute("UPDATE agent_states SET features=?,last_seen=? WHERE package=? AND state_key=?", (features, seen, descriptor["package"], descriptor["state"]))
        return self._db.execute("SELECT * FROM agent_states WHERE package=? AND state_key=?", (descriptor["package"], descriptor["state"])).fetchone()

    def _session(self, package):
        self._db.execute("INSERT OR IGNORE INTO agent_sessions(package,episode,steps,last_action) VALUES(?,?,0,'')", (package, uuid.uuid4().hex))
        return self._db.execute("SELECT * FROM agent_sessions WHERE package=?", (package,)).fetchone()

    def _discount(self, package):
        if package in self._discount_cache:
            return self._discount_cache[package]
        outcomes = self._db.execute("SELECT AVG(steps) AS horizon FROM agent_outcomes WHERE package=?", (package,)).fetchone()
        sessions = self._db.execute("SELECT MAX(steps) AS horizon FROM agent_sessions WHERE package=?", (package,)).fetchone()
        horizon = max(1.0, local_agent_number(outcomes["horizon"]), local_agent_number(sessions["horizon"]))
        value = horizon / (horizon + 1)
        self._discount_cache[package] = value
        return value

    @staticmethod
    def _cadence(observation):
        perception = observation.get("perception", {})
        perception = perception if isinstance(perception, dict) else {}
        capabilities = observation.get("capabilities", {})
        capabilities = capabilities if isinstance(capabilities, dict) else {}
        refresh = local_agent_number(capabilities.get("refresh_hz"), RUNTIME_BOOTSTRAP_DISPLAY_HZ)
        refresh = refresh if refresh > 0 else RUNTIME_BOOTSTRAP_DISPLAY_HZ
        return max(1 / refresh, local_agent_number(perception.get("frame_interval")), local_agent_number(capabilities.get("input_latency_seconds")))

    @staticmethod
    def _recalled_action_values(history, package):
        weighted = {}
        for entry in history if isinstance(history, (list, tuple)) else ():
            if not isinstance(entry, dict):
                continue
            strategies = entry.get("prior_strategies", ())
            for item in strategies if isinstance(strategies, (list, tuple)) else ():
                if not isinstance(item, dict) or not isinstance(item.get("action_relative_1000"), dict):
                    continue
                if item.get("game") != package:
                    continue
                similarity = max(0.0, min(1.0, local_agent_number(item.get("state_similarity"))))
                uncertainty = max(0.0, min(1.0, local_agent_number(item.get("uncertainty"), 1.0)))
                outcomes = max(0.0, local_agent_number(item.get("outcome_trials")))
                effects = max(0.0, local_agent_number(item.get("effect_trials")))
                if outcomes:
                    feedback = max(-1.0, min(1.0, local_agent_number(item.get("outcome_return"))))
                    count = outcomes
                elif effects:
                    feedback = max(-1.0, min(1.0, 2 * local_agent_number(item.get("effect_success_rate"), 1 / AI_SPATIAL_DIMENSIONS) - 1))
                    count = effects
                else:
                    continue
                strength = similarity * (1 - uncertainty) * count / (count + 1)
                if strength <= 0:
                    continue
                key = local_agent_memory_action_key(item["action_relative_1000"])
                total, evidence, matches = weighted.get(key, (0.0, 0.0, 0))
                weighted[key] = (total + strength * feedback, evidence + strength, matches + 1)
        return {key: (total / max(1.0, evidence), matches) for key, (total, evidence, matches) in weighted.items()}

    def _candidates(self, descriptor, observation, state_visits):
        width, height = descriptor["size"]
        supported = observation.get("capabilities", {}).get("actions", AI_ACTION_KINDS)
        capabilities = observation.get("capabilities", {})
        cadence = self._cadence(observation)
        duration = max(1, math.ceil(cadence * AI_MILLISECONDS_PER_SECOND))
        hold_ms = max(duration, math.ceil(local_agent_number(capabilities.get("long_press_ms"), AI_ANDROID_LONG_PRESS_INITIAL_MS)))
        active = [dict(point) for point in observation.get("active_touches", []) if isinstance(point, dict) and all(type(point.get(key)) is int for key in ("id", "x", "y"))]
        slots = max(1, int(local_agent_number(capabilities.get("touch_slots", capabilities.get("max_pointers")), 1)))
        available_ids = [identifier for identifier in range(slots) if identifier not in {point["id"] for point in active}]
        choices = {}
        def add(action, source, label="", target=None, prior=0.0, recalled_key=None, evidence=""):
            if action.get("kind") not in supported:
                return
            if action.get("kind") in {"tap", "long_press", "swipe"} and not available_ids:
                return
            if action.get("kind") == "touch" and any(point.get("id") not in available_ids for point in action.get("pointers", [])):
                return
            if action.get("kind") == "touch_begin" and any(point.get("id") not in available_ids for point in action.get("pointers", [])):
                return
            if action.get("kind") == "touch_update" and any(point.get("id") not in {held["id"] for held in active} for point in action.get("pointers", [])):
                return
            if action.get("kind") == "touch_end" and any(identifier not in {held["id"] for held in active} for identifier in action.get("ids", [])):
                return
            try:
                normalized = normalize_action(action, observation)
                relative = relative_action(normalized, (width, height))
            except (ValueError, TypeError, OverflowError):
                return
            signature = local_agent_learning_signature(relative, target)
            key = recalled_key or hashlib.sha256(json.dumps(signature, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()
            if key in choices:
                return
            conditions = [{"kind": "package", "value": descriptor["package"]}] if descriptor["package"] else []
            if descriptor["activity"]:
                conditions.append({"kind": "activity", "value": descriptor["activity"]})
            expected_effect = {}
            if target is not None:
                conditions.append({"kind": "node_enabled", "value": AI_node_reference(target)})
                if evidence:
                    conditions.append({"kind": "visible_text", "value": evidence})
                if normalized["kind"] == "tap" and target.get("checkable") is True:
                    checked = target.get("checked") is True
                    conditions.append({"kind": "node_state", "value": AI_node_reference(target), "field": "checked", "expected": checked})
                    expected_effect = {"kind": "node_state", "node_ref": AI_node_reference(target), "field": "checked", "value": not checked}
            if normalized["kind"] in {"touch_update", "touch_end"}:
                identifiers = [point["id"] for point in normalized.get("pointers", [])] if normalized["kind"] == "touch_update" else normalized.get("ids") or [point["id"] for point in active]
                conditions.extend({"kind": "active_pointer", "value": str(identifier)} for identifier in identifiers)
            if normalized["kind"] in {"touch", "touch_begin"}:
                conditions.extend({"kind": "available_pointer", "value": str(point["id"])} for point in normalized["pointers"])
            choices[key] = {"key": key, "action": normalized, "relative": relative, "source": source, "label": label, "preconditions": conditions, "expected_effect": expected_effect, "prior": prior, "recalled": recalled_key is not None}
        if descriptor["phase"] == "loading" and not descriptor["clickable"]:
            add({"kind": "wait", "ms": duration}, "loading_observation", "观察加载状态")
            return list(choices.values())
        if descriptor.get("turn") == "opponent" and descriptor["outcome"] == "unknown" and not any(target["navigation"] for target in descriptor["targets"].values()):
            add({"kind": "wait", "ms": duration}, "opponent_turn_observation", "对方回合：继续观察游戏状态")
            return list(choices.values())
        for semantic_action, label, prior, target in local_agent_semantic_actions(descriptor):
            add(semantic_action, "game_specific_observed_control", label, target=target, prior=prior)
        for profile_action, label, prior in local_agent_profile_actions(descriptor, observation):
            add(profile_action, "offline_game_layout", label, prior=prior)
        for node in descriptor["clickable"]:
            left, top, right, bottom = node["bounds"]
            x, y = (left + right - 1) // 2, (top + bottom - 1) // 2
            target = descriptor["targets"][AI_node_reference(node)]
            label = target["label"]
            prior = 1 / (len(descriptor["clickable"]) + 1) if target["navigation"] else 0.0
            add({"kind": "tap", "x": x, "y": y, "ms": duration}, "accessibility_target", label, node, prior, evidence=target["evidence"])
            if node.get("long_clickable") is True or node.get("long-clickable") is True:
                add({"kind": "long_press", "x": x, "y": y, "ms": hold_ms}, "accessibility_long_press", label, node)
        for node in descriptor["nodes"]:
            if node.get("enabled", True) is not True or node.get("scrollable") is not True:
                continue
            bounds = node.get("bounds", ())
            if len(bounds) != AI_BOUNDING_BOX_COMPONENTS or any(type(value) is not int for value in bounds):
                continue
            left, top, right, bottom = bounds
            if not 0 <= left < right <= width or not 0 <= top < bottom <= height:
                continue
            x, y = (left + right - 1) // 2, (top + bottom - 1) // 2
            for dx, dy in LOCAL_AGENT_DIRECTIONS:
                x2, y2 = x + dx * max(1, (right - left) // len(LOCAL_AGENT_DIRECTIONS)), y + dy * max(1, (bottom - top) // len(LOCAL_AGENT_DIRECTIONS))
                add({"kind": "swipe", "x": x, "y": y, "x2": min(width - 1, max(0, x2)), "y2": min(height - 1, max(0, y2)), "ms": max(duration, hold_ms // 2)}, "accessibility_scroll", "滚动可访问容器")
        motion_points = list(descriptor.get("motion_points", ()))
        region_targets = [region for region in descriptor.get("regions", ()) if not any(node["bounds"][0] <= region["x"] < node["bounds"][2] and node["bounds"][1] <= region["y"] < node["bounds"][3] for node in descriptor["clickable"])]
        for region in region_targets if not descriptor["clickable"] or descriptor["phase"] == "playing" else ():
            x, y = region["x"], region["y"]
            prior = AI_VISUAL_CONTROL_PRIOR * min(1.0, region["strength"] + region["motion"])
            add({"kind": "tap", "x": x, "y": y, "ms": duration}, "visual_region", "本地画面区域：" + region["kind"], prior=prior)
        prioritized = [(region["x"], region["y"], region["strength"] + region["motion"]) for region in region_targets] + sorted(motion_points, key=lambda item: item[2], reverse=True) + list(descriptor["points"])
        unique = {}
        for x, y, score in prioritized:
            unique.setdefault((x, y), (x, y, score))
        points = list(unique.values())
        control_anchors = tuple(points)
        visual = descriptor["features"]["visual"]
        colors = {visual[index:index + AI_RGB_CHANNELS] for index in range(0, len(visual), AI_RGB_CHANNELS)}
        perception = observation.get("perception", {})
        perception = perception if isinstance(perception, dict) else {}
        moving = local_agent_number(perception.get("motion")) > local_agent_number(perception.get("noise_floor"), 1 / AI_BYTE_MAX)
        visual_evidence = len(colors) > 1 or moving
        navigation = any(target["navigation"] for target in descriptor["targets"].values())
        gameplay_exploration = descriptor["phase"] == "playing" or bool(state_visits and visual_evidence and not navigation)
        if gameplay_exploration:
            for region in region_targets:
                if region["kind"] in {"movement_control", "action_control"}:
                    add({"kind": "long_press", "x": region["x"], "y": region["y"], "ms": hold_ms}, "visual_control_hold", "探索屏幕下部持续控制", prior=AI_VISUAL_CONTROL_PRIOR * region["strength"])
                    if available_ids:
                        add({"kind": "touch_begin", "pointers": [{"id": available_ids[0], "x": region["x"], "y": region["y"]}], "ms": duration}, "visual_control_touch", "探索连续游戏控制", prior=AI_VISUAL_CONTROL_PRIOR * region["strength"])
            if "keyevent" in supported:
                for direction in LOCAL_AGENT_DIRECTIONS:
                    key = {(0, -1): "KEYCODE_DPAD_UP", (0, 1): "KEYCODE_DPAD_DOWN", (-1, 0): "KEYCODE_DPAD_LEFT", (1, 0): "KEYCODE_DPAD_RIGHT"}[direction]
                    add({"kind": "keyevent", "key": key}, "keyboard_gameplay", "探索方向键控制")
        if self._db is not None and descriptor["phase"] in {"playing", "unknown"} and descriptor["package"]:
            remembered_controls = self._db.execute("SELECT action,demonstrations,reward_samples,reward_sum,effect_samples,effect_sum FROM agent_affordances WHERE package=? AND phase=? AND (demonstrations>0 OR reward_sum>0 OR effect_sum>0) ORDER BY demonstrations DESC,reward_sum DESC,effect_sum DESC LIMIT ?", (descriptor["package"], descriptor["phase"], LOCAL_AGENT_AFFORDANCE_RECALL)).fetchall()
            for record in remembered_controls:
                try:
                    restored = local_agent_absolute_action(json.loads(record["action"]), descriptor["size"])
                    prior = LOCAL_AGENT_AFFORDANCE_WEIGHT * (record["demonstrations"] / (record["demonstrations"] + 1) + max(0.0, record["reward_sum"]) / (record["reward_samples"] + 1) + max(0.0, record["effect_sum"]) / (record["effect_samples"] + 1))
                    add(restored, "learned_affordance", "复用当前游戏跨画面的已学控制热区", prior=prior)
                except (TypeError, ValueError, KeyError, OverflowError):
                    continue
        if descriptor["phase"] == "unknown" and not visual_evidence and state_visits == 0:
            add({"kind": "wait", "ms": duration}, "unknown_observation", "等待画面出现可辨认信息")
        if (descriptor["phase"] != "unknown" or visual_evidence or state_visits > 0) and (not descriptor["clickable"] or gameplay_exploration):
            count = min(LOCAL_AGENT_CANDIDATE_EXPLORATION_LIMIT, max(1, math.isqrt(state_visits + max(1, len(points)))))
            points = points[:count]
            for index in range(1, count + 1):
                exploratory_index = state_visits + index
                x = min(width - 1, round(local_agent_halton(exploratory_index, LOCAL_AGENT_HALTON_BASES[0]) * (width - 1)))
                y = min(height - 1, round(local_agent_halton(exploratory_index, LOCAL_AGENT_HALTON_BASES[1]) * (height - 1)))
                if (x, y) not in {(point[0], point[1]) for point in points}:
                    points.append((x, y, 0.0))
            cell_width = max(1, width // max(1, math.isqrt(math.ceil(math.sqrt(width)))))
            cell_height = max(1, height // max(1, math.isqrt(math.ceil(math.sqrt(height)))))
            for x, y, salience in points:
                add({"kind": "tap", "x": x, "y": y, "ms": duration}, "visual_exploration", "探索视觉区域")
                add({"kind": "long_press", "x": x, "y": y, "ms": hold_ms}, "visual_hold", "探索长按控制")
                for dx, dy in LOCAL_AGENT_DIRECTIONS:
                    x2, y2 = min(width - 1, max(0, x + dx * cell_width)), min(height - 1, max(0, y + dy * cell_height))
                    if (x2, y2) != (x, y):
                        motion_ms = max(duration, math.ceil(hold_ms * math.hypot(x2 - x, y2 - y) / max(1, math.hypot(width, height))))
                        add({"kind": "swipe", "x": x, "y": y, "x2": x2, "y2": y2, "ms": motion_ms}, "visual_drag", "探索方向拖动")
        if active:
            add({"kind": "touch_release_all"}, "held_control_release", "释放持续触控")
            for point in active:
                add({"kind": "touch_end", "ids": [point["id"]]}, "held_control_release", "释放一个持续触点")
                for dx, dy in LOCAL_AGENT_DIRECTIONS:
                    step_x = max(1, width // max(1, math.isqrt(math.ceil(math.sqrt(width)))))
                    step_y = max(1, height // max(1, math.isqrt(math.ceil(math.sqrt(height)))))
                    moved = dict(point, x=min(width - 1, max(0, point["x"] + dx * step_x)), y=min(height - 1, max(0, point["y"] + dy * step_y)))
                    update = [moved if held["id"] == point["id"] else held for held in active]
                    add({"kind": "touch_update", "pointers": update, "ms": duration}, "held_control_update", "调整持续触控方向")
            add({"kind": "wait", "ms": duration}, "held_control_observation", "维持控制并观察")
        if (gameplay_exploration or descriptor["phase"] == "unknown" and visual_evidence and (state_visits or moving)) and available_ids:
            for x, y, salience in points:
                add({"kind": "touch_begin", "pointers": [{"id": available_ids[0], "x": x, "y": y}], "ms": duration}, "continuous_control_probe", "开始持续触控")
            if len(available_ids) > 1 and len(points) > 1:
                ordered = sorted(control_anchors if len(control_anchors) > 1 else points, key=lambda point: (point[0], point[1]))
                left, right = ordered[0], ordered[-1]
                if left[:2] != right[:2]:
                    simultaneous = [{"id": identifier, "x": point[0], "y": point[1]} for identifier, point in zip(available_ids, (left, right))]
                    add({"kind": "touch", "pointers": simultaneous, "ms": max(duration, hold_ms // 2)}, "simultaneous_control_probe", "探索双点同时控制")
        if state_visits and not descriptor["scores"] and descriptor["phase"] == "menu" and not navigation:
            add({"kind": "back"}, "navigation_recovery", "菜单无可见前进操作时尝试返回")
        if not choices:
            add({"kind": "wait", "ms": duration}, "observation", "继续观察可执行控制")
        if self._db is not None:
            retained = max(1, math.isqrt(state_visits + len(choices)))
            demonstration_actions = self._db.execute("SELECT action_key,action,source,preconditions,label,demonstrations FROM agent_actions WHERE package=? AND state_key=? AND demonstrations>0 ORDER BY demonstrations DESC,action_key", (descriptor["package"], descriptor["state"])).fetchall()
            legacy_actions = self._db.execute("SELECT action_key,action,source,preconditions,label,demonstrations FROM agent_actions WHERE package=? AND state_key=? AND demonstrations>0 ORDER BY demonstrations DESC,action_key", (descriptor["package"], descriptor["legacy_state"])).fetchall() if descriptor["legacy_state"] != descriptor["state"] else ()
            experienced_actions = self._db.execute("SELECT action_key,action,source,preconditions,label,demonstrations FROM agent_actions WHERE package=? AND state_key=? AND visits>0 AND demonstrations=0 ORDER BY q DESC,visits DESC,action_key LIMIT ?", (descriptor["package"], descriptor["state"], retained)).fetchall()
            for learned in (*demonstration_actions, *legacy_actions, *experienced_actions):
                if learned["action_key"] in choices:
                    continue
                try:
                    relative = json.loads(learned["action"])
                    conditions = json.loads(learned["preconditions"])
                    if not isinstance(relative, dict) or not self._preconditions_hold(conditions, observation):
                        continue
                    source = str(learned["source"] or "learned_control")
                    targets = [condition["value"] for condition in conditions if condition.get("kind") == "node_enabled"]
                    target = None
                    action = local_agent_restore_action(relative, conditions, observation)
                    evidence = ""
                    if targets:
                        if len(targets) != 1:
                            continue
                        matches = AI_matching_nodes(descriptor["clickable"], targets[0])
                        if len(matches) != 1 or action.get("kind") not in {"tap", "long_press"}:
                            continue
                        target = matches[0]
                        evidence = descriptor["targets"][AI_node_reference(target)]["evidence"]
                    elif not learned["source"]:
                        signature = local_agent_learning_signature(relative)
                        legacy = action_signature(relative)
                        legacy.pop("ms", None)
                        identifiers = {hashlib.sha256(json.dumps(item, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest() for item in (signature, legacy)}
                        if learned["action_key"] not in identifiers:
                            continue
                    add(action, source, str(learned["label"] or "复用已执行的控制经验"), target=target, recalled_key=learned["action_key"], evidence=evidence, prior=LOCAL_AGENT_DEMONSTRATION_PRIOR if learned["demonstrations"] else 0.0)
                except (ValueError, TypeError, KeyError, OverflowError):
                    continue
        return list(choices.values())

    def _register_candidates(self, descriptor, candidates):
        keys = {candidate["key"] for candidate in candidates}
        rows = {}
        batch_size = AI_MEMORY_DEFAULT_RECALL * AI_MEMORY_DEFAULT_RECALL
        sequence = tuple(keys)
        for offset in range(0, len(sequence), batch_size):
            batch = sequence[offset:offset + batch_size]
            markers = ",".join("?" for _ in batch)
            query = "SELECT * FROM agent_actions WHERE package=? AND state_key=? AND action_key IN (" + markers + ")"
            for row in self._db.execute(query, (descriptor["package"], descriptor["state"], *batch)):
                rows[row["action_key"]] = row
        for candidate in candidates:
            key = candidate["key"]
            if key not in rows:
                rows[key] = {"visits": 0, "demonstrations": 0, "q": 0.0, "iq": 0.0, "effect_samples": 0, "effect_sum": 0.0, "reward_samples": 0}
        return rows

    def _persist_selected_candidate(self, descriptor, candidate):
        values = (json.dumps(candidate["relative"], ensure_ascii=False, separators=(",", ":")), candidate["source"], json.dumps(candidate["preconditions"], ensure_ascii=False, separators=(",", ":")), candidate["label"])
        identity = (descriptor["package"], descriptor["state"], candidate["key"])
        inserted = self._db.execute("INSERT OR IGNORE INTO agent_actions(package,state_key,action_key,action,source,preconditions,label) VALUES(?,?,?,?,?,?,?)", identity + values).rowcount
        if inserted:
            self._adjust_counts(actions=inserted)
        else:
            self._db.execute("UPDATE agent_actions SET action=?,source=?,preconditions=?,label=? WHERE package=? AND state_key=? AND action_key=? AND demonstrations=0 AND (action!=? OR source!=? OR preconditions!=? OR label!=?)", values + identity + values)

    def _refresh_value(self, package, state):
        old = self._db.execute("SELECT value,intrinsic_value FROM agent_states WHERE package=? AND state_key=?", (package, state)).fetchone()
        row = self._db.execute("SELECT MAX(q) AS value,MAX(iq) AS intrinsic_value FROM agent_actions WHERE package=? AND state_key=?", (package, state)).fetchone()
        value, intrinsic = local_agent_number(row["value"]), local_agent_number(row["intrinsic_value"])
        self._db.execute("UPDATE agent_states SET value=?,intrinsic_value=? WHERE package=? AND state_key=?", (value, intrinsic, package, state))
        return max(abs(value - local_agent_number(old["value"] if old is not None else 0)), abs(intrinsic - local_agent_number(old["intrinsic_value"] if old is not None else 0)))

    def _enqueue(self, package, state, action, priority):
        key = (package, state, action)
        priority = abs(local_agent_number(priority))
        if priority <= self._priorities.get(key, 0.0):
            return
        self._priorities[key] = priority
        heapq.heappush(self._planning, (-priority, key))
        if len(self._planning) > max(LOCAL_AGENT_PLANNING_BACKUP_LIMIT, len(self._priorities) * LOCAL_AGENT_PLANNING_STALE_RATIO):
            self._planning = [(-score, identity) for identity, score in self._priorities.items()]
            heapq.heapify(self._planning)

    def _predecessors(self, package, state, priority):
        for row in self._db.execute("SELECT DISTINCT state_key,action_key FROM agent_transitions WHERE package=? AND next_state=? AND terminal=0", (package, state)):
            self._enqueue(package, row["state_key"], row["action_key"], priority)

    def _backup_action(self, package, state, action):
        row = self._db.execute("SELECT q,iq FROM agent_actions WHERE package=? AND state_key=? AND action_key=?", (package, state, action)).fetchone()
        transitions = self._db.execute("SELECT t.*,s.value,s.intrinsic_value,s.visits AS next_visits FROM agent_transitions t JOIN agent_states s ON s.package=t.package AND s.state_key=t.next_state WHERE t.package=? AND t.state_key=? AND t.action_key=?", (package, state, action)).fetchall()
        count = sum(item["visits"] for item in transitions)
        if row is None or not count:
            return 0.0
        discount = self._discount(package)
        q = sum(item["reward_sum"] + item["visits"] * (0.0 if item["terminal"] else discount * item["value"]) for item in transitions) / count
        iq = sum(item["visits"] * ((1 / math.sqrt(item["next_visits"] + 1) if item["next_state"] != state else 0.0) + (0.0 if item["terminal"] else discount * item["intrinsic_value"])) for item in transitions) / count
        self._db.execute("UPDATE agent_actions SET q=?,iq=? WHERE package=? AND state_key=? AND action_key=?", (q, iq, package, state, action))
        error = max(abs(q - row["q"]), abs(iq - row["iq"]))
        changed = self._refresh_value(package, state)
        if changed > 0:
            self._predecessors(package, state, changed)
        return error

    def _replay(self, deadline, capacity, cancel=None, generation=None):
        completed = 0
        while self._planning and completed < capacity:
            self._check(cancel, generation)
            if completed and time.monotonic() >= deadline:
                break
            negative, key = heapq.heappop(self._planning)
            if self._priorities.get(key) != -negative:
                continue
            self._priorities.pop(key, None)
            self._backup_action(*key)
            completed += 1
        self._stats["planning_backups"] += completed
        return completed

    def _process_outcome(self, descriptor, observation, report=True):
        package = descriptor["package"]
        fresh = self._frame_fresh(observation) if descriptor.get("terminal_source") == "learned_visual_template" else self._nodes_fresh(observation)
        if descriptor["outcome"] == "unknown" or not fresh:
            self._terminal_candidates.pop(package, None)
            return False
        marker = (descriptor["outcome"], descriptor["evidence"])
        frame = int(local_agent_number(observation.get("frame_id")))
        captured = local_agent_number(observation.get("capture_started_at", observation.get("timestamp")))
        nodes_at = local_agent_number(observation.get("nodes_at"))
        current = {"marker": marker, "frame": frame, "captured": captured, "nodes_at": nodes_at}
        prior = self._terminal_candidates.get(package)
        if prior is None or prior["marker"] != marker:
            self._terminal_candidates[package] = current
            return False
        fresh_nodes = descriptor.get("terminal_source") == "accessibility"
        if (fresh_nodes and nodes_at <= prior["nodes_at"]) or captured <= prior["captured"] or frame <= prior["frame"]:
            return bool(prior.get("confirmed"))
        if prior.get("confirmed"):
            current["confirmation_frames"] = list(prior.get("confirmation_frames", ()))
        elif prior["frame"] > 0 and frame > 0:
            current["confirmation_frames"] = [prior["frame"], frame]
        else:
            self._terminal_candidates[package] = current
            return False
        current["confirmed"] = True
        self._terminal_candidates[package] = current
        session = self._session(package)
        if session["terminal_latched"]:
            return True
        observed = self._db.execute("SELECT * FROM agent_observed WHERE action_id=? AND package=? AND episode=?", (session["last_action"], package, session["episode"])).fetchone()
        action_fresh = bool(observed is not None and (self._nodes_fresh(observation, observed["applied_at"]) if fresh_nodes else self._frame_fresh(observation) and prior["captured"] > observed["applied_at"]))
        if observed is None or observed["applied_at"] <= self._input_epoch_started_at or not action_fresh or prior["captured"] <= observed["applied_at"]:
            self._terminal_candidates.pop(package, None)
            return False
        origin = self._db.execute("SELECT features FROM agent_states WHERE package=? AND state_key=?", (package, observed["state_key"])).fetchone()
        try:
            origin_phase = json.loads(origin["features"]).get("phase") if origin is not None else "unknown"
        except (TypeError, ValueError):
            origin_phase = "unknown"
        if origin_phase != "playing":
            self._terminal_candidates.pop(package, None)
            return False
        self._ensure_state(descriptor)
        reward = 1.0 if descriptor["outcome"] == "win" else -1.0
        prior_key = (package, observed["state_key"], observed["action_key"], observed["next_state"], observed["terminal"])
        self._db.execute("UPDATE agent_transitions SET visits=visits-1,reward_sum=reward_sum-?,intrinsic_sum=intrinsic_sum-?,reward_samples=reward_samples-?,seconds_sum=seconds_sum-? WHERE package=? AND state_key=? AND action_key=? AND next_state=? AND terminal=?", (observed["reward"], observed["intrinsic"], observed["verified"], observed["seconds"], *prior_key))
        removed = self._db.execute("DELETE FROM agent_transitions WHERE package=? AND state_key=? AND action_key=? AND next_state=? AND terminal=? AND visits<=0", prior_key).rowcount
        self._adjust_counts(model_edges=-removed)
        combined = observed["reward"] + reward
        duration = max(observed["seconds"], captured - observed["applied_at"])
        self._add_model_transition(package, observed["state_key"], observed["action_key"], descriptor["state"], True, combined, observed["intrinsic"], True, duration)
        if observed["verified"]:
            self._db.execute("UPDATE agent_transitions SET reward_samples=reward_samples+1 WHERE package=? AND state_key=? AND action_key=? AND next_state=? AND terminal=1", (package, observed["state_key"], observed["action_key"], descriptor["state"]))
        self._db.execute("UPDATE agent_actions SET reward_sum=reward_sum+?,reward_samples=reward_samples+1 WHERE package=? AND state_key=? AND action_key=?", (reward, package, observed["state_key"], observed["action_key"]))
        if origin is not None:
            original_phase = json.loads(origin["features"]).get("phase", "unknown")
            selected_record = self._db.execute("SELECT action FROM agent_actions WHERE package=? AND state_key=? AND action_key=?", (package, observed["state_key"], observed["action_key"])).fetchone()
            if selected_record is not None:
                with contextlib.suppress(ValueError, TypeError):
                    self._learn_affordance(package, original_phase, json.loads(selected_record["action"]), reward_verified=True, reward=reward)
        self._record_sample_counts(package, rewards=1)
        self._db.execute("UPDATE agent_observed SET next_state=?,terminal=1,reward=?,verified=1,seconds=?,evidence=? WHERE action_id=?", (descriptor["state"], combined, duration, descriptor["evidence"], observed["action_id"]))
        inserted = self._db.execute("INSERT OR IGNORE INTO agent_outcomes(episode,package,outcome,evidence,action_id,steps,verified_at) VALUES(?,?,?,?,?,?,?)", (session["episode"], package, descriptor["outcome"], descriptor["evidence"], observed["action_id"], session["steps"], utc_now())).rowcount
        self._adjust_counts(verified_episodes=inserted, **{"wins" if descriptor["outcome"] == "win" else "losses": inserted})
        self._discount_cache.pop(package, None)
        self._db.execute("UPDATE agent_sessions SET terminal_latched=1 WHERE package=?", (package,))
        self._remember_terminal_template(descriptor)
        error = self._backup_action(package, observed["state_key"], observed["action_key"])
        self._enqueue(package, observed["state_key"], observed["action_key"], max(abs(reward), error))
        if report:
            self.log("local_terminal_reward", package=package, outcome=descriptor["outcome"], evidence=descriptor["evidence"], reward=reward, action_id=observed["action_id"], source="verified_visual_template" if descriptor.get("terminal_source") == "learned_visual_template" else "distinct_fresh_accessibility_results", attribution="single_terminal_reward_with_td_propagation")
        return True

    def inspect_outcome(self, png, cancel=None, observation=None):
        self._check(cancel)
        frame_dimensions(png)
        if not isinstance(observation, dict):
            return {"outcome": "unknown", "score": None, "health": None, "evidence": "", "source": "fresh_accessibility_unavailable"}
        with self._lock, self._transaction():
            if self._db is None:
                return {"outcome": "unknown", "score": None, "health": None, "evidence": "", "source": "agent_stopped"}
            descriptor = self._describe(observation, png)
            confirmed = self._process_outcome(descriptor, observation)
            confirmation = self._terminal_candidates.get(descriptor["package"], {}) if confirmed else {}
            return {"outcome": descriptor["outcome"] if confirmed else "unknown", "score": None, "health": None, "evidence": descriptor["evidence"] if confirmed else "", "verified": bool(confirmed), "confirmation_frames": list(confirmation.get("confirmation_frames", ())), "source": ("verified_visual_template" if descriptor.get("terminal_source") == "learned_visual_template" else "distinct_fresh_accessibility_results") if confirmed else "awaiting_distinct_result_frames"}

    def plan(self, observation, png, history=(), cancel=None, _commit=True):
        generation = self._cancel_generation
        self._check(cancel, generation)
        if not self.alive() or not self._healthy:
            raise ComponentFailure("ai", "本地在线学习器尚未就绪，正在恢复")
        started = time.monotonic()
        self._deadline = started + max(self._cadence(observation), sum(self.timings) / max(1, len(self.timings)))
        try:
            with self._lock, self._transaction(enabled=_commit):
                self._check(cancel, generation)
                if self._db is None or not self._started:
                    raise Cancelled()
                descriptor = self._describe(observation, png)
                state_row = self._ensure_state(descriptor)
                confirmed = self._process_outcome(descriptor, observation, report=_commit)
                candidates = self._candidates(descriptor, observation, state_row["visits"])
                if not candidates:
                    raise ValueError("设备没有提供任何可执行动作")
                replay_capacity = min(LOCAL_AGENT_PLANNING_BACKUP_LIMIT, max(1, math.isqrt(self._stats["td_updates"] + 1)))
                backups = self._replay(self._deadline, replay_capacity, cancel, generation)
                rows = self._register_candidates(descriptor, candidates)
                recalled = self._recalled_action_values(history, descriptor["package"])
                transferred = self._transfer_values(descriptor, candidates)
                affordances = self._affordance_values(descriptor, candidates)
                package_samples = self._package_samples(descriptor["package"])
                reward_samples = int(package_samples["rewards"])
                intrinsic_weight = 1 / math.sqrt(reward_samples + 1)
                discount = self._discount(descriptor["package"])
                total = max(1, state_row["visits"] + len(candidates))
                ranked = []
                for candidate in candidates:
                    row = rows[candidate["key"]]
                    candidate["demonstration_restored"] = False
                    if row["demonstrations"]:
                        try:
                            preserved = json.loads(row["action"])
                            requirements = json.loads(row["preconditions"])
                            restored = local_agent_restore_action(preserved, requirements, observation)
                            candidate["action"] = restored
                            candidate["relative"] = relative_action(restored, descriptor["size"])
                            candidate["source"] = "human_demonstration"
                            candidate["demonstration_restored"] = True
                        except (ValueError, TypeError, KeyError, OverflowError):
                            pass
                    effect_samples = row["effect_samples"]
                    visual_effect = row["effect_sum"] / effect_samples if effect_samples else 0.0
                    no_effect_penalty = 0.0
                    if effect_samples >= AI_SPATIAL_DIMENSIONS and not row["reward_samples"]:
                        noise = max(LOCAL_AGENT_EFFECT_MINIMUM, local_agent_number(observation.get("perception", {}).get("noise_floor") if isinstance(observation.get("perception"), dict) else None))
                        no_effect_rate = max(0.0, 1 - min(1.0, visual_effect / noise))
                        no_effect_penalty = AI_VISUAL_FEEDBACK_WEIGHT * no_effect_rate * effect_samples / (effect_samples + 1)
                    uncertainty = math.sqrt(LOCAL_AGENT_HOEFFDING_FACTOR * math.log(total + 1) / (row["visits"] + 1))
                    if reward_samples:
                        uncertainty *= max(LOCAL_AGENT_REWARD_EXPLORATION_ATTENUATION, 1 / math.sqrt(reward_samples + 1))
                    intrinsic = (1 - discount) * row["iq"] * intrinsic_weight
                    recalled_bonus, remembered = recalled.get(local_agent_memory_action_key(candidate["relative"]), (0.0, 0))
                    transfer_bonus, transferred_count = transferred.get(candidate["key"], (0.0, 0))
                    demonstration_bonus = LOCAL_AGENT_DEMONSTRATION_PRIOR * row["demonstrations"] / (row["demonstrations"] + 1) / (row["visits"] + 1) if candidate["demonstration_restored"] else 0.0
                    affordance_record = affordances.get(local_agent_affordance_bucket(candidate["relative"]))
                    affordance_bonus = 0.0
                    if affordance_record:
                        effects = affordance_record["effect_samples"]
                        rewards = affordance_record["reward_samples"]
                        demos = affordance_record["demonstrations"]
                        affordance_bonus = LOCAL_AGENT_AFFORDANCE_WEIGHT * (affordance_record["effect_sum"] / (effects + 1) + affordance_record["reward_sum"] / (rewards + 1) + demos / (demos + 1))
                    value = row["q"] + intrinsic + uncertainty + candidate["prior"] / (row["visits"] + 1) + demonstration_bonus + recalled_bonus + transfer_bonus + AI_VISUAL_FEEDBACK_WEIGHT * visual_effect * effect_samples / (effect_samples + 1) + affordance_bonus - no_effect_penalty
                    candidate["no_effect_penalty"] = no_effect_penalty
                    ranked.append((value, -row["visits"], candidate["key"], candidate, row, uncertainty, intrinsic, recalled_bonus, remembered, transfer_bonus, transferred_count, affordance_bonus, affordance_record))
                _, _, _, selected, learned, uncertainty, intrinsic, recalled_bonus, remembered, transfer_bonus, transferred_count, selected_affordance_bonus, selected_affordance = max(ranked, key=lambda item: item[:3])
                self._persist_selected_candidate(descriptor, selected)
                self._plan_serial += 1
                self._stats["decisions"] += 1
                self._last_descriptors[descriptor["package"]] = descriptor
                self._save_statistics()
                reward_source = "fresh_accessibility_score" if descriptor["scores"] else "explicit_result_label" if descriptor["outcome"] != "unknown" else "unavailable"
                goal = "优化已识别的显式分数反馈；完整游戏目标仍需可验证证据" if descriptor["scores"] else "根据已验证的结果学习策略" if reward_samples else "目标尚未识别；探索控件及可观测状态转移"
                profile_goal = descriptor["profile"].get("objective", "")
                if descriptor["profile"].get("game_id") != "unclassified" and profile_goal:
                    goal += "；" + profile_goal
                kind = selected["action"]["kind"]
                mode = "continuous" if kind.startswith("touch_") or observation.get("active_touches") else "touch"
                evidence = {"algorithm": "UCB + TD + empirical transition replay", "valid_candidates": len(candidates), "matched_observations": learned["visits"], "visits": learned["visits"], "demonstrations": learned["demonstrations"], "uncertainty": uncertainty, "exploration_bonus": uncertainty, "learned_value": learned["q"], "intrinsic_value": intrinsic, "verified_reward_samples": reward_samples, "transition_samples": int(package_samples["transitions"]), "planning_backups": backups, "reward_source": reward_source, "goal_known": bool(reward_samples or descriptor["scores"]), "mode": "reward_learning" if reward_samples else "exploration", "action_source": "human_demonstration" if selected["demonstration_restored"] else selected["source"], "recalled_experience_matches": remembered, "recalled_experience_bonus": recalled_bonus, "similar_state_reward_matches": transferred_count, "similar_state_reward_bonus": transfer_bonus, "cross_scene_control_matches": len(affordances), "cross_scene_control_bonus": selected_affordance_bonus, "cross_scene_control_attempts": selected_affordance["attempts"] if selected_affordance else 0, "repeated_no_effect_penalty": selected.get("no_effect_penalty", 0.0), "motion_targets": len(descriptor.get("motion_points", ())), "confidence_kind": "action_sample_support", "professional_skill_verified": False}
                assessment = ("已执行动作证据 " + str(learned["visits"]) + " 次；" + ("利用已观测奖励与真实转移模型" if reward_samples else "暂无可靠成绩反馈，当前按访问次数与状态新奇度探索") + "。" + LOCAL_AGENT_LIMITATION)
                actions = [selected["action"]]
                result = {"game": descriptor["package"] or "当前安卓应用", "phase": descriptor["phase"], "task_state": {"goal": goal, "control_mode": mode, "turn": descriptor["turn"], "state_key": descriptor["state"], "rules": []}, "actions": actions, "confidence": learned["visits"] / (learned["visits"] + 1), "confidence_kind": "action_sample_support", "assessment": assessment, "expected": selected["label"] + "；效果将在实际执行后的新观察中核实", "reward_signal": {"outcome": descriptor["outcome"] if confirmed else "unknown", "score": next(iter(descriptor["scores"].values()))["value"] if len(descriptor["scores"]) == 1 else None, "health": None, "evidence": descriptor["evidence"] if confirmed else "", "verified": bool(confirmed), "confirmation_frames": list(self._terminal_candidates.get(descriptor["package"], {}).get("confirmation_frames", ())) if confirmed else []}, "preconditions": selected["preconditions"], "policy_evidence": evidence, "execution_capacity": len(actions), "local_policy": {"state": descriptor["state"], "action": selected["key"], "serial": self._plan_serial, "signature": AI_action_identity(relative_action(selected["action"], descriptor["size"]))}}
                result["expected_effect"] = dict(selected["expected_effect"])
                result["local_policy"].update(source=evidence["action_source"], label=learned["label"] if selected["demonstration_restored"] else selected["label"])
                result["policy_evidence"].update(restored_candidate=selected["recalled"], learned_action_reused=learned["visits"] > 0, visual_regions=len(descriptor["regions"]), visual_effect_samples=learned["effect_samples"], visual_effect_value=learned["effect_sum"] / learned["effect_samples"] if learned["effect_samples"] else None)
                result["scene_graph"] = descriptor["scene_graph"][:LOCAL_AGENT_SMART_OVERLAY_LIMIT]
                result["screen_size"] = [width for width in descriptor["size"]]
                result["game_profile"] = {key: value for key, value in descriptor["profile"].items() if key not in {"anchors", "annotations"}}
                result["policy_evidence"]["recurrent_state_similarity"] = descriptor["state_match"]
                result["policy_evidence"]["game_profile_evidence"] = descriptor["profile"]["evidence"]
                result["policy_evidence"]["explicit_score_indicators"] = len(descriptor["scores"])
                result["policy_evidence"]["score_feedback_is_verified"] = bool(descriptor["scores"] and self._nodes_fresh(observation))
                result["policy_evidence"]["turn_detection"] = descriptor["turn"]
            self._check(cancel, generation)
            self.timings.append(time.monotonic() - started)
            return result
        finally:
            self._deadline = 0.0

    def _add_model_transition(self, package, state, action, next_state, terminal, reward, intrinsic, verified, seconds):
        identity = (package, state, action, next_state, int(terminal))
        values = (reward, intrinsic, int(verified), seconds)
        inserted = self._db.execute("INSERT OR IGNORE INTO agent_transitions(package,state_key,action_key,next_state,terminal,visits,reward_sum,intrinsic_sum,reward_samples,seconds_sum) VALUES(?,?,?,?,?,1,?,?,?,?)", identity + values).rowcount
        if inserted:
            self._adjust_counts(model_edges=inserted)
        else:
            self._db.execute("UPDATE agent_transitions SET visits=visits+1,reward_sum=reward_sum+?,intrinsic_sum=intrinsic_sum+?,reward_samples=reward_samples+?,seconds_sum=seconds_sum+? WHERE package=? AND state_key=? AND action_key=? AND next_state=? AND terminal=?", values + identity)

    def observe_transition(self, before, after, action, result, plan, before_png=None, after_png=None):
        if not isinstance(result, dict) or result.get("action_applied") is not True:
            return {"learned": False, "reason": "action_not_applied"}
        if not all(isinstance(item, dict) for item in (before, after, action, plan)):
            return {"learned": False, "reason": "invalid_transition"}
        package = str(before.get("package", ""))
        if not package or str(after.get("package", "")) != package:
            return {"learned": False, "reason": "package_changed"}
        applied = local_agent_number(result.get("action_applied_at"), -1)
        captured = local_agent_number(after.get("capture_started_at", after.get("timestamp")), -1)
        if applied < 0 or captured <= applied:
            return {"learned": False, "reason": "post_action_frame_unavailable"}
        with self._lock, self._transaction():
            if self._db is None or not self._started:
                return {"learned": False, "reason": "agent_stopped"}
            first, second = self._describe(before, before_png), self._describe(after, after_png)
            if first["size"] != second["size"]:
                return {"learned": False, "reason": "geometry_changed"}
            identity = str(result.get("action_id", "")) or hashlib.sha256(json.dumps((package, applied, captured, action), sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()
            if self._db.execute("SELECT 1 FROM agent_observed WHERE action_id=?", (identity,)).fetchone() is not None:
                return {"learned": False, "reason": "already_recorded"}
            first_state, second_state = self._ensure_state(first), self._ensure_state(second)
            policy = plan.get("local_policy", {})
            signature = AI_action_identity(relative_action(normalize_action(action, before), first["size"]))
            if not isinstance(policy, dict) or policy.get("signature") != signature:
                return {"learned": False, "reason": "executed_action_does_not_match_policy"}
            action_key = str(policy.get("action", ""))
            if policy.get("state") != first["state"]:
                inserted = self._db.execute("INSERT OR IGNORE INTO agent_actions(package,state_key,action_key,action,source,preconditions,label) VALUES(?,?,?,?,?,?,?)", (package, first["state"], action_key, json.dumps(relative_action(action, first["size"]), ensure_ascii=False, separators=(",", ":")), str(policy.get("source", "")), json.dumps(plan.get("preconditions", []), ensure_ascii=False, separators=(",", ":")), str(policy.get("label", "")))).rowcount
                self._adjust_counts(actions=inserted)
            learned = self._db.execute("SELECT * FROM agent_actions WHERE package=? AND state_key=? AND action_key=?", (package, first["state"], action_key)).fetchone()
            if learned is None:
                return {"learned": False, "reason": "unknown_policy_action"}
            session = self._session(package)
            if session["terminal_latched"] and (first["outcome"] == "unknown" or second["outcome"] == "unknown"):
                self._db.execute("UPDATE agent_sessions SET episode=?,steps=0,last_action='',terminal_latched=0 WHERE package=?", (uuid.uuid4().hex, package))
                self._discount_cache.pop(package, None)
                session = self._session(package)
            reward, raw_reward, verified, evidence, source = 0.0, 0.0, False, "", "unavailable"
            preceding = self._db.execute("SELECT applied_at FROM agent_observed WHERE action_id=?", (session["last_action"],)).fetchone()
            preceding_applied = preceding["applied_at"] if preceding is not None else None
            if first["outcome"] == "unknown" and second["outcome"] == "unknown" and first["activity"] == second["activity"] and self._nodes_fresh(before, preceding_applied) and local_agent_number(before.get("nodes_at")) <= applied and self._nodes_fresh(after, applied):
                changes = []
                for key in sorted(first["scores"].keys() & second["scores"].keys()):
                    old, new = first["scores"][key], second["scores"][key]
                    direction = old.get("direction", 1)
                    if new.get("direction", 1) != direction:
                        continue
                    delta = direction * (new["value"] - old["value"])
                    if delta:
                        changes.append((delta / max(1.0, abs(old["value"]), abs(new["value"])), delta, old["label"] + " → " + new["label"]))
                if changes:
                    reward = sum(item[0] for item in changes) / len(changes)
                    raw_reward = sum(item[1] for item in changes)
                    evidence = "; ".join(item[2] for item in changes)
                    verified, source = True, "fresh_accessibility_score_delta"
            changed = first["state"] != second["state"]
            before_samples = first["samples"] if before_png is not None else None
            after_samples = second["samples"] if after_png is not None else None
            visual_change = visual_difference(before_samples, after_samples)
            localized_effect = local_agent_action_focus(before_samples, after_samples, first["size"], action)
            before_perception = before.get("perception", {}) if isinstance(before.get("perception"), dict) else {}
            after_perception = after.get("perception", {}) if isinstance(after.get("perception"), dict) else {}
            visual_noise = max(LOCAL_AGENT_EFFECT_MINIMUM, local_agent_number(before_perception.get("noise_floor")), local_agent_number(after_perception.get("noise_floor")))
            animation_baseline = max(visual_noise, local_agent_number(before_perception.get("motion")), local_agent_number(before_perception.get("adaptive_drift")))
            eligible_visual = visual_change is not None and action.get("kind") in {"tap", "long_press", "swipe", "touch", "touch_begin", "touch_update", "touch_end", "keyevent", "enter", "back", "type"}
            relative_movement = min(1.0, (visual_change - animation_baseline) / max(animation_baseline, visual_change)) if eligible_visual and visual_change > animation_baseline else 0.0
            local_contrast = localized_effect["local_contrast"] if localized_effect is not None else 0.0
            visual_effect = max(relative_movement * LOCAL_AGENT_EFFECT_ATTENUATION, local_contrast) if eligible_visual else 0.0
            effect_confirmed = bool(eligible_visual and (relative_movement > LOCAL_AGENT_EFFECT_MINIMUM or local_contrast > visual_noise))
            effect_measured = bool(eligible_visual and self._frame_fresh(before) and self._frame_fresh(after))
            expected = plan.get("expected_effect", {})
            ui_effect = None
            if isinstance(expected, dict) and expected.get("kind") == "node_state" and self._nodes_fresh(before) and self._nodes_fresh(after, applied):
                reference = expected.get("node_ref", "")
                field = expected.get("field", "")
                prior_nodes = AI_matching_nodes(before.get("nodes", ()), reference)
                next_nodes = AI_matching_nodes(after.get("nodes", ()), reference)
                if field in {"checked", "selected", "focused"} and type(expected.get("value")) is bool and len(prior_nodes) == len(next_nodes) == 1:
                    before_value = prior_nodes[0].get(field) is True
                    after_value = next_nodes[0].get(field) is True
                    ui_effect = before_value != after_value and after_value == expected["value"]
                    effect_measured = True
                    if ui_effect:
                        effect_confirmed = True
                        visual_effect = max(visual_effect, AI_VISUAL_FEEDBACK_WEIGHT)
            if not effect_measured or not effect_confirmed:
                visual_effect = 0.0
            effect_status = "confirmed_effect" if effect_measured and effect_confirmed else "confirmed_no_effect" if effect_measured else "unknown"

            intrinsic = 1 / math.sqrt(second_state["visits"] + 1) if changed else 0.0
            seconds = max(0.0, local_agent_number(result.get("seconds"), captured - applied))
            frame_id = max(0, int(local_agent_number(after.get("frame_id"))))
            self._db.execute("INSERT INTO agent_observed(action_id,package,episode,ordinal,state_key,action_key,next_state,initial_next_state,terminal,reward,intrinsic,verified,applied_at,nodes_at,frame_id,seconds,evidence) VALUES(?,?,?,?,?,?,?,?,0,?,?,?,?,?,?,?,?)", (identity, package, session["episode"], session["steps"] + 1, first["state"], action_key, second["state"], second["state"], reward, intrinsic, int(verified), applied, local_agent_number(after.get("nodes_at")), frame_id, seconds, evidence))
            self._db.execute("UPDATE agent_sessions SET steps=steps+1,last_action=? WHERE package=?", (identity, package))
            self._discount_cache.pop(package, None)
            self._db.execute("UPDATE agent_states SET visits=visits+1 WHERE package=? AND state_key=?", (package, first["state"]))
            if changed:
                self._db.execute("UPDATE agent_states SET visits=visits+1 WHERE package=? AND state_key=?", (package, second["state"]))
            discount = self._discount(package)
            target = reward + discount * second_state["value"]
            intrinsic_target = intrinsic + discount * second_state["intrinsic_value"]
            visits = learned["visits"] + 1
            q = learned["q"] + (target - learned["q"]) / visits
            iq = learned["iq"] + (intrinsic_target - learned["iq"]) / visits
            error = target - learned["q"]
            self._db.execute("UPDATE agent_actions SET visits=?,reward_samples=reward_samples+?,reward_sum=reward_sum+?,intrinsic_sum=intrinsic_sum+?,q=?,iq=?,effect_samples=effect_samples+?,effect_sum=effect_sum+? WHERE package=? AND state_key=? AND action_key=?", (visits, int(verified), reward, intrinsic, q, iq, int(effect_measured), visual_effect, package, first["state"], action_key))
            self._record_sample_counts(package, transitions=1, rewards=int(verified))
            self._learn_affordance(package, first["phase"], relative_action(normalize_action(action, before), first["size"]), effect_measured=effect_measured, effect=visual_effect, reward_verified=verified, reward=reward)
            self._adjust_counts(visual_effect_samples=int(effect_measured))
            self._add_model_transition(package, first["state"], action_key, second["state"], False, reward, intrinsic, verified, seconds)
            self._stats["td_updates"] += 1
            value_change = self._refresh_value(package, first["state"])
            self._enqueue(package, first["state"], action_key, max(abs(error), abs(intrinsic_target - learned["iq"])))
            self._predecessors(package, first["state"], value_change)
            self._process_outcome(second, after)
            backups = self._replay(time.monotonic() + self._cadence(after), min(LOCAL_AGENT_PLANNING_BACKUP_LIMIT, max(1, math.isqrt(self._stats["td_updates"]))), generation=self._cancel_generation)
            self._last_descriptors[package] = second
            self._save_statistics()
            stats = self._learning_stats_locked()
            return {"learned": True, "reward": reward, "raw_reward": raw_reward, "reward_verified": verified, "verified": verified, "reward_source": source, "source": source, "evidence": evidence, "intrinsic_reward": intrinsic, "state_changed": changed, "learned_updates": stats["td_updates"], "model_error": error, "planning_backups": backups, "transitions": stats["transition_samples"], "episodes": stats["verified_episodes"], "wins": stats["wins"], "losses": stats["losses"], "action_id": identity, "visual_change": visual_change, "visual_effect": visual_effect if effect_measured else None, "local_effect": localized_effect, "visual_effect_measured": effect_measured, "effect_status": effect_status, "native_ui_effect_confirmed": ui_effect, "professional_skill_verified": False}

    def _learning_stats_locked(self):
        if self._aggregate_counts is None:
            counts = self._db.execute("SELECT COUNT(*) AS actions,COALESCE(SUM(visits),0) AS observations,COALESCE(SUM(reward_samples),0) AS reward_samples,COALESCE(SUM(effect_samples),0) AS visual_effect_samples,COALESCE(SUM(demonstrations),0) AS demonstrations FROM agent_actions").fetchone()
            states = self._db.execute("SELECT COUNT(*) FROM agent_states").fetchone()[0]
            edges = self._db.execute("SELECT COUNT(*) FROM agent_transitions").fetchone()[0]
            outcomes = {row["outcome"]: row["amount"] for row in self._db.execute("SELECT outcome,COUNT(*) AS amount FROM agent_outcomes GROUP BY outcome")}
            control_summary = self._db.execute("SELECT COUNT(*) AS cells,COALESCE(SUM(attempts),0) AS trials,COALESCE(SUM(effect_samples),0) AS effects,COALESCE(SUM(reward_samples),0) AS rewards,COALESCE(SUM(demonstrations),0) AS demos FROM agent_affordances").fetchone()
            self._aggregate_counts = {"affordance_cells": control_summary["cells"], "affordance_trials": control_summary["trials"], "affordance_effect_samples": control_summary["effects"], "affordance_reward_samples": control_summary["rewards"], "affordance_demonstrations": control_summary["demos"], "states": states, "actions": counts["actions"], "transition_samples": counts["observations"], "model_edges": edges, "verified_reward_samples": counts["reward_samples"], "visual_effect_samples": counts["visual_effect_samples"], "demonstrations": counts["demonstrations"], "verified_episodes": sum(outcomes.values()), "wins": outcomes.get("win", 0), "losses": outcomes.get("loss", 0)}
        return {**self._stats, **self._aggregate_counts, "algorithm": self.model_name, "backend": self.backend, "professional_skill_verified": False, "external_models": False, "external_network": False, "limitation": LOCAL_AGENT_LIMITATION}

    def learning_stats(self):
        with self._lock:
            return self._learning_stats_locked() if self._db is not None else {**self._stats, "available": False, "limitation": LOCAL_AGENT_LIMITATION}

    def maintain(self):
        with self._lock:
            if self._db is None or self._db.in_transaction:
                return False
            usage = shutil.disk_usage(self.root)
            summary = self._db.execute("SELECT COUNT(*) AS entries, AVG(LENGTH(evidence) + LENGTH(action_id) + LENGTH(state_key) + LENGTH(action_key) + LENGTH(next_state)) AS bytes FROM agent_observed").fetchone()
            count = int(summary["entries"])
            mean_bytes = max(1, math.ceil(local_agent_number(summary["bytes"], 1)))
            retained = min(AI_MEMORY_EVENT_RECORDS, max(1, usage.free // mean_bytes))
            eligible = max(0, count - retained)
            records = [dict(row) for row in self._db.execute("SELECT * FROM agent_observed WHERE action_id NOT IN (SELECT last_action FROM agent_sessions) ORDER BY applied_at,action_id LIMIT ?", (min(AI_MEMORY_ARCHIVE_BATCH, eligible),)).fetchall()] if eligible else []
        removed = 0
        archive_name = ""
        if records:
            folder = safe_workspace_file(self.root, self.root / "data" / "policy-archives")
            folder.mkdir(parents=True, exist_ok=True)
            archive_name = "observed-" + uuid.uuid4().hex + ".jsonl.gz"
            destination = safe_workspace_file(self.root, folder / archive_name)
            temporary = safe_workspace_file(self.root, folder / (archive_name + ".part"))
            metadata = {"table": "agent_observed", "rows": len(records), "first_action": records[0]["action_id"], "last_action": records[-1]["action_id"], "archived_at": utc_now(), "cumulative_policy_preserved": True}
            try:
                with temporary.open("xb") as stream:
                    with gzip.GzipFile(filename="", mode="wb", fileobj=stream) as compressed:
                        compressed.write((json.dumps({"archive_meta": metadata}, ensure_ascii=False) + "\n").encode("utf-8"))
                        for record in records:
                            compressed.write((json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n").encode("utf-8"))
                    stream.flush()
                    os.fsync(stream.fileno())
                os.replace(temporary, destination)
                with gzip.open(destination, "rt", encoding="utf-8") as verification:
                    header = json.loads(next(verification, ""))
                    exported_actions = [json.loads(line)["action_id"] for line in verification]
                if not isinstance(header, dict) or not isinstance(header.get("archive_meta"), dict) or header["archive_meta"].get("rows") != len(records) or exported_actions != [record["action_id"] for record in records]:
                    raise OSError("学习明细归档复核失败，原数据库保持不变")
            except BaseException:
                with contextlib.suppress(OSError):
                    destination.unlink()
                raise
            finally:
                with contextlib.suppress(OSError):
                    temporary.unlink()
            with self._lock:
                if self._db is None:
                    return False
                with self._db:
                    for record in records:
                        removed += self._db.execute("DELETE FROM agent_observed WHERE action_id=? AND action_id NOT IN (SELECT last_action FROM agent_sessions)", (record["action_id"],)).rowcount
        folder = self.root / "data" / "policy-archives"
        if folder.is_dir() and not path_is_link(folder):
            archives = sorted((file for file in folder.glob("observed-*.jsonl.gz") if file.is_file() and not path_is_link(file)), key=lambda file: file.stat().st_mtime_ns)
            total = sum(file.stat().st_size for file in archives)
            archive_budget = min(AI_MEMORY_ARCHIVE_MAX_BYTES, shutil.disk_usage(self.root).free // AI_MEMORY_ARCHIVE_FREE_SHARE)
            for file in archives:
                if total <= archive_budget:
                    break
                size = file.stat().st_size
                file.unlink()
                total -= size
                self.log("policy_observation_archive_evicted", archive=file.name, bytes=size, policy_aggregates_preserved=True)
        with self._lock:
            if self._db is None or self._db.in_transaction:
                return False
            stale_actions = self._db.execute("SELECT package,state_key,action_key FROM agent_actions WHERE visits=0 AND demonstrations=0 AND reward_samples=0 AND effect_samples=0 AND NOT EXISTS (SELECT 1 FROM agent_transitions t WHERE t.package=agent_actions.package AND t.state_key=agent_actions.state_key AND t.action_key=agent_actions.action_key) LIMIT ?", (AI_MEMORY_ARCHIVE_BATCH,)).fetchall()
            with self._db:
                unlearned_actions = sum(self._db.execute("DELETE FROM agent_actions WHERE package=? AND state_key=? AND action_key=? AND visits=0 AND demonstrations=0 AND reward_samples=0 AND effect_samples=0", (row["package"], row["state_key"], row["action_key"])).rowcount for row in stale_actions)
                orphan_states = self._db.execute("SELECT package,state_key FROM agent_states WHERE visits=0 AND NOT EXISTS (SELECT 1 FROM agent_actions a WHERE a.package=agent_states.package AND a.state_key=agent_states.state_key) AND NOT EXISTS (SELECT 1 FROM agent_transitions t WHERE t.package=agent_states.package AND (t.state_key=agent_states.state_key OR t.next_state=agent_states.state_key)) LIMIT ?", (AI_MEMORY_ARCHIVE_BATCH,)).fetchall()
                empty_states = sum(self._db.execute("DELETE FROM agent_states WHERE package=? AND state_key=? AND visits=0", (row["package"], row["state_key"])).rowcount for row in orphan_states)
            if unlearned_actions or empty_states:
                self._aggregate_counts = None
                self._package_counts.clear()
            self._db.execute("PRAGMA optimize")
            self._db.execute("PRAGMA wal_checkpoint(PASSIVE)")
        if removed or unlearned_actions or empty_states:
            self.log("policy_storage_compacted", observations_archived=removed, unlearned_actions_removed=unlearned_actions, orphan_states_removed=empty_states, learned_policy_preserved=True)
        return {"archived": removed, "retained": count - removed, "unlearned_actions_removed": unlearned_actions, "orphan_states_removed": empty_states}

    def backup(self, path, cancel=None):
        check_cancel(cancel)
        destination_path = Path(path)
        if path_is_link(destination_path):
            raise OSError("经验备份路径不能是链接")
        with self._lock:
            database_path = self._database_path
        check_cancel(cancel)
        source = sqlite3.connect(database_path.resolve().as_uri() + "?mode=ro", uri=True, timeout=0)
        destination = None
        try:
            destination = sqlite3.connect(str(destination_path), timeout=0)
            source.backup(destination, pages=AI_MEMORY_BACKUP_PAGES, sleep=AI_MEMORY_BACKUP_YIELD_SECONDS, progress=lambda *values: check_cancel(cancel))
        finally:
            if destination is not None:
                destination.close()
            source.close()


def normalize_action(action, observation):
    if not isinstance(action, dict) or not isinstance(observation, dict):
        raise ValueError("动作和观察必须是 JSON 对象")
    size = observation.get("size", (observation.get("width"), observation.get("height")))
    if not isinstance(size, (list, tuple)) or len(size) != AI_SPATIAL_DIMENSIONS or any(type(value) is not int or value <= 0 for value in size):
        raise ValueError("必须使用当前画面的真实尺寸")
    width, height = size
    capabilities = observation.get("capabilities", {})
    capabilities = capabilities if isinstance(capabilities, dict) else {}
    pointer_limit = capabilities.get("touch_slots", capabilities.get("max_pointers", 1))
    if type(pointer_limit) is not int or pointer_limit < 1:
        raise ValueError("设备触控能力无效")
    aliases = {"click": "tap", "hold": "long_press", "drag": "swipe", "text": "type", "key": "keyevent", "multi_touch": "touch", "touch_release": "touch_end"}
    kind = aliases.get(str(action.get("kind", "")).strip().lower(), str(action.get("kind", "")).strip().lower())
    supported = capabilities.get("actions", AI_ACTION_KINDS)
    if kind not in AI_ACTION_KINDS or kind not in supported:
        raise ValueError("当前设备不支持该动作：" + kind)
    source = dict(action)
    target_position = source.get("target_position")
    if target_position is not None:
        if kind not in {"tap", "long_press"} or not isinstance(target_position, (tuple, list)) or len(target_position) != AI_SPATIAL_DIMENSIONS or any(type(item) is not int or not 0 <= item <= AI_COORDINATE_SCALE for item in target_position):
            raise ValueError("示教控件内部坐标无效")
        target_position = list(target_position)
    if "target" in source:
        if kind not in {"tap", "long_press"} or not isinstance(source["target"], str):
            raise ValueError("语义目标只支持点击或长按")
        matches = AI_matching_nodes(observation.get("nodes", []), source["target"])
        if len(matches) != 1:
            raise ValueError("语义目标不在当前画面内或不唯一")
        target = matches[0]
        bounds = target.get("bounds")
        if target.get("enabled", True) is not True or target.get("clickable") is not True or not isinstance(bounds, (list, tuple)) or len(bounds) != AI_BOUNDING_BOX_COMPONENTS:
            raise ValueError("语义目标当前不可交互")
        if any(type(value) is not int for value in bounds):
            raise ValueError("语义目标边界无效")
        left, top, right, bottom = bounds
        if not 0 <= left < right <= width or not 0 <= top < bottom <= height:
            raise ValueError("语义目标超出当前画面")
        if target_position is None:
            source["x"], source["y"] = (left + right - 1) // 2, (top + bottom - 1) // 2
        else:
            source["x"] = left + round((right - left - 1) * target_position[0] / AI_COORDINATE_SCALE)
            source["y"] = top + round((bottom - top - 1) * target_position[1] / AI_COORDINATE_SCALE)
    result = {"kind": kind}
    if target_position is not None:
        result["target_position"] = target_position
    def integer(value, name):
        if type(value) is int:
            return value
        if type(value) is not float or not math.isfinite(value):
            raise ValueError(name + "必须为有限数字")
        return int(round(value))
    def coordinate(item, axis, maximum, default=None):
        value = item.get(axis, default)
        if value is None:
            raise ValueError("缺少坐标 " + axis)
        value = integer(value, axis)
        if not 0 <= value < maximum:
            raise ValueError("坐标超出当前安卓画面：" + axis)
        return value
    if kind in {"tap", "long_press", "swipe"}:
        result["x"], result["y"] = coordinate(source, "x", width), coordinate(source, "y", height)
    if kind == "swipe":
        result["x2"], result["y2"] = coordinate(source, "x2", width), coordinate(source, "y2", height)
    if kind in {"tap", "long_press", "swipe"}:
        count = integer(source.get("repeat", 1), "动作重复次数")
        spacing = integer(source.get("interval_ms", 0), "动作间隔")
        if count < 1 or spacing < 0:
            raise ValueError("重复次数必须为正数，间隔必须非负")
        result.update(repeat=count, interval_ms=spacing)
    if kind in {"touch", "touch_begin", "touch_update"}:
        pointers = source.get("pointers")
        if not isinstance(pointers, list) or not 1 <= len(pointers) <= pointer_limit:
            raise ValueError("触点数量必须在设备能力范围内")
        identifiers = set()
        result["pointers"] = []
        for point in pointers:
            if not isinstance(point, dict):
                raise ValueError("触点格式无效")
            identifier = integer(point.get("id", len(identifiers)), "触点编号")
            if identifier in identifiers or not 0 <= identifier < pointer_limit:
                raise ValueError("触点编号重复或超出设备范围")
            identifiers.add(identifier)
            x, y = coordinate(point, "x", width), coordinate(point, "y", height)
            result["pointers"].append({"id": identifier, "x": x, "y": y, "x2": coordinate(point, "x2", width, x), "y2": coordinate(point, "y2", height, y)})
    if kind == "touch_end":
        ids = source.get("ids", [])
        if not isinstance(ids, list) or len(ids) > pointer_limit:
            raise ValueError("释放触点编号格式无效")
        result["ids"] = [integer(value, "触点编号") for value in ids]
        if any(not 0 <= value < pointer_limit for value in result["ids"]) or len(set(result["ids"])) != len(result["ids"]):
            raise ValueError("释放触点编号重复或无效")
    if kind in {"tap", "long_press", "swipe", "touch", "touch_begin", "touch_update", "wait"}:
        timing = observation.get("input_timing", {})
        timing = timing if isinstance(timing, dict) else {}
        defaults = {"tap": AI_ANDROID_TAP_INITIAL_MS, "long_press": AI_ANDROID_LONG_PRESS_INITIAL_MS, "swipe": AI_ANDROID_SWIPE_INITIAL_MS, "touch": AI_ANDROID_SWIPE_INITIAL_MS, "wait": AI_ANDROID_WAIT_INITIAL_MS}
        refresh_hz = capabilities.get("refresh_hz", 0)
        latency = capabilities.get("input_latency_seconds", 0)
        refresh_hz = refresh_hz if type(refresh_hz) in (int, float) and math.isfinite(refresh_hz) and refresh_hz > 0 else 0
        latency = latency if type(latency) in (int, float) and math.isfinite(latency) and latency > 0 else 0
        if refresh_hz:
            defaults["tap"] = math.ceil(max(1 / refresh_hz, latency) * AI_MILLISECONDS_PER_SECOND)
        if type(capabilities.get("long_press_ms")) is int and capabilities["long_press_ms"] > 0:
            defaults["long_press"] = capabilities["long_press_ms"]
        default = timing.get(kind + "_ms", defaults.get(kind, 0))
        duration = integer(source.get("ms", default), "持续时间")
        try:
            representable = duration >= 0 and math.isfinite(duration / AI_MILLISECONDS_PER_SECOND)
        except OverflowError:
            representable = False
        if not representable:
            raise ValueError("动作时长必须非负且可由主机计时器表示")
        result["ms"] = duration
    if kind == "type":
        value = source.get("text")
        if not isinstance(value, str) or not value:
            raise ValueError("输入文字不能为空")
        result["text"] = value
        if "x" in source or "y" in source:
            result["x"], result["y"] = coordinate(source, "x", width), coordinate(source, "y", height)
        if source.get("clear"):
            result["clear"] = True
    if kind == "keyevent":
        key = str(source.get("key", source.get("text", ""))).strip().upper()
        if not re.fullmatch(r"(?:KEYCODE_[A-Z0-9_]+|[0-9]+)", key):
            raise ValueError("安卓按键代码无效")
        result["text"] = key
    return result


def rebind_semantic_action(action, conditions, observation):
    if action.get("kind") not in {"tap", "long_press"} or not isinstance(conditions, list):
        return action, False
    targets = [condition.get("value") for condition in conditions if isinstance(condition, dict) and condition.get("kind") == "node_enabled"]
    if len(targets) != 1 or not GameAI._preconditions_hold(conditions, observation):
        return action, False
    updated = normalize_action({**action, "target": targets[0]}, observation)
    return updated, True


def expand_game_actions(actions, phase, confidence, limit=None):
    if type(confidence) not in (int, float) or not math.isfinite(confidence):
        raise ValueError("动作置信信息无效")
    budget = max(1, len(actions) + math.ceil(len(actions) * max(0.0, min(1.0, confidence)))) if limit is None else max(1, int(limit))
    expanded = []
    for action in actions:
        kind = action.get("kind", "")
        count = int(action.get("repeat", 1)) if phase == "playing" and kind in {"tap", "swipe"} else 1
        for index in range(max(1, count)):
            if len(expanded) >= budget:
                return expanded
            if index and action.get("interval_ms", 0):
                if len(expanded) + 1 >= budget:
                    return expanded
                expanded.append({"kind": "wait", "ms": action["interval_ms"]})
            expanded.append({key: value for key, value in action.items() if key not in {"repeat", "interval_ms"}})
    return expanded


def summarize_recalled_experience(recalled):
    usable = []
    for index, item in enumerate(recalled):
        if not isinstance(item, dict) or not item.get("observations"):
            continue
        usable.append({"candidate": index, "guidance": item.get("guidance", "uncertain"), "state_match": item.get("state_similarity", 0), "terminal_samples": item.get("outcome_trials", 0), "terminal_return": item.get("outcome_return", 0), "effect_samples": item.get("effect_trials", 0), "effect_success": item.get("effect_success_rate"), "uncertainty": item.get("uncertainty", 1)})
    return json.dumps(usable, ensure_ascii=False, separators=(",", ":")) if usable else ""


def stored_action(action):
    result = dict(action)
    if result.get("kind") == "type":
        result["text_length"] = len(str(result.pop("text", "")))
        result["text_redacted"] = True
    return result


def frame_dimensions(png):
    if not isinstance(png, bytes) or len(png) < AI_PNG_MIN_IMAGE_BYTES or not png.startswith(AI_PNG_SIGNATURE):
        raise ValueError("没有取得有效的安卓截图")
    if png[len(AI_PNG_SIGNATURE):AI_PNG_DIMENSION_OFFSET] != b"\x00\x00\x00\x0dIHDR":
        raise ValueError("安卓截图缺少合法的PNG图像头")
    checksum = struct.unpack(">I", png[AI_PNG_PROPERTIES_END:AI_PNG_HEADER_BYTES])[0]
    if zlib.crc32(png[len(AI_PNG_SIGNATURE) + AI_PNG_UINT_BYTES:AI_PNG_PROPERTIES_END]) != checksum:
        raise ValueError("安卓截图图像头校验失败")
    if not png.endswith(AI_PNG_END):
        raise ValueError("安卓截图传输不完整")
    width, height = struct.unpack(">II", png[AI_PNG_DIMENSION_OFFSET:AI_PNG_DIMENSION_END])
    if not 0 < width <= AI_PNG_MAX_DIMENSION or not 0 < height <= AI_PNG_MAX_DIMENSION:
        raise ValueError("安卓截图尺寸异常")
    return width, height


_WINDOWS_IMAGE_LOCK = threading.RLock()


_WINDOWS_GDIP_STATE = None


def _windows_gdip_shutdown():
    global _WINDOWS_GDIP_STATE
    with _WINDOWS_IMAGE_LOCK:
        state, _WINDOWS_GDIP_STATE = _WINDOWS_GDIP_STATE, None
        if state is not None:
            with contextlib.suppress(Exception):
                state[0].GdiplusShutdown(state[1])


def _windows_gdip_initialize():
    global _WINDOWS_GDIP_STATE
    if _WINDOWS_GDIP_STATE is not None:
        return _WINDOWS_GDIP_STATE[0]
    gdiplus = ctypes.WinDLL("gdiplus", use_last_error=True)
    shlwapi = ctypes.WinDLL("shlwapi", use_last_error=True)
    class StartupInput(ctypes.Structure):
        _fields_ = [("version", ctypes.c_uint32), ("callback", ctypes.c_void_p), ("suppress_background", ctypes.c_int), ("suppress_codecs", ctypes.c_int)]
    gdiplus.GdiplusStartup.argtypes = [ctypes.POINTER(ctypes.c_size_t), ctypes.POINTER(StartupInput), ctypes.c_void_p]
    gdiplus.GdiplusStartup.restype = ctypes.c_int
    gdiplus.GdiplusShutdown.argtypes = [ctypes.c_size_t]
    gdiplus.GdiplusShutdown.restype = None
    gdiplus.GdipCreateBitmapFromStream.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p)]
    gdiplus.GdipCreateBitmapFromStream.restype = ctypes.c_int
    gdiplus.GdipGetImageWidth.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32)]
    gdiplus.GdipGetImageWidth.restype = ctypes.c_int
    gdiplus.GdipGetImageHeight.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32)]
    gdiplus.GdipGetImageHeight.restype = ctypes.c_int
    gdiplus.GdipBitmapLockBits.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_int32, ctypes.c_void_p]
    gdiplus.GdipBitmapLockBits.restype = ctypes.c_int
    gdiplus.GdipBitmapUnlockBits.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
    gdiplus.GdipBitmapUnlockBits.restype = ctypes.c_int
    gdiplus.GdipDisposeImage.argtypes = [ctypes.c_void_p]
    gdiplus.GdipDisposeImage.restype = ctypes.c_int
    shlwapi.SHCreateMemStream.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    shlwapi.SHCreateMemStream.restype = ctypes.c_void_p
    token = ctypes.c_size_t()
    if gdiplus.GdiplusStartup(ctypes.byref(token), ctypes.byref(StartupInput(1, None, 0, 0)), None):
        return None
    _WINDOWS_GDIP_STATE = (gdiplus, token, shlwapi)
    import atexit
    atexit.register(_windows_gdip_shutdown)
    return gdiplus


def _windows_visual_samples(png, width, height, columns, rows):
    if os.name != "nt" or width * height * AI_RGBA_CHANNELS > AI_PERCEPTION_MAX_DECODE_BYTES:
        return None
    with _WINDOWS_IMAGE_LOCK:
        try:
            gdiplus = _windows_gdip_initialize()
            if gdiplus is None:
                return None
            shlwapi = _WINDOWS_GDIP_STATE[2]
            class Rect(ctypes.Structure):
                _fields_ = [("x", ctypes.c_int32), ("y", ctypes.c_int32), ("width", ctypes.c_int32), ("height", ctypes.c_int32)]
            class BitmapData(ctypes.Structure):
                _fields_ = [("width", ctypes.c_uint32), ("height", ctypes.c_uint32), ("stride", ctypes.c_int32), ("format", ctypes.c_int32), ("scan0", ctypes.c_void_p), ("reserved", ctypes.c_size_t)]
            contents = ctypes.create_string_buffer(png)
            stream = shlwapi.SHCreateMemStream(ctypes.cast(contents, ctypes.c_void_p), len(png))
            if not stream:
                return None
            try:
                bitmap = ctypes.c_void_p()
                if gdiplus.GdipCreateBitmapFromStream(stream, ctypes.byref(bitmap)) or not bitmap.value:
                    return None
                try:
                    bitmap_width, bitmap_height = ctypes.c_uint32(), ctypes.c_uint32()
                    if gdiplus.GdipGetImageWidth(bitmap, ctypes.byref(bitmap_width)) or gdiplus.GdipGetImageHeight(bitmap, ctypes.byref(bitmap_height)):
                        return None
                    if (bitmap_width.value, bitmap_height.value) != (width, height):
                        return None
                    data = BitmapData()
                    bounds = Rect(0, 0, width, height)
                    if gdiplus.GdipBitmapLockBits(bitmap, ctypes.byref(bounds), AI_GDIP_IMAGE_LOCK_READ, AI_GDIP_PIXEL_FORMAT_ARGB, ctypes.byref(data)) or not data.scan0:
                        return None
                    try:
                        stride = int(data.stride)
                        if abs(stride) < width * AI_RGBA_CHANNELS:
                            return None
                        base = int(data.scan0) + min(0, stride * (height - 1))
                        xs = [min(width - 1, (gx * AI_SPATIAL_DIMENSIONS + 1) * width // (AI_SPATIAL_DIMENSIONS * columns)) for gx in range(columns)]
                        output = []
                        for gy in range(rows):
                            y = min(height - 1, (gy * AI_SPATIAL_DIMENSIONS + 1) * height // (AI_SPATIAL_DIMENSIONS * rows))
                            row_offset = (y if stride > 0 else height - 1 - y) * abs(stride)
                            pixels = ctypes.string_at(base + row_offset, width * AI_RGBA_CHANNELS)
                            for x in xs:
                                offset = x * AI_RGBA_CHANNELS
                                blue, green, red, alpha = pixels[offset:offset + AI_RGBA_CHANNELS]
                                output.append((red * alpha // AI_BYTE_MAX, green * alpha // AI_BYTE_MAX, blue * alpha // AI_BYTE_MAX))
                        return tuple(output)
                    finally:
                        gdiplus.GdipBitmapUnlockBits(bitmap, ctypes.byref(data))
                finally:
                    gdiplus.GdipDisposeImage(bitmap)
            finally:
                interface = ctypes.cast(stream, ctypes.POINTER(ctypes.POINTER(ctypes.c_void_p)))
                release = ctypes.WINFUNCTYPE(ctypes.c_ulong, ctypes.c_void_p)(interface.contents[AI_COM_RELEASE_VTABLE_INDEX])
                release(stream)
        except Exception:
            return None


def vision_sample_grid(width, height):
    columns = min(width, max(1, math.ceil(math.sqrt(width)) * AI_VISION_GRID_MULTIPLIER))
    rows = min(height, max(1, math.ceil(math.sqrt(height)) * AI_VISION_GRID_MULTIPLIER))
    if columns * rows > AI_PERCEPTION_MAX_SAMPLES:
        scale = math.sqrt(AI_PERCEPTION_MAX_SAMPLES / (columns * rows))
        columns = max(1, math.floor(columns * scale))
        rows = max(1, math.floor(rows * scale))
    return columns, rows


def local_agent_visual_regions(samples, size, previous=(), noise=0.0):
    if not samples or not isinstance(size, (tuple, list)) or len(size) != AI_SPATIAL_DIMENSIONS:
        return []
    width, height = size
    columns, rows = vision_sample_grid(width, height)
    if len(samples) != columns * rows:
        return []
    temporal = len(previous) == len(samples)
    gradient, motion, saturation = [], [], []
    for index, color in enumerate(samples):
        y, x = divmod(index, columns)
        neighbors = (samples[(y + dy) * columns + x + dx] for dx, dy in LOCAL_AGENT_DIRECTIONS if 0 <= x + dx < columns and 0 <= y + dy < rows)
        edges = [sum(abs(a - b) for a, b in zip(color, nearby)) / (AI_RGB_CHANNELS * AI_BYTE_MAX) for nearby in neighbors]
        gradient.append(sum(edges) / len(edges) if edges else 0.0)
        motion.append(sum(abs(a - b) for a, b in zip(color, previous[index])) / (AI_RGB_CHANNELS * AI_BYTE_MAX) if temporal else 0.0)
        saturation.append((max(color) - min(color)) / AI_BYTE_MAX)
    middle = statistics.median(gradient)
    deviation = statistics.median(abs(value - middle) for value in gradient)
    edge_threshold = max(1 / AI_BYTE_MAX, middle + max(deviation, middle / AI_SPATIAL_DIMENSIONS))
    motion_threshold = max(1 / AI_BYTE_MAX, local_agent_number(noise) * AI_RGB_CHANNELS)
    areas = set(index for index in range(len(samples)) if gradient[index] > edge_threshold or temporal and motion[index] > motion_threshold)
    regions = []
    while areas:
        index = areas.pop()
        pending = [index]
        points = [index]
        while pending:
            current = pending.pop()
            y, x = divmod(current, columns)
            for dx, dy in AI_VISION_NEIGHBORS:
                nx, ny = x + dx, y + dy
                if 0 <= nx < columns and 0 <= ny < rows:
                    neighbor = ny * columns + nx
                    if neighbor in areas:
                        areas.remove(neighbor)
                        pending.append(neighbor)
                        points.append(neighbor)
        if not AI_VISION_MIN_REGION_CELLS <= len(points) <= len(samples) * AI_VISION_REGION_AREA_LIMIT:
            continue
        xs = [point % columns for point in points]
        ys = [point // columns for point in points]
        left, top, right, bottom = min(xs), min(ys), max(xs) + 1, max(ys) + 1
        weights = [gradient[point] + motion[point] + saturation[point] / AI_RGB_CHANNELS for point in points]
        strength = sum(weights) / len(weights)
        x = round(sum((point % columns + 0.5) * weight for point, weight in zip(points, weights)) / max(sys.float_info.epsilon, sum(weights)) * width / columns)
        y = round(sum((point // columns + 0.5) * weight for point, weight in zip(points, weights)) / max(sys.float_info.epsilon, sum(weights)) * height / rows)
        rect = [left * width // columns, top * height // rows, min(width, math.ceil(right * width / columns)), min(height, math.ceil(bottom * height / rows))]
        movement = sum(motion[point] for point in points) / len(points)
        width_span, height_span = max(1, right - left), max(1, bottom - top)
        compact = max(width_span, height_span) <= AI_SPATIAL_DIMENSIONS * min(width_span, height_span)
        control_zone = temporal and movement <= motion_threshold and compact and y >= height * AI_SPATIAL_DIMENSIONS / AI_RGB_CHANNELS
        role = "motion_target" if temporal and movement > motion_threshold else "movement_control" if control_zone and x < width / AI_SPATIAL_DIMENSIONS else "action_control" if control_zone else "visual_target"
        average_rgb = tuple(round(sum(samples[point][channel] for point in points) / len(points) * (AI_VISION_STATE_LEVELS - 1) / AI_BYTE_MAX) for channel in range(AI_RGB_CHANNELS))
        regions.append({"kind": role, "source": "local_visual", "bounds": rect, "x": max(0, min(width - 1, x)), "y": max(0, min(height - 1, y)), "strength": round(strength, AI_RGB_CHANNELS), "motion": round(movement, AI_RGB_CHANNELS), "area": len(points), "appearance": average_rgb})
    regions.sort(key=lambda item: (item["motion"], item["strength"] * math.sqrt(item["area"])), reverse=True)
    selected = []
    for region in regions:
        x, y = region["x"], region["y"]
        if any(left <= x < right and top <= y < bottom for other in selected for left, top, right, bottom in (other["bounds"],)):
            continue
        selected.append(region)
        if len(selected) >= AI_VISION_MAX_REGIONS:
            break
    return selected


def png_image_payload(png):
    pieces = []
    palette = []
    transparency = b""
    position = len(AI_PNG_SIGNATURE)
    try:
        while position + AI_PNG_CHUNK_FRAMING_BYTES <= len(png):
            size = struct.unpack_from(">I", png, position)[0]
            kind = png[position + AI_PNG_UINT_BYTES:position + AI_PNG_CHUNK_HEADER_BYTES]
            if size > len(png) - position - AI_PNG_CHUNK_FRAMING_BYTES:
                return None
            content = png[position + AI_PNG_CHUNK_HEADER_BYTES:position + AI_PNG_CHUNK_HEADER_BYTES + size]
            checksum = struct.unpack_from(">I", png, position + AI_PNG_CHUNK_HEADER_BYTES + size)[0]
            if zlib.crc32(png[position + AI_PNG_UINT_BYTES:position + AI_PNG_CHUNK_HEADER_BYTES + size]) != checksum:
                return None
            if kind == b"IHDR":
                if position != len(AI_PNG_SIGNATURE):
                    return None
            elif kind == b"IDAT":
                pieces.append(content)
            elif kind == b"PLTE":
                if pieces or size % AI_RGB_CHANNELS or size > AI_PNG_PALETTE_MAX_BYTES:
                    return None
                palette = [tuple(content[index:index + AI_RGB_CHANNELS]) for index in range(0, size, AI_RGB_CHANNELS)]
            elif kind == b"tRNS":
                transparency = content
            position += size + AI_PNG_CHUNK_FRAMING_BYTES
            if kind == b"IEND":
                if size or position != len(png) or not pieces:
                    return None
                return pieces, palette, transparency
    except (ValueError, IndexError, struct.error, OverflowError, MemoryError):
        return None
    return None


@functools.lru_cache(maxsize=AI_PERCEPTION_CACHE_FRAMES)
def visual_samples(png, columns=None, rows=None):
    width, height = frame_dimensions(png)
    default_columns, default_rows = vision_sample_grid(width, height)
    columns = default_columns if columns is None else int(columns)
    rows = default_rows if rows is None else int(rows)
    if columns < 1 or rows < 1 or columns * rows > AI_PERCEPTION_MAX_SAMPLES:
        return None
    payload = png_image_payload(png)
    if payload is None:
        return None
    accelerated = _windows_visual_samples(png, width, height, columns, rows)
    if accelerated is not None:
        return accelerated
    bit_depth, color, compression, filtering, interlace = png[AI_PNG_DIMENSION_END:AI_PNG_PROPERTIES_END]
    channels = {AI_PNG_GRAYSCALE: 1, AI_PNG_TRUECOLOR: AI_RGB_CHANNELS, AI_PNG_INDEXED: 1, AI_PNG_GRAYSCALE_ALPHA: AI_PNG_GRAY_ALPHA_CHANNELS, AI_PNG_TRUECOLOR_ALPHA: AI_RGBA_CHANNELS}.get(color)
    if bit_depth != AI_PNG_BITS_PER_CHANNEL or channels is None or compression != 0 or filtering != 0 or interlace != 0:
        return None
    row_bytes = width * channels
    expected_size = height * (row_bytes + 1)
    if expected_size > AI_PERCEPTION_MAX_DECODE_BYTES:
        return None
    pieces, palette, transparency = payload
    if color == AI_PNG_INDEXED and not palette:
        return None
    try:
        decompressor = zlib.decompressobj()
        raw = decompressor.decompress(b"".join(pieces), expected_size + 1)
        if len(raw) != expected_size or not decompressor.eof or decompressor.unconsumed_tail or decompressor.unused_data:
            return None
        xs = [min(width - 1, (index * 2 + 1) * width // (2 * columns)) for index in range(columns)]
        target_rows = {}
        for index in range(rows):
            y = min(height - 1, (index * 2 + 1) * height // (2 * rows))
            target_rows.setdefault(y, []).append(index)
        samples = [None] * (columns * rows)
        previous = bytearray(row_bytes)
        position = 0
        for y in range(height):
            filter_type = raw[position]
            current = bytearray(raw[position + 1:position + row_bytes + 1])
            position += row_bytes + 1
            if filter_type == AI_PNG_FILTER_SUB:
                for index in range(channels, row_bytes):
                    current[index] = (current[index] + current[index - channels]) & AI_BYTE_MAX
            elif filter_type == AI_PNG_FILTER_UP:
                for index in range(row_bytes):
                    current[index] = (current[index] + previous[index]) & AI_BYTE_MAX
            elif filter_type == AI_PNG_FILTER_AVERAGE:
                for index in range(row_bytes):
                    left = current[index - channels] if index >= channels else 0
                    current[index] = (current[index] + ((left + previous[index]) >> 1)) & AI_BYTE_MAX
            elif filter_type == AI_PNG_FILTER_PAETH:
                for index in range(row_bytes):
                    left = current[index - channels] if index >= channels else 0
                    above = previous[index]
                    upper_left = previous[index - channels] if index >= channels else 0
                    prediction = left + above - upper_left
                    da, db, dc = abs(prediction - left), abs(prediction - above), abs(prediction - upper_left)
                    predictor = left if da <= db and da <= dc else above if db <= dc else upper_left
                    current[index] = (current[index] + predictor) & AI_BYTE_MAX
            elif filter_type != 0:
                return None
            for gy in target_rows.get(y, ()):
                for gx, x in enumerate(xs):
                    offset = x * channels
                    if color == AI_PNG_GRAYSCALE:
                        rgb = (current[offset],) * AI_RGB_CHANNELS
                    elif color == AI_PNG_TRUECOLOR:
                        rgb = tuple(current[offset:offset + AI_RGB_CHANNELS])
                    elif color == AI_PNG_INDEXED:
                        palette_index = current[offset]
                        if palette_index >= len(palette):
                            return None
                        rgb = palette[palette_index]
                        if palette_index < len(transparency):
                            alpha = transparency[palette_index]
                            rgb = tuple(value * alpha // AI_BYTE_MAX for value in rgb)
                    elif color == AI_PNG_GRAYSCALE_ALPHA:
                        alpha = current[offset + 1]
                        rgb = (current[offset] * alpha // AI_BYTE_MAX,) * AI_RGB_CHANNELS
                    else:
                        alpha = current[offset + AI_RGB_CHANNELS]
                        rgb = tuple(value * alpha // AI_BYTE_MAX for value in current[offset:offset + AI_RGB_CHANNELS])
                    samples[gy * columns + gx] = rgb
            previous = current
        return tuple(samples)
    except (ValueError, IndexError, struct.error, zlib.error, OverflowError, MemoryError):
        return None


def visual_difference(first, second):
    if first is None or second is None or len(first) != len(second) or not first:
        return None
    total = sum((sum(abs(x - y) for x, y in zip(a, b)) / (max(1, len(a)) * AI_BYTE_MAX)) ** 2 for a, b in zip(first, second))
    return math.sqrt(total / len(first))

def decision_is_stale(age, drift, original_png, current_png, phase="unknown", perception=None, actions=None):
    if original_png == current_png:
        return False
    if actions and all(isinstance(action, dict) and action.get("kind") in {"wait", "touch_end", "touch_release_all"} for action in actions):
        return False
    if type(age) not in (int, float) or not math.isfinite(age) or age < 0:
        return True
    perception = perception if isinstance(perception, dict) else {}
    frame_interval = perception.get("frame_interval", 0)
    noise = perception.get("noise_floor", 1 / AI_BYTE_MAX)
    drift_limit = perception.get("adaptive_drift", noise)
    rate = perception.get("motion_rate", 0)
    values = (frame_interval, noise, drift_limit, rate)
    if any(type(value) not in (int, float) or not math.isfinite(value) or value < 0 for value in values):
        return True
    if drift is None:
        return age > max(frame_interval, time.get_clock_info("monotonic").resolution)
    if type(drift) not in (int, float) or not math.isfinite(drift):
        return True
    if drift <= noise:
        return False
    if frame_interval > 0 and age <= frame_interval:
        return False
    if actions:
        width, height = frame_dimensions(current_png)
        first = visual_samples(original_png)
        second = visual_samples(current_png)
        if first is not None and second is not None and len(first) == len(second):
            columns, rows = vision_sample_grid(width, height)
            if len(first) == columns * rows:
                points = []
                for action in actions:
                    if "x" in action and "y" in action:
                        points.append((action["x"], action["y"]))
                    points.extend((point["x"], point["y"]) for point in action.get("pointers", []) if "x" in point and "y" in point)
                local_changes = []
                for x, y in points:
                    column = min(columns - 1, max(0, int(x * columns / width)))
                    row = min(rows - 1, max(0, int(y * rows / height)))
                    neighborhood = [neighbor_y * columns + neighbor_x for neighbor_y in range(max(0, row - AI_SAMPLING_NEIGHBOR_RADIUS), min(rows, row + AI_SAMPLING_NEIGHBOR_RADIUS + 1)) for neighbor_x in range(max(0, column - AI_SAMPLING_NEIGHBOR_RADIUS), min(columns, column + AI_SAMPLING_NEIGHBOR_RADIUS + 1))]
                    local = visual_difference(tuple(first[neighbor] for neighbor in neighborhood), tuple(second[neighbor] for neighbor in neighborhood))
                    if local is not None:
                        local_changes.append(local)
                        if local > max(noise, drift_limit):
                            return True
                if points and len(local_changes) == len(points) and max(local_changes) <= noise:
                    return False
    expected = rate * min(age, frame_interval) if frame_interval else 0
    tolerance = max(noise, drift_limit, expected)
    if phase == "playing" and frame_interval > 0:
        tolerance /= math.sqrt(max(1.0, age / frame_interval))
    return drift > tolerance


class RealtimePerception:
    def __init__(self):
        self.lock = threading.Lock()
        self.generation = 0
        self.previous = None
        self.last_captured = 0.0
        self.motion = None
        self.max_motion = 0.0
        self.observations = 0
        self._interval = AI_OnlineEstimate()
        self._processing = AI_OnlineEstimate()
        self._changes = AI_OnlineEstimate()
        self._rates = AI_OnlineEstimate()
        self._noise_floor = 1 / AI_BYTE_MAX

    def update(self, png, captured, interval=None):
        with self.lock:
            measured = self._processing.upper(0)
            cadence = max(0.0, float(interval)) if interval is not None else measured
            if captured <= self.last_captured or captured - self.last_captured < cadence:
                return
            generation = self.generation
        started = time.monotonic()
        sample = visual_samples(png)
        elapsed = time.monotonic() - started
        if sample is None:
            return
        with self.lock:
            if generation != self.generation or captured <= self.last_captured:
                return
            previous_captured = self.last_captured
            self.last_captured = captured
            self._processing.update(elapsed)
            change = visual_difference(self.previous, sample) if self.previous is not None else None
            if previous_captured and self.previous is not None and len(self.previous) == len(sample):
                period = captured - previous_captured
                self._interval.update(period)
                if change is not None:
                    self._changes.update(change)
                    self._rates.update(change / max(period, time.get_clock_info("monotonic").resolution))
                    count = max(1, math.isqrt(len(sample)))
                    stationary = heapq.nsmallest(count, (sum(abs(x - y) for x, y in zip(left, right)) / (AI_RGB_CHANNELS * AI_BYTE_MAX) for left, right in zip(self.previous, sample)))
                    self._noise_floor = max(1 / AI_BYTE_MAX, sum(stationary) / len(stationary))
            self.previous = sample
            self.motion = change
            self.max_motion = max(self.max_motion, change or 0.0)
            self.observations += 1

    def state(self):
        with self.lock:
            return {"motion": self.motion, "recent_peak": self._changes.upper(self.max_motion), "observations": self.observations, "frame_interval": self._interval.mean, "sample_seconds": self._processing.upper(0), "motion_rate": self._rates.mean, "noise_floor": self._noise_floor, "adaptive_drift": max(self._noise_floor, self._changes.upper(self._noise_floor))}

    def clear(self):
        with self.lock:
            self.generation += 1
            self.previous = None
            self.last_captured = 0.0
            self.motion = None
            self.max_motion = 0.0
            self.observations = 0
            self._interval = AI_OnlineEstimate()
            self._processing = AI_OnlineEstimate()
            self._changes = AI_OnlineEstimate()
            self._rates = AI_OnlineEstimate()
            self._noise_floor = 1 / AI_BYTE_MAX


def scene_features(plan, observation):
    task = plan.get("task_state", observation.get("task_state", {}))
    task = task if isinstance(task, dict) else {}
    game = str(observation.get("package", "")).strip() or re.sub(r"\s+", " ", str(plan.get("game", ""))).strip() or "unknown"
    phase = str(plan.get("phase", observation.get("previous_phase", "unknown")))
    anchors = sorted({str(node.get("id", node.get("resource_id", ""))).strip() or str(node.get("text", "")).strip() for node in observation.get("nodes", []) if isinstance(node, dict) and (node.get("id") or node.get("resource_id") or node.get("text"))})
    if not anchors:
        anchors = [str(task.get("state_key", ""))]
    objective = str(task.get("goal", ""))[:AI_STATE_FIELD_LIMIT]
    mode = str(task.get("control_mode", "unknown"))
    turn = str(task.get("turn", "unknown"))
    signature = {"objective": objective, "mode": mode, "turn": turn, "anchors": anchors}
    state_key = str(task.get("state_key", "")).strip() or hashlib.sha256(json.dumps(signature, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()[:AI_HASH_PREFIX_BYTES * AI_HEXADECIMAL_DIGITS_PER_BYTE]
    return {"game": game[:AI_LABEL_FIELD_LIMIT], "phase": phase, "situation": state_key[:AI_STATE_FIELD_LIMIT], "objective": objective, "mode": mode, "turn": turn, "anchors": anchors, "screen": list(observation.get("size", []))}


def relative_action(action, size):
    if not isinstance(size, (list, tuple)) or len(size) != AI_SPATIAL_DIMENSIONS or any(type(value) is not int or value <= 0 for value in size):
        raise ValueError("动作经验缺少有效的原始画面尺寸")
    safe = stored_action(action)
    width, height = size
    for key in ("x", "x2", "y", "y2"):
        if key in safe:
            extent = width if key.startswith("x") else height
            if type(safe[key]) not in (int, float) or not math.isfinite(safe[key]) or not 0 <= safe[key] < extent:
                raise ValueError("动作经验中的坐标无效")
            safe[key] = round(AI_COORDINATE_SCALE * safe[key] / max(1, extent - 1))
    if "pointers" in safe:
        safe["pointers"] = [relative_action(point, size) for point in safe["pointers"]]
    return safe


def action_signature(action):
    if isinstance(action, list):
        return [action_signature(item) for item in action]
    if isinstance(action, dict):
        return {key: action_signature(value) for key, value in action.items() if key not in {"note", "target", "repeat", "interval_ms", "text_redacted", "text_length"}}
    return action


def game_observation(png, context=None, captured=None):
    width, height = frame_dimensions(png)
    context = context if isinstance(context, dict) else {}
    nodes = context.get("nodes", [])
    nodes = nodes if isinstance(nodes, list) else []
    observation = {"width": width, "height": height, "size": [width, height], "package": str(context.get("package", "")), "activity": str(context.get("activity", "")), "state": hashlib.sha256(png).hexdigest(), "timestamp": time.monotonic() if captured is None else captured, "summary": str(context.get("summary", "")), "nodes": AI_disambiguate_nodes(nodes)}
    for key in ("capabilities", "input_timing", "task_state"):
        if isinstance(context.get(key), dict):
            observation[key] = dict(context[key])
    for key in ("nodes_at", "nodes_started_at"):
        value = context.get(key)
        if type(value) in (int, float) and math.isfinite(value) and value >= 0:
            observation[key] = value
    return observation


def observed_action_effect(episode, observation, confirmation=None):
    if not isinstance(episode, dict) or not isinstance(observation, dict):
        return None
    result = episode.get("result")
    if not isinstance(result, dict) or result.get("action_applied") is not True or not episode.get("expected"):
        return None
    action_id = str(result.get("action_id", episode.get("action_id", "")))
    applied_at = local_agent_number(result.get("action_applied_at"), -1)
    if not action_id or applied_at < 0 or str(episode.get("package", "")) != str(observation.get("package", "")) or not GameAI._nodes_fresh(observation, applied_at):
        return None
    expected = result.get("expected_effect")
    if not isinstance(expected, dict) or expected.get("kind") != "node_state":
        return None
    reference = str(expected.get("node_ref", ""))
    field = expected.get("field")
    value = expected.get("value")
    if not reference or field not in {"checked", "selected", "enabled", "focused"} or type(value) is not bool:
        return None
    before_states = result.get("before_node_states", {})
    prior = before_states.get(reference) if isinstance(before_states, dict) else None
    matches = AI_matching_nodes(observation.get("nodes", ()), reference)
    if not isinstance(prior, dict) or type(prior.get(field)) is not bool or len(matches) != 1 or prior[field] == value:
        return None
    node = matches[0]
    if type(node.get(field)) is not bool:
        return None
    if node[field] == value:
        evidence = str(node.get("text") or node.get("content_desc") or node.get("resource_id") or node.get("id") or reference).strip()
        return {"action_id": action_id, "fulfilled": True, "evidence": evidence, "node_ref": reference, "field": field, "value": value, "source": "verified_target_state"}
    if confirmation is None or not isinstance(confirmation, dict) or not GameAI._nodes_fresh(confirmation, applied_at):
        return None
    if str(confirmation.get("package", "")) != str(observation.get("package", "")) or str(confirmation.get("activity", "")) != str(observation.get("activity", "")):
        return None
    if confirmation["nodes_started_at"] <= observation["nodes_at"] or confirmation.get("capture_started_at", 0) <= observation.get("capture_started_at", 0):
        return None
    verified_matches = AI_matching_nodes(confirmation.get("nodes", ()), reference)
    if len(verified_matches) != 1 or type(verified_matches[0].get(field)) is not bool:
        return None
    verified_node = verified_matches[0]
    if verified_node[field] == value:
        evidence = str(verified_node.get("text") or verified_node.get("content_desc") or verified_node.get("resource_id") or verified_node.get("id") or reference).strip()
        return {"action_id": action_id, "fulfilled": True, "evidence": evidence, "node_ref": reference, "field": field, "value": value, "source": "verified_target_state"}
    if node[field] != prior[field] or verified_node[field] != prior[field]:
        return None
    evidence = str(verified_node.get("text") or verified_node.get("content_desc") or verified_node.get("resource_id") or verified_node.get("id") or reference).strip()
    return {"action_id": action_id, "fulfilled": False, "evidence": evidence, "node_ref": reference, "field": field, "value": value, "source": "verified_target_unchanged"}


class MemoryStore:
    def __init__(self, root):
        self.root = pathlib.Path(root)
        if path_is_link(self.root):
            raise OSError("经验数据库目录不得是符号链接")
        self.root.mkdir(parents=True, exist_ok=True)
        if path_is_link(self.root / "memory.sqlite3"):
            raise OSError("经验数据库文件不得是符号链接")
        self.lock = threading.RLock()
        self.db = sqlite3.connect(self.root / "memory.sqlite3", check_same_thread=False, timeout=AI_MEMORY_BUSY_SECONDS)
        self.db.row_factory = sqlite3.Row
        self.db.executescript("PRAGMA journal_mode=WAL; PRAGMA synchronous=NORMAL; CREATE TABLE IF NOT EXISTS settings(key TEXT PRIMARY KEY,value TEXT NOT NULL); CREATE TABLE IF NOT EXISTS events(id INTEGER PRIMARY KEY,ts TEXT NOT NULL,kind TEXT NOT NULL,payload TEXT NOT NULL); CREATE TABLE IF NOT EXISTS transitions(id INTEGER PRIMARY KEY,ts TEXT NOT NULL,package TEXT NOT NULL,scene TEXT NOT NULL,state TEXT NOT NULL,action TEXT NOT NULL,result TEXT NOT NULL); CREATE INDEX IF NOT EXISTS transition_scene ON transitions(package,scene,id);")
        self.db.execute("PRAGMA busy_timeout=" + str(AI_MEMORY_BUSY_SECONDS * AI_MILLISECONDS_PER_SECOND))
        columns = {row[1] for row in self.db.execute("PRAGMA table_info(transitions)")}
        if "episode_id" not in columns:
            self.db.execute("ALTER TABLE transitions ADD COLUMN episode_id TEXT NOT NULL DEFAULT ''")
        self.db.execute("CREATE INDEX IF NOT EXISTS transition_episode ON transitions(episode_id,id)")
        self.db.executescript("CREATE TABLE IF NOT EXISTS credited_outcomes(episode_id TEXT PRIMARY KEY,ts TEXT NOT NULL,outcome TEXT NOT NULL); CREATE TABLE IF NOT EXISTS action_feedback(action_id TEXT PRIMARY KEY,ts TEXT NOT NULL,fulfilled INTEGER NOT NULL,evidence TEXT NOT NULL,forecast REAL NOT NULL); CREATE TABLE IF NOT EXISTS strategy_evidence(package TEXT NOT NULL,game TEXT NOT NULL,phase TEXT NOT NULL,context_key TEXT NOT NULL,features TEXT NOT NULL,action_key TEXT NOT NULL,action TEXT NOT NULL,outcome_trials INTEGER NOT NULL DEFAULT 0,outcome_sum REAL NOT NULL DEFAULT 0,effect_trials INTEGER NOT NULL DEFAULT 0,effect_successes INTEGER NOT NULL DEFAULT 0,last_seen TEXT NOT NULL,PRIMARY KEY(package,game,phase,context_key,action_key)); CREATE INDEX IF NOT EXISTS evidence_lookup ON strategy_evidence(package,game,phase,last_seen);")
        evidence_columns = {row[1] for row in self.db.execute("PRAGMA table_info(strategy_evidence)")}
        for column in ("verified_effect_trials", "verified_effect_successes"):
            if column not in evidence_columns:
                self.db.execute("ALTER TABLE strategy_evidence ADD COLUMN " + column + " INTEGER NOT NULL DEFAULT 0")
        self.db.commit()
        self.closed = False

    def get(self, key, default=None):
        with self.lock:
            row = self.db.execute("SELECT value FROM settings WHERE key=?", (str(key),)).fetchone()
            if row is None:
                return default
            try:
                return json.loads(row[0])
            except ValueError:
                return default

    def set(self, key, value):
        with self.lock, self.db:
            self.db.execute("INSERT INTO settings(key,value) VALUES(?,?) ON CONFLICT(key) DO UPDATE SET value=excluded.value", (str(key), json.dumps(value, ensure_ascii=False)))

    def log(self, kind, **fields):
        with self.lock, self.db:
            self.db.execute("INSERT INTO events(ts,kind,payload) VALUES(?,?,?)", (utc_now(), str(kind), json.dumps(fields, ensure_ascii=False, default=str)))

    def record(self, package, scene, observation, action, result, episode_id=""):
        if not isinstance(result, dict):
            raise ValueError("动作结果必须是 JSON 对象")
        result.setdefault("action_id", uuid.uuid4().hex)
        result.setdefault("before_visible_text", AI_visible_text(observation))
        with self.lock, self.db:
            row = self.db.execute("INSERT INTO transitions(ts,package,scene,state,action,result,episode_id) VALUES(?,?,?,?,?,?,?)", (utc_now(), str(package), str(scene), observation.get("state", ""), json.dumps(stored_action(action), ensure_ascii=False), json.dumps(result, ensure_ascii=False, default=str), str(episode_id)))
            return row.lastrowid

    def _experience_identity(self, episode):
        action = episode.get("action", {})
        result = episode.get("result", {})
        if not isinstance(action, dict) or not isinstance(result, dict) or result.get("action_applied") is not True:
            return None
        if action.get("kind") in {"type", "wait", "touch_release_all"}:
            return None
        size = episode.get("size", result.get("size"))
        if not isinstance(size, (list, tuple)) or len(size) != AI_SPATIAL_DIMENSIONS or any(type(value) is not int or value <= 0 for value in size):
            return None
        features = episode.get("features", result.get("features", {}))
        if not isinstance(features, dict):
            return None
        package = str(episode.get("package", "")).strip()
        if not package:
            return None
        normalized = relative_action(action, size)
        signature = AI_action_identity(normalized)
        context = {key: features.get(key, "") for key in ("situation", "objective", "mode", "turn", "anchors")}
        packed_context = json.dumps(context, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        context_key = hashlib.sha256(packed_context.encode("utf-8")).hexdigest()
        action_key = hashlib.sha256(signature.encode("utf-8")).hexdigest()
        return (package, str(features.get("game", package)), str(features.get("phase", "unknown")), context_key, json.dumps(features, ensure_ascii=False, sort_keys=True), action_key, json.dumps(normalized, ensure_ascii=False, sort_keys=True))

    def _experience_credit(self, episode, reward, source="outcome"):
        identity = self._experience_identity(episode)
        if identity is None or type(reward) not in (int, float) or not math.isfinite(reward):
            return False
        if source not in {"outcome", "effect"}:
            raise ValueError("经验反馈来源无效")
        _, _, phase, _, _, _, _ = identity
        if source == "outcome" and phase not in {"playing", "unknown"}:
            return False
        trials = int(source == "outcome")
        outcomes = max(-1.0, min(1.0, float(reward))) if trials else 0.0
        effect_trials = int(source == "effect")
        effects = int(reward > 0) if effect_trials else 0
        self.db.execute("INSERT INTO strategy_evidence(package,game,phase,context_key,features,action_key,action,outcome_trials,outcome_sum,verified_effect_trials,verified_effect_successes,last_seen) VALUES(?,?,?,?,?,?,?,?,?,?,?,?) ON CONFLICT(package,game,phase,context_key,action_key) DO UPDATE SET outcome_trials=outcome_trials+excluded.outcome_trials,outcome_sum=outcome_sum+excluded.outcome_sum,verified_effect_trials=verified_effect_trials+excluded.verified_effect_trials,verified_effect_successes=verified_effect_successes+excluded.verified_effect_successes,features=excluded.features,action=excluded.action,last_seen=excluded.last_seen", identity + (trials, outcomes, effect_trials, effects, utc_now()))
        return True

    def _retained_episode_rows(self, episode_id):
        seen = set()
        for row in self.db.execute("SELECT id,package,action,result FROM transitions WHERE episode_id=? ORDER BY id", (episode_id,)):
            seen.add(row["id"])
            yield dict(row, source="live")
        folder = self.root / "archives"
        if not folder.is_dir():
            return
        if path_is_link(folder):
            raise OSError("经验归档目录不得是链接")
        for archive in sorted(folder.glob("transitions-*.jsonl.gz")):
            try:
                if path_is_link(archive) or not archive.is_file():
                    raise OSError("经验归档不是安全的普通文件")
                with gzip.open(archive, "rt", encoding="utf-8") as source:
                    first = source.readline()
                    if not first:
                        continue
                    record = json.loads(first)
                    metadata = record.get("archive_meta") if isinstance(record, dict) else None
                    if isinstance(metadata, dict):
                        if metadata.get("table") != "transitions" or episode_id not in metadata.get("episodes", []):
                            continue
                    elif isinstance(record, dict) and str(record.get("episode_id", "")) == episode_id and record.get("id") not in seen:
                        seen.add(record.get("id"))
                        yield dict(record, source="archive")
                    for line in source:
                        record = json.loads(line)
                        if isinstance(record, dict) and str(record.get("episode_id", "")) == episode_id and record.get("id") not in seen:
                            seen.add(record.get("id"))
                            yield dict(record, source="archive")
            except (OSError, ValueError, EOFError, UnicodeError) as exc:
                self.db.execute("INSERT INTO events(ts,kind,payload) VALUES(?,?,?)", (utc_now(), "experience_archive_read_error", json.dumps({"archive": archive.name, "episode_id": episode_id, "error": str(exc), "coverage": "retained_evidence"}, ensure_ascii=False)))

    def credit(self, episodes, signal, episode_id=None):
        if not isinstance(signal, dict):
            return False
        outcome = str(signal.get("outcome", "unknown"))
        evidence = str(signal.get("evidence", "")).strip()
        frames = signal.get("confirmation_frames", [])
        if outcome not in {"win", "loss"} or not evidence or signal.get("verified") is not True or not isinstance(frames, (list, tuple)) or len(frames) < AI_TERMINAL_CONFIRMATION_FRAMES or any(type(value) is not int or value <= 0 for value in frames) or len(set(frames)) != len(frames):
            return False
        episode_id = str(episode_id or next((str(item.get("episode_id", "")) for item in reversed(episodes) if isinstance(item, dict) and item.get("episode_id")), ""))
        if not episode_id:
            return False
        reward = 1.0 if outcome == "win" else -1.0
        credited = 0
        seen = set()
        def apply_credit(episode, attributed_reward):
            nonlocal credited
            try:
                identity = self._experience_identity(episode)
            except (TypeError, ValueError, OverflowError):
                return
            if identity is None:
                return
            package, game, phase, context_key, _, action_key, _ = identity
            key = (package, game, phase, context_key, action_key)
            if key in seen:
                return
            if self._experience_credit(episode, attributed_reward, "outcome"):
                seen.add(key)
                credited += 1
        with self.lock, self.db:
            existing = self.db.execute("SELECT outcome FROM credited_outcomes WHERE episode_id=?", (episode_id,)).fetchone()
            if existing is not None:
                return False
            rows_seen = 0
            sources = collections.Counter()
            retained = []
            for row in self._retained_episode_rows(episode_id):
                rows_seen += 1
                sources[row["source"]] += 1
                try:
                    result = json.loads(row["result"])
                    action = json.loads(row["action"])
                    if isinstance(result, dict) and isinstance(action, dict):
                        retained.append({"package": row["package"], "features": result.get("features", {}), "size": result.get("size"), "action": action, "result": result})
                except (TypeError, ValueError, KeyError):
                    continue
            if not retained:
                retained = [episode for episode in episodes if isinstance(episode, dict) and str(episode.get("episode_id", "")) == episode_id]
            retained.sort(key=lambda episode: local_agent_number(episode.get("result", {}).get("action_applied_at")))
            horizon = len(retained)
            discount = max(0.0, 1 - 1 / math.sqrt(horizon + 1))
            for distance, episode in enumerate(reversed(retained)):
                apply_credit(episode, reward * discount ** distance)
            self.db.execute("INSERT INTO credited_outcomes(episode_id,ts,outcome) VALUES(?,?,?)", (episode_id, utc_now(), outcome))
            self.db.execute("INSERT INTO events(ts,kind,payload) VALUES(?,?,?)", (utc_now(), "verified_game_outcome", json.dumps({"signal": signal, "source": "distinct_result_frames", "attribution": "temporal_discounted_episode_association", "coverage": "retained_evidence", "retained_rows": dict(sources), "credited_state_actions": credited, "episode_id": episode_id}, ensure_ascii=False)))
        return True

    def feedback(self, episode, effect, confidence, observation=None, confirmation=None):
        if not isinstance(episode, dict) or not isinstance(effect, dict) or type(effect.get("fulfilled")) is not bool or not isinstance(observation, dict):
            return False
        if type(confidence) not in (int, float) or not math.isfinite(confidence):
            return False
        result = episode.get("result", {})
        if not isinstance(result, dict) or result.get("action_applied") is not True or not str(episode.get("expected", "")).strip():
            return False
        action_id = str(result.get("action_id", episode.get("action_id", "")))
        if not action_id or effect.get("action_id") != action_id or episode.get("feedback_applied"):
            return False
        if str(observation.get("package", "")) != str(episode.get("package", "")):
            return False
        captured = observation.get("capture_started_at", observation.get("timestamp"))
        applied = result.get("action_applied_at")
        if any(type(value) not in (int, float) or not math.isfinite(value) for value in (captured, applied)) or captured <= applied:
            return False
        nodes_started = observation.get("nodes_started_at")
        nodes_finished = observation.get("nodes_at")
        if any(type(value) not in (int, float) or not math.isfinite(value) for value in (nodes_started, nodes_finished)) or not applied < nodes_started <= nodes_finished <= time.monotonic():
            return False
        verified = observed_action_effect(episode, observation, confirmation)
        if verified is None or any(effect.get(key) != verified.get(key) for key in ("action_id", "fulfilled", "evidence", "node_ref", "field", "value", "source")):
            return False
        evidence = verified["evidence"]
        with self.lock, self.db:
            if self._experience_identity(episode) is None:
                return False
            inserted = self.db.execute("INSERT OR IGNORE INTO action_feedback(action_id,ts,fulfilled,evidence,forecast) VALUES(?,?,?,?,?)", (action_id, utc_now(), int(effect["fulfilled"]), evidence, max(0.0, min(1.0, confidence))))
            if inserted.rowcount == 0:
                return False
            credited = self._experience_credit(episode, 1.0 if effect["fulfilled"] else -1.0, "effect")
        episode["feedback_applied"] = bool(credited)
        return bool(credited)

    def recall(self, package, features=None, limit=AI_MEMORY_DEFAULT_RECALL):
        features = features if isinstance(features, dict) else {}
        count = max(0, int(limit))
        if not count:
            return []
        game = str(features.get("game", package))
        phase = str(features.get("phase", "unknown"))
        pool = count * max(1, math.isqrt(count))
        with self.lock:
            rows = self.db.execute("SELECT * FROM strategy_evidence WHERE package=? AND game=? AND phase=? AND outcome_trials+verified_effect_trials>0 ORDER BY outcome_trials+verified_effect_trials DESC,last_seen DESC LIMIT ?", (str(package), game, phase, pool)).fetchall()
        recalled = []
        for row in rows:
            try:
                past_features = json.loads(row["features"])
                action = json.loads(row["action"])
            except (TypeError, ValueError):
                continue
            if not isinstance(past_features, dict) or not isinstance(action, dict):
                continue
            similarity = AI_context_similarity(features, past_features)
            if similarity <= 0:
                continue
            terminal_trials = max(0, int(row["outcome_trials"]))
            effect_trials = max(0, int(row["verified_effect_trials"]))
            wins = (terminal_trials + row["outcome_sum"]) / 2
            result_mean, result_deviation = AI_posterior(wins, terminal_trials - wins)
            effect_mean, effect_deviation = AI_posterior(row["verified_effect_successes"], effect_trials - row["verified_effect_successes"])
            if terminal_trials:
                mean, deviation = 2 * result_mean - 1, 2 * result_deviation
            else:
                mean, deviation = 2 * effect_mean - 1, 2 * effect_deviation
            guidance = "candidate" if mean - deviation > 0 else "avoid" if mean + deviation < 0 else "uncertain"
            recalled.append({"game": game, "phase": phase, "situation": past_features.get("situation", ""), "features": past_features, "action_relative_1000": action, "observations": terminal_trials + effect_trials, "outcome_trials": terminal_trials, "outcome_return": 2 * result_mean - 1, "effect_trials": effect_trials, "effect_success_rate": effect_mean if effect_trials else None, "uncertainty": deviation, "state_similarity": similarity, "guidance": guidance, "source": "verified_terminal_and_target_state"})
        recalled.sort(key=lambda item: (item["state_similarity"], item["observations"] / (item["observations"] + 1) * (1 - item["uncertainty"]), abs(item["outcome_return"])), reverse=True)
        return recalled[:count]

    def backup(self, target, cancel=None):
        check_cancel(cancel)
        source = sqlite3.connect((self.root / "memory.sqlite3").resolve().as_uri() + "?mode=ro", uri=True, timeout=0)
        destination = None
        try:
            check_cancel(cancel)
            destination = sqlite3.connect(str(target), timeout=0)
            source.backup(destination, pages=AI_MEMORY_BACKUP_PAGES, progress=lambda *_: check_cancel(cancel), sleep=AI_MEMORY_BACKUP_YIELD_SECONDS)
            check_cancel(cancel)
        finally:
            if destination is not None:
                destination.close()
            source.close()

    def diagnostic_events(self, limit=AI_MEMORY_DIAGNOSTIC_LIMIT):
        count = max(1, int(limit))
        with self.lock:
            rows = self.db.execute("SELECT ts,kind,payload FROM events WHERE kind LIKE '%error%' OR kind IN ('preparation_retry','recovering','worker_error','stale_decision_rejected','game_ai_backend_failed','stop_worker_stalled','fast_touch_failed') ORDER BY id DESC LIMIT ?", (count,)).fetchall()
        events = []
        for row in reversed(rows):
            try:
                payload = json.loads(row["payload"])
            except (TypeError, ValueError):
                payload = {}
            details = {name: str(payload[name])[:AI_TEXT_FIELD_LIMIT] for name in ("component", "error", "reason", "attempt", "backend", "phase", "age_seconds", "visual_drift") if name in payload} if isinstance(payload, dict) else {}
            events.append({"time": row["ts"], "kind": row["kind"], "detail": details})
        return events

    @staticmethod
    def _verify_archive(path, metadata, records):
        with gzip.open(path, "rt", encoding="utf-8") as source:
            header = json.loads(next(source, ""))
            if not isinstance(header, dict) or header.get("archive_meta") != metadata:
                raise OSError("经验压缩包头与待归档记录不一致")
            for expected in records:
                line = source.readline()
                if not line or json.loads(line) != expected:
                    raise OSError("经验归档记录内容验证失败，原数据库保持不变")
            if source.readline():
                raise OSError("经验归档记录数量不一致，原数据库保持不变")
        return True

    def maintain(self):
        free_memory = max(1, available_memory_mb()) * AI_BYTES_PER_MEBIBYTE
        disk = shutil.disk_usage(self.root)
        for table, initial_retained in (("events", AI_MEMORY_EVENT_RECORDS), ("transitions", AI_MEMORY_TRANSITION_RECORDS)):
            with self.lock:
                if self.closed:
                    return
                count = int(self.db.execute("SELECT COUNT(*) FROM " + table).fetchone()[0])
                sample_count = max(1, math.isqrt(count))
                field = "payload" if table == "events" else "result"
                average = self.db.execute("SELECT AVG(LENGTH(" + field + ")) FROM (SELECT " + field + " FROM " + table + " ORDER BY id DESC LIMIT ?)", (sample_count,)).fetchone()[0] or 1
                retained = max(sample_count, min(initial_retained, int(min(free_memory, disk.free) / max(1, average))))
                batch = min(AI_MEMORY_ARCHIVE_BATCH, max(1, count - retained))
                if count <= retained:
                    continue
                if table == "transitions":
                    active = {row["episode_id"] for row in self.db.execute("SELECT t.episode_id FROM transitions t JOIN (SELECT package,MAX(id) AS latest FROM transitions WHERE episode_id!='' GROUP BY package) latest ON latest.latest=t.id LEFT JOIN credited_outcomes c ON c.episode_id=t.episode_id WHERE c.episode_id IS NULL")}
                    if active:
                        placeholders = ",".join("?" for _ in active)
                        records = [dict(row) for row in self.db.execute("SELECT * FROM transitions WHERE episode_id NOT IN (" + placeholders + ") ORDER BY id LIMIT ?", (*active, batch)).fetchall()]
                    else:
                        records = [dict(row) for row in self.db.execute("SELECT * FROM transitions ORDER BY id LIMIT ?", (batch,)).fetchall()]
                else:
                    records = [dict(row) for row in self.db.execute("SELECT * FROM " + table + " ORDER BY id LIMIT ?", (batch,)).fetchall()]
            if not records:
                continue
            folder = self.root / "archives"
            folder.mkdir(exist_ok=True)
            name = table + "-" + str(records[0]["id"]) + "-" + str(records[-1]["id"]) + ".jsonl.gz"
            temporary = folder / (name + ".part")
            if path_is_link(folder) or path_is_link(temporary) or path_is_link(folder / name):
                raise OSError("历史归档存储路径不安全")
            metadata = {"table": table, "rows": len(records), "first_id": records[0]["id"], "last_id": records[-1]["id"]}
            if table == "transitions":
                metadata["episodes"] = sorted({str(record["episode_id"]) for record in records})
            destination = folder / name
            try:
                if destination.exists():
                    self._verify_archive(destination, metadata, records)
                else:
                    with temporary.open("xb") as stream:
                        with gzip.GzipFile(filename="", mode="wb", fileobj=stream) as compressed:
                            compressed.write((json.dumps({"archive_meta": metadata}, ensure_ascii=False) + "\n").encode("utf-8"))
                            for row in records:
                                compressed.write((json.dumps(row, ensure_ascii=False) + "\n").encode("utf-8"))
                        stream.flush()
                        os.fsync(stream.fileno())
                    self._verify_archive(temporary, metadata, records)
                    os.replace(temporary, destination)
                    self._verify_archive(destination, metadata, records)
                with self.lock:
                    if self.closed:
                        return
                    with self.db:
                        self.db.executemany("DELETE FROM " + table + " WHERE id=?", ((row["id"],) for row in records))
            finally:
                with contextlib.suppress(OSError):
                    temporary.unlink()
        with self.lock:
            if self.closed:
                return
            self.db.execute("PRAGMA optimize")
        folder = self.root / "archives"
        if folder.is_dir() and not path_is_link(folder):
            files = sorted((path for path in folder.glob("*.jsonl.gz") if path.is_file() and not path_is_link(path)), key=lambda path: path.stat().st_mtime_ns)
            size = sum(path.stat().st_size for path in files)
            retention = min(AI_MEMORY_ARCHIVE_MAX_BYTES, shutil.disk_usage(self.root).free // AI_MEMORY_ARCHIVE_FREE_SHARE)
            for archive in files:
                if size <= retention or self.closed:
                    break
                removed = archive.stat().st_size
                archive.unlink()
                size -= removed
                with self.lock:
                    if self.closed:
                        return
                    with self.db:
                        self.db.execute("INSERT INTO events(ts,kind,payload) VALUES(?,?,?)", (utc_now(), "experience_archive_evicted", json.dumps({"archive": archive.name, "bytes": removed, "retention_bytes": retention, "coverage": "retained_evidence"}, ensure_ascii=False)))

    def close(self):
        with self.lock:
            if not self.closed:
                self.closed = True
                self.db.close()


CONTROL_PERCENT_SCALE = 100


CONTROL_SUPERVISOR_HEARTBEAT_SECONDS = 3.0


CONTROL_SHUTDOWN_GRACE_SECONDS = 4.0


CONTROL_SECONDS_PER_MINUTE = 60


CONTROL_MILLISECONDS_PER_SECOND = 1000


CONTROL_BYTES_PER_MIB = 1024 ** 2


CONTROL_ESTIMATION_CONFIDENCE = 0.95


CONTROL_RELATIVE_PRECISION = 0.2


CONTROL_LATENCY_QUANTILE = 0.95


CONTROL_TIMER_BOOTSTRAP_SECONDS = 0.05


CONTROL_FRAME_BOOTSTRAP_HZ = 60


CONTROL_MODEL_BOOTSTRAP_SECONDS = 1.0


CONTROL_ANDROID_MIN_MB = 1536


CONTROL_ANDROID_MAX_MB = 8192


CONTROL_DESKTOP_RESERVE_FRACTION = 0.125


CONTROL_ANDROID_OVERHEAD_FRACTION = 0.25


CONTROL_DESKTOP_CORE_FRACTION = 0.25


CONTROL_CAPTURE_CPU_SHARE = 0.5


CONTROL_MEMORY_CRITICAL_FRACTION = 0.5


CONTROL_INITIAL_SCENE_DRIFT = 0.5


CONTROL_INITIAL_MOTION_DRIFT = 0.35


CONTROL_INSTALL_PERMANENT_ERRORS = ("INSTALL_FAILED_INVALID_APK", "INSTALL_PARSE_FAILED_", "INSTALL_FAILED_NO_MATCHING_ABIS", "INSTALL_FAILED_OLDER_SDK", "INSTALL_FAILED_UPDATE_INCOMPATIBLE", "INSTALL_FAILED_VERSION_DOWNGRADE", "INSTALL_FAILED_MISSING_SPLIT", "INSTALL_FAILED_CONFLICTING_PROVIDER", "INSTALL_FAILED_DUPLICATE_PACKAGE", "INSTALL_FAILED_TEST_ONLY")
CONTROL_INSTALL_FAILURE_HISTORY = AI_MEMORY_DEFAULT_RECALL * AI_MEMORY_DEFAULT_RECALL
CONTROL_RETRY_BACKOFF_BASE = 2


CONTROL_RETRY_JITTER_FRACTION = 0.25


CONTROL_INITIAL_RETRY_SECONDS = 1.0


CONTROL_INITIAL_RESOURCE_RETRY_SECONDS = 15.0


CONTROL_RETRY_CEILING_SECONDS = 60.0


CONTROL_INITIAL_RECOVERY_FAILURES = 3


CONTROL_INITIAL_INVALID_PLANS = 4


CONTROL_NON_GAME_PACKAGES = frozenset(("android", "com.android.settings", "com.android.systemui", "com.android.vending", "com.android.packageinstaller", "com.android.permissioncontroller", "com.google.android.permissioncontroller", "com.google.android.packageinstaller"))


CONTROL_MONITORED_WORK_PHASES = frozenset(("observe", "observe_after", "observe_stale", "observe_nodes", "act", "plan", "judge_result", "confirm_result", "storage"))


CONTROL_DIAGNOSTIC_PRECISION = 4


CONTROL_STATUS_CHARACTERS = 240


CONTROL_CONTEXT_CHARACTERS = 1100


CONTROL_HISTORY_CAPACITY = 64


CONTROL_LOG_CAPACITY = 8192


CONTROL_INPUT_CAPACITY = 64


CONTROL_TOUCH_FRAME_CAPACITY = 256


CONTROL_ARCHIVE_TAIL_BYTES = 2 * CONTROL_BYTES_PER_MIB


CONTROL_ARCHIVE_COPY_BYTES = CONTROL_BYTES_PER_MIB


CONTROL_CAPTURE_HISTORY_SECONDS = CONTROL_SECONDS_PER_MINUTE


CONTROL_MODEL_PROFILE_SCHEMA = 1


CONTROL_PREPARATION_STAGES = ("检查本地安卓环境", "准备本地输入与资源", "验证截图与本地策略", "安装导入的APK", "完成就绪检查")


CONTROL_WINDOWS_POINTER_BYTES = 8


CONTROL_PYTHON_MIN_VERSION = (3, 10)


CONTROL_WATCHDOG_ARGUMENTS = 4


CONTROL_RESUME_ARGUMENTS = 3


CONTROL_DPI_PER_MONITOR_V2 = -4


CONTROL_DPI_PER_MONITOR = 2


class ControlTuning:
    def __init__(self, path):
        self.path = pathlib.Path(path)
        self.lock = threading.RLock()
        self.capacity = math.ceil(statistics.NormalDist().inv_cdf((1 + CONTROL_ESTIMATION_CONFIDENCE) / 2) ** 2 / CONTROL_RELATIVE_PRECISION ** 2)
        self.samples = {}
        self.counts = collections.Counter()
        self.pressure = 0.0
        self.clock_floor = max(time.get_clock_info("monotonic").resolution, CONTROL_TIMER_BOOTSTRAP_SECONDS / CONTROL_FRAME_BOOTSTRAP_HZ)
        self.identity = {"machine": platform.machine(), "cpus": os.cpu_count(), "memory_mb": physical_memory_mb()}
        saved = read_json(self.path, {})
        if isinstance(saved, dict) and saved.get("schema") == CONTROL_MODEL_PROFILE_SCHEMA and saved.get("hardware") == self.identity:
            data = saved.get("samples", {})
            if isinstance(data, dict):
                for key, values in data.items():
                    if isinstance(key, str) and isinstance(values, list):
                        for value in values[-self.capacity:]:
                            self.observe(key, value)

    def observe(self, key, value):
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value < 0:
            return
        with self.lock:
            self.samples.setdefault(str(key), collections.deque(maxlen=self.capacity)).append(float(value))
            self.counts[str(key)] += 1

    def estimate(self, key, fallback=CONTROL_TIMER_BOOTSTRAP_SECONDS, quantile=None):
        with self.lock:
            values = sorted(self.samples.get(str(key), ()))
        if not values:
            return max(self.clock_floor, float(fallback))
        if quantile is None:
            return statistics.median(values)
        position = min(1.0, max(0.0, float(quantile))) * (len(values) - 1)
        lower = math.floor(position)
        upper = math.ceil(position)
        return values[lower] + (values[upper] - values[lower]) * (position - lower)

    def deadline(self, key, fallback=CONTROL_MODEL_BOOTSTRAP_SECONDS):
        median = self.estimate(key, fallback)
        tail = self.estimate(key, fallback, CONTROL_LATENCY_QUANTILE)
        with self.lock:
            values = tuple(self.samples.get(str(key), ()))
        deviation = statistics.median(abs(value - median) for value in values) if values else median
        confidence = statistics.NormalDist().inv_cdf((1 + CONTROL_ESTIMATION_CONFIDENCE) / 2)
        estimation_error = median / math.sqrt(max(1, len(values)))
        return max(self.clock_floor, float(fallback), tail + confidence * max(deviation, estimation_error, self.clock_floor))

    def interval(self, key, fallback=CONTROL_TIMER_BOOTSTRAP_SECONDS, duty=CONTROL_CAPTURE_CPU_SHARE):
        work = self.estimate(key, fallback)
        with self.lock:
            pressure = self.pressure
        usable = max(self.clock_floor, min(1.0, duty / (1 + pressure)))
        return max(self.clock_floor, work / usable)

    def retry(self, key, attempt, resource=False):
        initial = CONTROL_INITIAL_RESOURCE_RETRY_SECONDS if resource else CONTROL_INITIAL_RETRY_SECONDS
        measured = self.estimate("retry:" + str(key), initial)
        exponent = min(max(0, int(attempt) - 1), math.ceil(math.log(CONTROL_RETRY_CEILING_SECONDS / min(CONTROL_RETRY_CEILING_SECONDS, initial), CONTROL_RETRY_BACKOFF_BASE)))
        delay = min(CONTROL_RETRY_CEILING_SECONDS, max(initial, measured) * CONTROL_RETRY_BACKOFF_BASE ** exponent)
        return max(self.clock_floor, delay * random.uniform(1 - CONTROL_RETRY_JITTER_FRACTION, 1))

    def scene_threshold(self, key, fallback=CONTROL_INITIAL_SCENE_DRIFT):
        with self.lock:
            values = tuple(self.samples.get(key, ()))
        if len(values) < math.ceil(1 / (1 - CONTROL_ESTIMATION_CONFIDENCE)):
            return fallback
        baseline = statistics.median(values)
        deviation = statistics.median(abs(value - baseline) for value in values)
        band = statistics.NormalDist().inv_cdf((1 + CONTROL_ESTIMATION_CONFIDENCE) / 2) * deviation
        return min(1.0, max(sys.float_info.epsilon, baseline + max(band, math.sqrt(sys.float_info.epsilon))))

    def snapshot(self):
        with self.lock:
            keys = tuple(self.samples)
            counts = dict(self.counts)
            pressure = self.pressure
        return {"sample_count": counts, "pressure": pressure, "estimation_confidence": CONTROL_ESTIMATION_CONFIDENCE, **{key + "_seconds": round(self.estimate(key), CONTROL_DIAGNOSTIC_PRECISION) for key in keys if key in {"capture", "plan", "input", "context", "accessibility", "ui_render", "ui_poll"}}}

    def save(self):
        with self.lock:
            value = {"schema": CONTROL_MODEL_PROFILE_SCHEMA, "hardware": self.identity, "samples": {key: list(values) for key, values in self.samples.items()}}
        atomic_json(self.path, value)


def protected_desktop_memory_mb(total_mb, variation_mb=0):
    total, variation = float(total_mb), float(variation_mb)
    if not math.isfinite(total) or total <= 0 or not math.isfinite(variation) or variation < 0:
        raise ComponentFailure("resources", "桌面保留内存测量值无效")
    return min(math.ceil(total), math.ceil(max(total * CONTROL_DESKTOP_RESERVE_FRACTION, variation)))


def runtime_resource_budget(total_mb, available_mb, cpu_count, model_mb=0, variation_mb=0, busy_fraction=0.0):
    total_mb, available_mb = int(total_mb), int(available_mb)
    if total_mb <= 0 or not 0 <= available_mb <= total_mb:
        raise ComponentFailure("resources", "无法获得可信的物理内存容量，正在重新检测")
    cores = max(1, int(cpu_count or 1))
    reserve = protected_desktop_memory_mb(total_mb, variation_mb)
    remaining = max(0, available_mb - reserve - max(0, int(model_mb)))
    capacity = min(CONTROL_ANDROID_MAX_MB, math.floor(remaining / (1 + CONTROL_ANDROID_OVERHEAD_FRACTION)))
    android_mb = capacity if capacity >= CONTROL_ANDROID_MIN_MB else 0
    host_overhead = math.ceil(android_mb * CONTROL_ANDROID_OVERHEAD_FRACTION)
    busy_fraction = float(busy_fraction)
    if not math.isfinite(busy_fraction):
        raise ComponentFailure("resources", "处理器资源测量值无效")
    spare_fraction = max(CONTROL_DESKTOP_CORE_FRACTION, min(1.0, busy_fraction))
    usable = max(1, cores - math.ceil(cores * spare_fraction))
    threads = 1
    android_cores = max(1, usable - threads)
    return {"android_mb": android_mb, "android_capacity_mb": android_mb, "android_cores": android_cores, "ai_threads": threads, "protected_mb": reserve, "android_host_overhead_mb": host_overhead, "headroom_mb": max(0, remaining - android_mb - host_overhead), "model_mb": int(model_mb), "available_mb": available_mb}


def hash_file(path, algorithm="sha256", cancel=None):
    digest = hashlib.new(algorithm)
    with pathlib.Path(path).open("rb") as handle:
        while True:
            check_cancel(cancel)
            block = handle.read(RUNTIME_BYTES_PER_MIB)
            if not block:
                return digest.hexdigest()
            digest.update(block)


class SessionRunLatch:
    def __init__(self, root):
        self.handle = None
        self.local = threading.Event()
        self.local.set()
        self.kernel = None
        if os.name == "nt":
            self.kernel = ctypes.WinDLL("kernel32", use_last_error=True)
            self.kernel.CreateEventW.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_wchar_p]
            self.kernel.CreateEventW.restype = ctypes.c_void_p
            self.kernel.SetEvent.argtypes = [ctypes.c_void_p]
            self.kernel.SetEvent.restype = ctypes.c_int
            self.kernel.ResetEvent.argtypes = [ctypes.c_void_p]
            self.kernel.ResetEvent.restype = ctypes.c_int
            self.kernel.WaitForSingleObject.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
            self.kernel.WaitForSingleObject.restype = ctypes.c_uint32
            self.kernel.CloseHandle.argtypes = [ctypes.c_void_p]
            self.kernel.CloseHandle.restype = ctypes.c_int
            name = "Local\\OfflineGameAgent-" + hashlib.sha256(str(pathlib.Path(root).resolve()).casefold().encode("utf-8")).hexdigest()
            self.handle = self.kernel.CreateEventW(None, True, True, name)
            if not self.handle:
                raise ctypes.WinError(ctypes.get_last_error())

    def stop(self):
        self.local.set()
        if self.handle and not self.kernel.SetEvent(self.handle):
            raise ctypes.WinError(ctypes.get_last_error())

    def allow(self):
        if self.handle and not self.kernel.ResetEvent(self.handle):
            raise ctypes.WinError(ctypes.get_last_error())
        self.local.clear()

    def is_stopped(self):
        if self.handle:
            return self.kernel.WaitForSingleObject(self.handle, 0) != RUNTIME_WIN32_WAIT_TIMEOUT
        return self.local.is_set()

    def close(self):
        if self.handle:
            self.kernel.CloseHandle(self.handle)
            self.handle = None


class Controller:
    def __init__(self, root, events, supervised=False, autostart=True):
        self.root = pathlib.Path(root).resolve()
        self.root.mkdir(parents=True, exist_ok=True)
        self.workspace_lock = WorkspaceLock(self.root)
        self.run_latch = SessionRunLatch(self.root)
        if not supervised:
            self.run_latch.stop()
        self.events = events
        self.memory = MemoryStore(self.root / "data")
        self.tuning = ControlTuning(self.root / "state" / "control-profile.json")
        self.shutdown = threading.Event()
        self.ready_event = threading.Event()
        self._readiness = {"capture": False, "input": False, "decision": False}
        self.preparation_wake = threading.Event()
        self.lifecycle = threading.RLock()
        self.action_lock = threading.RLock()
        self.frame_lock = threading.Lock()
        self.frame_available = threading.Condition(self.frame_lock)
        self.progress_lock = threading.Lock()
        self.model_lock = threading.RLock()
        self.desired_running = False
        self.stopping = False
        self.android_ready = False
        self.generation = 0
        self.run_cancel = None
        self.worker = None
        self._pending_stop_release = None
        self.frame = None
        self.frame_number = 0
        self.frame_time = 0.0
        self.frame_start_time = 0.0
        self.capture_id = 0
        self.context = {}
        self.last_observation = None
        self.last_plan = None
        self.completed_steps = 0
        self.input_steps = 0
        self.wait_steps = 0
        self.ai_decisions = 0
        self.plan_seconds = None
        self.capture_seconds = None
        self.recoveries = 0
        self._android_assets = False
        self._ai_assets = False
        self._reset_android = False
        self._reset_ai = False
        self._manual_epoch = 0
        self._manual_queue = queue.Queue(maxsize=CONTROL_INPUT_CAPACITY)
        self._manual_cancel = threading.Event()
        self._manual_frames = collections.deque(maxlen=CONTROL_TOUCH_FRAME_CAPACITY)
        self._manual_demo_active = {}
        self._fast_pointers = {}
        self._fast_wake = threading.Event()
        self._fast_generation = None
        self._fast_update_serial = 0
        self._fast_applied_serial = 0
        self._fast_rejected_serial = 0
        self._fast_rejected_reason = ""
        self._fast_delivery = threading.Condition(self.lifecycle)
        self.perception = RealtimePerception()
        self.stale_rejections = 0
        self.scene_interruptions = 0
        self.run_started_at = 0.0
        self._jobs = set()
        self._pending_install_save_lock = threading.Lock()
        self._apk_cache_lock = threading.RLock()
        self.pending_installs_path = self.root / "state" / "pending-installs.json"
        stored_installs = read_json(self.pending_installs_path, [])
        self._pending_installs = collections.deque(item for item in stored_installs if isinstance(item, dict) and (isinstance(item.get("path"), str) and item["path"].lower().endswith(".apk") or isinstance(item.get("paths"), list) and item["paths"] and all(isinstance(value, str) and value.lower().endswith(".apk") for value in item["paths"]))) if isinstance(stored_installs, list) else collections.deque()
        self._resume_game_after_recovery = False
        self.last_game_package = str(self.memory.get("last_game_package", "") or "")
        previous_selection = self.memory.get("selected_game_package", None)
        if previous_selection is None:
            previously_imported = self.memory.get("installed_apks", [])
            known_games = {str(item.get("package", "")) for item in previously_imported if isinstance(item, dict)} if isinstance(previously_imported, list) else set()
            previous_selection = self.last_game_package if self.last_game_package in known_games else ""
        self.selected_game_package = str(previous_selection or "")
        self._last_launcher_probe = 0.0
        self._last_idle_notice = 0.0
        self._failed_game_launches = {}
        self._launch_failures = collections.Counter()
        self._memory_pressure = 0
        self._background_pressure = False
        self.ui_visible = True
        self.desktop_load = DesktopLoad()
        self.resource_sample = {}
        self.ready_seconds = None
        self.preparation_profile = {}
        self._startup_clock = RUNTIME_PROCESS_STARTED
        self._previous_available_mb = None
        self._episode_id = uuid.uuid4().hex
        self._terminal_seen = None
        self._terminal_candidate = None
        self._unverified_result_reviews = 0
        self.exporting = False
        self.logs = queue.Queue(maxsize=CONTROL_LOG_CAPACITY)
        self.last_progress = time.monotonic()
        self.progress_phase = "prepare"
        self.worker_progress_phase = "prepare"
        self.worker_progress_at = time.monotonic()
        self._active_action_until = 0.0
        self.run_intent_path = self.root / "state" / "run-intent.json"
        previous = persisted_run_record(self.root)
        self.intent_revision = previous["revision"] if previous else 0
        self.resume_requested = bool(supervised and not self.run_latch.is_stopped())
        self._resume_game_after_recovery = bool(self.resume_requested and self.selected_game_package)
        self._intent_dirty = False
        self._intent_lock = threading.RLock()
        self._intent_pending = None
        self.environment_error = ""
        self._last_memory_check = 0.0
        self._maintenance_active = False
        self._last_capture_saved = 0.0
        self._last_passive_analysis = 0.0
        self._passive_samples = None
        self._passive_identity = None
        self.supervision_enabled = False
        self.supervised_child = bool(supervised)
        self.supervisor_process_handle = None
        self.supervisor_thread = None
        self.supervisor_state_path = self.root / "state" / "supervisor.json"
        self.supervisor_program_path = pathlib.Path(__file__).resolve()
        self.android = AndroidRuntime(self.root, self.log, self.status, total_memory_mb=physical_memory_mb())
        self.ai = GameAI(self.root, self.log, self.status)
        self.log_thread = threading.Thread(target=self._write_logs, daemon=True, name="BlackBoxWriter")
        self.preparation_thread = threading.Thread(target=self._prepare_forever, daemon=True, name="AutomaticPreparation")
        self.frame_thread = threading.Thread(target=self._frames, daemon=True, name="AndroidScreen")
        self.context_thread = threading.Thread(target=self._contexts, daemon=True, name="AndroidContext")
        self.manual_thread = threading.Thread(target=self._manual_loop, daemon=True, name="ManualAndroidInput")
        self.fast_thread = threading.Thread(target=self._fast_loop, daemon=True, name="RealtimeTouchControl")
        self.watchdog_thread = threading.Thread(target=self._watchdog, daemon=True, name="RuntimeMonitor")
        if autostart:
            for thread in (self.log_thread, self.frame_thread, self.context_thread, self.manual_thread, self.fast_thread, self.watchdog_thread, self.preparation_thread):
                thread.start()
        self.log("session_open", version=APP_VERSION, python=platform.python_version(), system=platform.platform(), memory_mb=physical_memory_mb(), cpu_count=os.cpu_count())

    def readiness_checks(self):
        with self.lifecycle:
            return dict(self._readiness)

    def status(self, value):
        self.events.put(("status", str(value)))
        with self.progress_lock:
            if threading.current_thread() in (self.preparation_thread, self.worker):
                self.last_progress = time.monotonic()

    def milestone(self, description):
        if not self.shutdown.is_set():
            self.events.put(("milestone", {"step": CONTROL_PREPARATION_STAGES.index(description) + 1, "total": len(CONTROL_PREPARATION_STAGES), "description": str(description)}))

    def log(self, kind, **fields):
        try:
            self.logs.put_nowait((str(kind), fields))
        except queue.Full:
            self.events.put(("notice", "诊断写入暂时落后，控制循环继续运行"))

    def _write_logs(self):
        while True:
            try:
                item = self.logs.get(timeout=self.tuning.deadline("log"))
            except queue.Empty:
                if self.shutdown.is_set():
                    return
                continue
            try:
                if item is None:
                    return
                if item[0] == "__flush__":
                    item[1].set()
                elif item[0] == "__intent__":
                    with self._intent_lock:
                        record = self._intent_pending
                    if record is not None and record["revision"] == item[1]["revision"]:
                        atomic_json(self.run_intent_path, record)
                        self.memory.set("run_intent", record)
                        with self._intent_lock:
                            if self._intent_pending["revision"] == record["revision"]:
                                self._intent_dirty = False
                else:
                    self.memory.log(item[0], **item[1])
            except Exception as exc:
                self.events.put(("notice", "诊断文件暂时无法写入：" + str(exc)))
            finally:
                self.logs.task_done()

    def _heartbeat(self, phase):
        with self.progress_lock:
            now = time.monotonic()
            self.progress_phase = str(phase)
            self.last_progress = now
            if threading.current_thread() is self.worker:
                self.worker_progress_phase = str(phase)
                self.worker_progress_at = now

    def _job(self, work, name, background=False):
        def execute():
            try:
                with runtime_background_work(self.log) if background else contextlib.nullcontext():
                    work()
            except Cancelled:
                pass
            except Exception as exc:
                self.log("background_error", job=name, error=str(exc), traceback=traceback.format_exc())
                self.status(name + "：" + str(exc))
            finally:
                with self.lifecycle:
                    self._jobs.discard(threading.current_thread())
        thread = threading.Thread(target=execute, daemon=True, name=name)
        with self.lifecycle:
            self._jobs.add(thread)
        thread.start()
        return thread

    def _persist_run_intent(self, running):
        with self._intent_lock:
            self.intent_revision = max(time.time_ns(), self.intent_revision + 1)
            record = {"desired_running": bool(running), "revision": self.intent_revision, "changed_at": utc_now()}
            self._intent_pending = record
            self._intent_dirty = True
        try:
            atomic_json(self.run_intent_path, record)
        except OSError as exc:
            self.log("run_intent_immediate_write_failed", error=str(exc))
        try:
            self.logs.put_nowait(("__intent__", record))
        except queue.Full:
            self.log("intent_queue_busy", desired_running=bool(running))
        return True

    def _runtime_alive(self):
        return self.android.alive()

    def _budget(self, cancel=None):
        cancel = cancel or self.shutdown
        check_cancel(cancel)
        total, available = system_memory_mb()
        learner_mb = self.ai.preferred_host_budget(cancel)
        variation = self.tuning.estimate("memory_variation_mb", 0, CONTROL_LATENCY_QUANTILE)
        cpu = self.resource_sample.get("cpu_percent")
        busy = float(cpu) / CONTROL_PERCENT_SCALE if isinstance(cpu, (int, float)) and self.resource_sample.get("other_app_active") else 0.0
        budget = runtime_resource_budget(total, available, os.cpu_count(), learner_mb, variation, busy)
        existing = self.android.alive() or not getattr(self.android, "owned", True)
        if existing:
            budget.update(android_planned_mb=0, android_allocated_mb=self.android.memory_mb, android_mb=self.android.memory_mb, android_host_overhead_mb=0)
        else:
            budget.update(android_planned_mb=budget["android_mb"], android_allocated_mb=0)
            if budget["android_mb"] < CONTROL_ANDROID_MIN_MB:
                raise ComponentFailure("resources", f"可用内存 {available} MB 不足以启动本地安卓，同时保留桌面运行空间")
            budget = self.android.configure_resource_budget(budget, cancel)
        self.resource_budget = budget
        self.log("resource_budget", **budget)

    def _stage(self, name, work):
        started = time.monotonic()
        with self.progress_lock:
            self.preparation_profile[name] = {"state": "working", "started_seconds": round(started - self._startup_clock, CONTROL_DIAGNOSTIC_PRECISION)}
        try:
            value = work()
        except BaseException as exc:
            with self.progress_lock:
                self.preparation_profile[name].update(state="failed", seconds=round(time.monotonic() - started, CONTROL_DIAGNOSTIC_PRECISION), error=str(exc))
            raise
        with self.progress_lock:
            self.preparation_profile[name].update(state="complete", seconds=round(time.monotonic() - started, CONTROL_DIAGNOSTIC_PRECISION))
        self.tuning.observe("stage:" + name, time.monotonic() - started)
        self.log("startup_stage", stage=name, **self.preparation_profile[name])
        return value

    def _prepare_stack(self):
        self._heartbeat("prepare_assets")
        cancel = self.shutdown
        with self.lifecycle:
            self._readiness = {"capture": False, "input": False, "decision": False}
        self.milestone(CONTROL_PREPARATION_STAGES[0])
        ai_done = threading.Event()
        ai_errors = []
        def load_ai():
            try:
                with self.model_lock:
                    if not self._ai_assets:
                        self._stage("ai_assets", lambda: self.ai.prepare(cancel))
                        self._ai_assets = True
                    self._stage("ai_load", lambda: self.ai.start(cancel))
            except BaseException as exc:
                ai_errors.append(exc)
            finally:
                ai_done.set()
        self._job(load_ai, "PrepareLocalPolicy")
        def start_android():
            with self.action_lock:
                self.android.ensure_running(cancel)
                verified = self.android.capabilities() if self.android.capabilities().get("verified") and self.android.alive() else self._stage("input_verify", lambda: self.android.validate_input(cancel))
                if not isinstance(verified, dict) or verified.get("verified") is not True:
                    raise ComponentFailure("android", "输入通道未通过验证")
                with self.lifecycle:
                    self._readiness["input"] = True
            captured = time.monotonic()
            picture = self.android.screenshot(cancel)
            finished = time.monotonic()
            game_observation(picture)
            context = self.android.game_context(cancel)
            context.update(nodes=[], nodes_started_at=0.0, nodes_at=0.0)
            context["context_at"] = time.monotonic()
            with self.frame_lock:
                self.context = context
            with self.lifecycle:
                self.android_ready = True
            self._publish_frame(picture, captured, finished)
            self._fast_wake.set()
            return picture
        try:
            if not self._android_assets:
                try:
                    self._stage("android_assets", lambda: self.android.prepare(cancel))
                    self._android_assets = True
                except Cancelled:
                    raise
                except Exception as exc:
                    raise ComponentFailure("android_assets", exc) from exc
            self.milestone(CONTROL_PREPARATION_STAGES[1])
            self._stage("resource_plan", lambda: self._budget(cancel=cancel))
            self._heartbeat("android_start")
            try:
                png = self._stage("android_boot", start_android)
            except Cancelled:
                raise
            except Exception as exc:
                raise ComponentFailure("android", exc) from exc
        finally:
            while not ai_done.wait(RUNTIME_CANCEL_POLL_SECONDS):
                check_cancel(cancel)
        if ai_errors:
            if isinstance(ai_errors[0], Cancelled):
                raise ai_errors[0]
            raise ComponentFailure("ai", ai_errors[0]) from ai_errors[0]
        self.milestone(CONTROL_PREPARATION_STAGES[2])
        self.status("正在验证真实截图和本地决策通道")
        with self.model_lock:
            try:
                self._stage("ai_visual_verify", lambda: self.ai.verify_inference(png, cancel))
            except Cancelled:
                raise
            except Exception as exc:
                raise ComponentFailure("android", "截图解析验证失败：" + str(exc)) from exc
            with self.lifecycle:
                self._readiness["capture"] = True
            self.android._save_graphics_profile()
            with self.frame_lock:
                context = dict(self.context)
            observation = game_observation(png, context)
            observation["capabilities"] = self.android.capabilities()
            try:
                verification = self._stage("ai_decision_verify", lambda: self.ai.validate_decision(observation, png, cancel))
            except Cancelled:
                raise
            except Exception as exc:
                raise ComponentFailure("ai", exc) from exc
            if not isinstance(verification, dict) or verification.get("verified") is not True:
                raise ComponentFailure("ai", "本地策略没有通过动作生成验证")
            with self.lifecycle:
                self._readiness["decision"] = True
        self.milestone("安装导入的APK")
        self._restore_cached_games(cancel)
        self._stage("game_restore", lambda: self._process_pending_installs(cancel))
        with self.lifecycle:
            resume_package = self.selected_game_package if self._resume_game_after_recovery and (self.desired_running or self.resume_requested) else ""
            resume_generation = self.generation
            resume_cancel = CombinedCancel(cancel, self.run_cancel)
            self._resume_game_after_recovery = False
        if resume_package:
            with self.action_lock:
                with self.lifecycle:
                    permitted = self.generation == resume_generation and (self.desired_running or self.resume_requested) and not self.stopping
                if permitted and resume_package not in self.android.user_packages(resume_cancel):
                    self.log("game_auto_resume_target_unavailable", package=resume_package, continue_monitoring=True)
                elif permitted and self.android.game_context(resume_cancel).get("package") != resume_package:
                    self.android.launch_package(resume_package, resume_cancel)
                    self.log("game_auto_relaunched", package=resume_package)
        check_cancel(cancel)
        self.milestone(CONTROL_PREPARATION_STAGES[-1])
        self.environment_error = ""
        self.log("preparation_verified", size=frame_dimensions(png), algorithm=self.ai.model_name, backend=self.ai.backend, screenshot_verified=True, capabilities=self.android.capabilities(), actions_executed=0, stages=self._startup_diagnostics())

    def _save_pending_installs(self):
        with self._pending_install_save_lock:
            with self.lifecycle:
                pending = [dict(item) for item in self._pending_installs]
            try:
                atomic_json(self.pending_installs_path, pending)
                return True
            except Exception as exc:
                self.log("pending_install_save_error", error=str(exc))
                return False

    def _startup_diagnostics(self):
        with self.progress_lock:
            return {name: dict(value) for name, value in self.preparation_profile.items()}

    def _process_pending_installs(self, cancel=None):
        cancel = cancel or self.shutdown
        while True:
            check_cancel(cancel)
            with self.lifecycle:
                if not self._pending_installs:
                    return
                pending = dict(self._pending_installs[0])
            paths = [pathlib.Path(value) for value in pending.get("paths", [pending.get("path")])]
            self.android.last_installed_packages = []
            try:
                if self._skip_existing_restore(pending, cancel):
                    continue
                files = selected_apk_files(paths)
                fingerprint = pending.get("files") or [{"size": pending.get("size"), "mtime_ns": pending.get("mtime_ns")}]
                if len(fingerprint) != len(files):
                    raise ValueError("待安装 APK 列表不完整")
                for file, expected in zip(files, fingerprint):
                    info = file.stat()
                    if not isinstance(expected, dict) or expected.get("size") is not None and info.st_size != expected["size"] or expected.get("mtime_ns") is not None and info.st_mtime_ns != expected["mtime_ns"]:
                        raise ValueError("待安装 APK 不存在或已发生变化")
                if pending.get("restore_package"):
                    groups = self._cached_install_groups(paths, cancel)
                    if len(groups) != 1 or groups[0]["package"] != pending["restore_package"]:
                        raise ValueError("待恢复的缓存 APK 与原应用不一致")
                with self._apk_cache_lock, runtime_background_work(self.log):
                    files = self._cache_apks(files, cancel)
                paths = list(files)
                with self.lifecycle:
                    if self._pending_installs:
                        self._pending_installs[0].update(paths=[str(file) for file in files], files=[{"size": file.stat().st_size, "mtime_ns": file.stat().st_mtime_ns} for file in files])
                self._save_pending_installs()
                requirements = [apk_compatibility(file) for file in files]
                required_api = max((int(item["min_sdk"]) for item in requirements if item.get("min_sdk") is not None), default=0)
                package_abis = {}
                for file, requirement in zip(files, requirements):
                    package = apk_package_info(file)["package"]
                    package_abis.setdefault(package, set()).update(requirement["native_abis"])
                unsuitable_abis = {package: sorted(abis) for package, abis in package_abis.items() if abis and self.android.abis and abis.isdisjoint(self.android.abis)}
                old_api = self.android.device_api_level
                if old_api and (required_api > old_api or unsuitable_abis):
                    if pending.get("restore_package"):
                        raise ValueError("缓存游戏与目前 Android API 或 CPU 架构不兼容，保留原游戏缓存，未重复切换系统")
                    changed = False
                    if self.android.owned:
                        with self.action_lock:
                            changed = self.android.switch_compatible_image(required_api, package_abis, cancel)
                    if changed:
                        raise ComponentFailure("android", "已切换 APK 兼容系统镜像，重新验证后自动完成安装")
                    diagnostic = f"当前 Android API {old_api}，设备支持 {', '.join(self.android.abis) or '未知'}；APK 要求 API {required_api}"
                    if unsuitable_abis:
                        diagnostic += "；以下游戏原生库与设备不匹配：" + json.dumps(unsuitable_abis, ensure_ascii=False)
                    raise ValueError(diagnostic + "。请使用本机已有兼容模拟器；ARM-only 游戏无法仅靠切换 x86_64 系统镜像运行")
                with self.action_lock:
                    if self._skip_existing_restore(pending, cancel):
                        continue
                    self.android.install_apk(files, cancel)
                self._remember_install(files)
                packages = getattr(self.android, "last_installed_packages", [])
                if packages and (not pending.get("restore_package") or not self.selected_game_package):
                    self._select_game_package(str(packages[-1]), explicit=not bool(pending.get("restore_package")))
            except Cancelled:
                raise
            except Exception as exc:
                if isinstance(exc, ComponentFailure):
                    raise
                if not isinstance(exc, (ValueError, zipfile.BadZipFile)) and not self.android.alive():
                    raise ComponentFailure("android", exc) from exc
                permanent = isinstance(exc, (ValueError, zipfile.BadZipFile)) or any(marker in str(exc) for marker in CONTROL_INSTALL_PERMANENT_ERRORS)
                if not permanent:
                    with self.lifecycle:
                        if self._pending_installs and self._pending_installs[0].get("id") == pending.get("id"):
                            self._pending_installs[0]["attempts"] = max(0, int(pending.get("attempts", 0))) + 1
                    if not self._save_pending_installs():
                        self.log("pending_game_retry_save_failed", files=[str(file) for file in paths])
                    self.log("pending_game_install_retry", files=[str(file) for file in paths], error=str(exc), attempts=max(0, int(pending.get("attempts", 0))) + 1)
                    raise ComponentFailure("install", "APK 安装临时失败，保留安装队列并自动重试：" + str(exc)) from exc
                installed = list(getattr(self.android, "last_installed_packages", []))
                detail = str(exc)
                if installed:
                    completed = []
                    for file in paths:
                        try:
                            if apk_package_info(file)["package"] in installed:
                                completed.append(file)
                        except (OSError, ValueError, zipfile.BadZipFile):
                            continue
                    if completed:
                        self._remember_install(completed)
                    if not pending.get("restore_package") or not self.selected_game_package:
                        self._select_game_package(str(installed[-1]), explicit=not bool(pending.get("restore_package")))
                    detail = "已安装 " + "、".join(installed) + "；其余安装失败：" + detail
                with self.lifecycle:
                    if self._pending_installs:
                        self._pending_installs.popleft()
                self._save_pending_installs()
                self.log("pending_game_install_failed", files=[str(file) for file in paths], error=str(exc))
                failures_path = safe_workspace_file(self.root, self.root / "state" / "install-failures.json")
                failed_items = read_json(failures_path, [])
                failed_items = failed_items if isinstance(failed_items, list) else []
                failed_items.append({"time": utc_now(), "request": pending, "error": str(exc), "installed_packages": installed})
                try:
                    atomic_json(failures_path, failed_items[-CONTROL_INSTALL_FAILURE_HISTORY:])
                except OSError as record_error:
                    self.log("install_failure_history_save_failed", error=str(record_error))
                if pending.get("restore_package"):
                    self.log("cached_game_restore_failed", package=pending["restore_package"], image=self.android.IMAGE_PACKAGE, error=str(exc), automatic_retry=False)
                self.events.put(("install_result", {"ok": False, "files": [file.name for file in paths], "installed_packages": installed, "error": detail[:CONTROL_STATUS_CHARACTERS]}))
                continue
            with self.lifecycle:
                if self._pending_installs:
                    self._pending_installs.popleft()
            self._save_pending_installs()
            self.events.put(("install_result", {"ok": True, "files": [file.name for file in files]}))
            self.status("已完成本地安装：" + ", ".join(file.name for file in files))

    def _cached_install_groups(self, paths, cancel=None, excluded=()):
        imports = safe_workspace_file(self.root, self.root / "imports")
        files = []
        for value in paths:
            check_cancel(cancel)
            file = safe_workspace_file(self.root, value)
            try:
                file.relative_to(imports)
            except ValueError as exc:
                raise ValueError("只能恢复工作文件夹 imports 内的缓存 APK") from exc
            files.append(file)
        groups = {}
        for file in selected_apk_files(files):
            check_cancel(cancel)
            info = apk_package_info(file)
            groups.setdefault(info["package"], []).append((file, info))
        result = []
        for package, items in groups.items():
            if package in excluded:
                continue
            splits = [info["split"] for file, info in items]
            versions = {(info["version_code_major"], info["version_code"]) for file, info in items}
            if splits.count("") != 1 or len(splits) != len(set(splits)) or len(versions) != 1:
                raise ValueError("缓存应用缺少完整且版本一致的 base / split 组合：" + package)
            for file, info in items:
                if hash_file(file, "sha256", cancel) != file.parent.name:
                    raise ValueError("缓存 APK 内容校验失败：" + file.name)
            ordered = [file for file, info in sorted(items, key=lambda item: (bool(item[1]["split"]), item[1]["split"]))]
            result.append({"package": package, "paths": [str(file) for file in ordered], "files": [{"size": file.stat().st_size, "mtime_ns": file.stat().st_mtime_ns} for file in ordered]})
        return result

    def _restore_cached_games(self, cancel=None):
        check_cancel(cancel)
        if not self.android.owned or getattr(self.android, "_external", False):
            return
        image = self.android.IMAGE_PACKAGE
        previous = self.memory.get("cached_apk_restore_image", "")
        if previous == image:
            return
        saved = self.memory.get("installed_apks", [])
        saved = [item for item in saved if isinstance(item, dict) and isinstance(item.get("paths"), list)] if isinstance(saved, list) else []
        if not previous:
            previous = saved[-1].get("image", "") if saved else ""
        if not previous or previous == image or not saved:
            self.memory.set("cached_apk_restore_image", image)
            return
        installed = set(self.android.user_packages(cancel, refresh=True))
        with self.lifecycle:
            pending = [dict(item) for item in self._pending_installs]
        queued = {item["restore_package"] for item in pending if item.get("restore_package")}
        for item in pending:
            for value in item.get("paths", [item.get("path")]):
                check_cancel(cancel)
                try:
                    queued.add(apk_package_info(value)["package"])
                except (OSError, TypeError, ValueError, KeyError, zipfile.BadZipFile):
                    continue
        candidates = {}
        for item in reversed(saved):
            check_cancel(cancel)
            excluded = installed | queued | candidates.keys()
            if item.get("package") in excluded:
                continue
            try:
                for group in self._cached_install_groups(item["paths"], cancel, excluded):
                    candidates[group["package"]] = group
            except Cancelled:
                raise
            except (OSError, TypeError, ValueError, KeyError, zipfile.BadZipFile) as exc:
                self.log("cached_game_restore_skipped", package=item.get("package", ""), image=image, error=str(exc))
        with self.lifecycle:
            for package, group in candidates.items():
                self._pending_installs.append({"id": uuid.uuid4().hex, "paths": group["paths"], "source_paths": group["paths"], "files": group["files"], "cached": True, "attempts": 0, "restore_package": package})
        if not self._save_pending_installs():
            raise OSError("新安卓环境的缓存恢复队列尚未保存，将在环境准备时重试")
        self.memory.set("cached_apk_restore_image", image)
        self.log("cached_games_restore_queued", previous_image=previous, image=image, packages=sorted(candidates), installed_skipped=sorted(installed), saved_games_migrated=False)
        if candidates:
            self.status("安卓镜像已切换，正在恢复缓存的游戏安装包；旧环境存档仍保留在原环境")

    def _skip_existing_restore(self, pending, cancel=None):
        package = pending.get("restore_package")
        if not package:
            return False
        if not self.android.owned or getattr(self.android, "_external", False):
            raise ValueError("缓存应用自动恢复仅用于本程序拥有的安卓环境")
        if package not in self.android.user_packages(cancel, refresh=True):
            return False
        with self.lifecycle:
            if self._pending_installs and self._pending_installs[0].get("id") == pending.get("id"):
                self._pending_installs.popleft()
        self._save_pending_installs()
        self.log("cached_game_restore_existing", package=package, image=self.android.IMAGE_PACKAGE, replaced=False)
        return True

    def _prepare_forever(self):
        failures = 0
        while not self.shutdown.is_set():
            if self.ready_event.is_set():
                self.preparation_wake.wait(self.tuning.deadline("prepare"))
                self.preparation_wake.clear()
                continue
            with self.lifecycle:
                reset_android, reset_ai = self._reset_android, self._reset_ai
                self._reset_android = False
                self._reset_ai = False
            try:
                if reset_android:
                    with self.action_lock:
                        try:
                            self.android.release_touches()
                        except Exception as exc:
                            self.log("touch_release_before_recycle_failed", error=str(exc))
                        self.android.force_recycle()
                    self._fast_wake.set()
                if reset_ai:
                    self.ai.cancel_request()
                    with self.model_lock:
                        self.ai.stop()
                self._prepare_stack()
                with self.lifecycle:
                    if self._reset_android or self._reset_ai:
                        continue
                    check_cancel(self.shutdown)
                    if self._pending_installs:
                        continue
                    if not all(self._readiness.values()):
                        raise ComponentFailure("preparation", "截图、输入、决策验证尚未全部通过")
                    self.ready_event.set()
                    if self.ready_seconds is None:
                        self.ready_seconds = time.monotonic() - self._startup_clock
                        self.log("first_ready", seconds=round(self.ready_seconds, CONTROL_DIAGNOSTIC_PRECISION), stages=self._startup_diagnostics())
                failures = 0
                self.events.put(("prepared", True))
                self._update_resources()
                self.status("AI 已恢复，继续控制游戏" if self.desired_running else f"全部就绪 · 本次准备 {self.ready_seconds:.1f} 秒 · 安装或打开游戏后点击启动")
                self._heartbeat("running" if self.desired_running else "ready")
                with self.lifecycle:
                    if self.resume_requested and not self.stopping:
                        self.start(recovery=True)
            except Cancelled:
                if self.shutdown.is_set():
                    break
                self.environment_error = "本地运行环境的一项操作已取消，正在重新检测"
                self.ready_event.clear()
                with self.lifecycle:
                    self._readiness = dict.fromkeys(self._readiness, False)
                self.events.put(("prepare_retry", {"error": self.environment_error, "delay": self.tuning.deadline("prepare"), "attempt": failures}))
                self.shutdown.wait(self.tuning.deadline("prepare"))
            except Exception as exc:
                failures += 1
                self.environment_error = str(exc)
                self.ready_event.clear()
                component = getattr(exc, "component", "preparation")
                if component in {"android", "android_assets"}:
                    self.android_ready = False
                    self._reset_android = component == "android"
                    with self.lifecycle:
                        self._readiness = dict.fromkeys(self._readiness, False)
                if component == "android_assets":
                    self._android_assets = False
                if component == "ai":
                    self._reset_ai = True
                    with self.lifecycle:
                        self._readiness["decision"] = False
                self.log("preparation_retry", component=component, attempt=failures, error=str(exc), traceback=traceback.format_exc())
                delay = self.tuning.retry(component, failures, resource=component == "resources")
                self.events.put(("prepare_retry", {"error": str(exc)[:CONTROL_STATUS_CHARACTERS], "delay": delay, "attempt": failures}))
                self.status("本地环境未就绪 / 自动恢复：" + str(exc)[:CONTROL_STATUS_CHARACTERS] + f" · {delay} 秒后重试")
                self._heartbeat("prepare_retry")
                self.shutdown.wait(delay)

    def _request_recovery(self, component, error, generation=None):
        with self.lifecycle:
            if self.shutdown.is_set():
                return
            if generation is not None and (generation != self.generation or not self.desired_running):
                return
            already_pending = not self.ready_event.is_set()
            self.ready_event.clear()
            if component == "android":
                self._readiness = dict.fromkeys(self._readiness, False)
                self.android_ready = False
                self._reset_android = True
                self._resume_game_after_recovery = bool(self.selected_game_package and (self.desired_running or self.resume_requested))
                self._fast_pointers.clear()
                self._fast_wake.set()
                self.perception.clear()
                with self.frame_lock:
                    self.context = {}
            if component == "ai":
                self._readiness["decision"] = False
                self.ai.note_runtime_failure(error)
                self._reset_ai = True
                if self.android_ready and not self._reset_android:
                    self._fast_pointers.clear()
                    self._fast_update_serial += 1
                    self._fast_wake.set()
                    self.log("game_ai_recovery_release", reason="等待新观测时释放旧触点")
            if not already_pending:
                self.recoveries += 1
        if component == "android":
            self.ai.cancel_request()
        self.log("recovering", component=component, error=str(error), desired_running=self.desired_running)
        self.status("正在自动恢复" + ("安卓连接" if component == "android" else "本地学习器") + "：" + str(error)[:CONTROL_STATUS_CHARACTERS])
        self.preparation_wake.set()

    def operation_state(self):
        with self.lifecycle:
            if self.shutdown.is_set():
                return "CLOSED"
            if self.stopping:
                return "STOPPING"
            if self.desired_running or self.resume_requested:
                return "RUNNING" if self.ready_event.is_set() else "RECOVERING"
            if self.ready_event.is_set():
                return "READY"
            return "BLOCKED" if self.environment_error else "PREPARING"

    def manual_authorized(self):
        with self.lifecycle:
            return bool(self.ready_event.is_set() and self.android_ready and not self.shutdown.is_set() and not self.desired_running and not self.resume_requested and not self.stopping)

    @staticmethod
    def _is_launcher_package(package):
        return package in {"com.google.android.apps.nexuslauncher", "com.android.launcher", "com.android.launcher3", "com.google.android.launcher"} or str(package).startswith("com.android.launcher")

    def _foreground_game(self):
        context = self.android.game_context(self.shutdown, fresh=True)
        package = str(context.get("package", ""))
        if not re.fullmatch(r"[A-Za-z0-9_]+(?:\.[A-Za-z0-9_]+)+", package) or self._is_launcher_package(package) or package in CONTROL_NON_GAME_PACKAGES:
            return ""
        if package not in self.android.user_packages(self.shutdown):
            return ""
        with self.frame_lock:
            self.context = dict(context, context_at=time.monotonic(), nodes=[], nodes_started_at=0.0, nodes_at=0.0)
        return package

    def _select_game_package(self, package, explicit=False):
        if not re.fullmatch(r"[A-Za-z0-9_]+(?:\.[A-Za-z0-9_]+)+", str(package)) or self._is_launcher_package(package):
            return False
        with self.lifecycle:
            if self.shutdown.is_set() or self.desired_running and self.selected_game_package and self.selected_game_package != package:
                return False
            changed = package != self.selected_game_package or package != self.last_game_package
            self.selected_game_package = package
            self.last_game_package = package
        if changed:
            try:
                self.memory.set("selected_game_package", package)
                self.memory.set("last_game_package", package)
            except Exception as exc:
                self.log("game_package_save_error", package=package, error=str(exc))
            self.log("game_target_selected", package=package, explicit=bool(explicit))
        return changed

    def _remember_foreground_package(self, package, cancel=None, known_packages=None, explicit=False):
        if not package or self._is_launcher_package(package):
            return False
        if not re.fullmatch(r"[A-Za-z0-9_]+(?:\.[A-Za-z0-9_]+)+", str(package)):
            return False
        if not explicit:
            saved = self.memory.get("installed_apks", [])
            catalog = {str(item.get("package")) for item in saved if isinstance(item, dict)} if isinstance(saved, list) else set()
            if package not in catalog and package != self.selected_game_package:
                return False
            if self.desired_running and self.selected_game_package and package != self.selected_game_package:
                return False
        installed = known_packages if known_packages is not None else self.android.user_packages(cancel)
        if package not in installed:
            return False
        return self._select_game_package(package, explicit=explicit)

    def _handle_launcher(self, before, generation, cancel):
        if not self._is_launcher_package(before.get("package", "")):
            return False
        now = time.monotonic()
        if now - self._last_launcher_probe < self.tuning.deadline("launcher"):
            self._heartbeat("launcher_monitor")
            cancel.wait(self.tuning.interval("capture"))
            return True
        self._last_launcher_probe = now
        try:
            installed = self.android.user_packages(cancel)
        except Cancelled:
            raise
        except Exception as exc:
            self.log("game_catalog_unavailable", error=str(exc))
            return False
        if self.selected_game_package and self.selected_game_package not in installed:
            with self.lifecycle:
                invalid = self.selected_game_package
                self.selected_game_package = ""
                self.last_game_package = ""
            try:
                self.memory.set("selected_game_package", "")
                self.memory.set("last_game_package", "")
            except Exception as exc:
                self.log("game_selection_clear_failed", package=invalid, error=str(exc))
            self.log("game_selection_uninstalled", package=invalid, action="monitor_for_available_game")
        preferred = self.selected_game_package if self.selected_game_package in installed else ""
        candidates = [preferred] if preferred else sorted(installed)
        candidate = candidates[0] if preferred or len(candidates) == 1 else ""
        if candidate and now >= self._failed_game_launches.get(candidate, 0.0):
            try:
                with self.action_lock:
                    self._authorized(generation, cancel)
                    launched_at = time.monotonic()
                    self.android.launch_package(candidate, cancel)
                    self.tuning.observe("launcher", time.monotonic() - launched_at)
                    self._launch_failures.pop(candidate, None)
                self._remember_foreground_package(candidate, cancel, installed, explicit=True)
                self.completed_steps += 1
                self.input_steps += 1
                self.log("game_auto_launched", package=candidate, input_steps=self.input_steps)
                self.status("AI 已自动打开应用：" + candidate)
                cancel.wait(1.0)
                return True
            except Cancelled:
                raise
            except Exception as exc:
                self._launch_failures[candidate] += 1
                self._failed_game_launches[candidate] = now + self.tuning.retry("launch:" + candidate, self._launch_failures[candidate])
                self.log("game_auto_launch_failed", package=candidate, error=str(exc))
        if not candidate:
            if now - self._last_idle_notice >= self.tuning.deadline("launcher") * self.tuning.capacity:
                self._last_idle_notice = now
                self.status("有多个已安装应用；点击结束后选择游戏再启动" if installed else "AI 正在监测安卓桌面；安装或打开游戏后将自动继续操作")
            self._heartbeat("launcher_monitor")
            cancel.wait(self.tuning.interval("context"))
            return True
        before["summary"] = (before.get("summary", "") + "\nSelected game: " + candidate)[:CONTROL_CONTEXT_CHARACTERS]
        return False

    def _handle_foreign_app(self, before, generation, cancel):
        package = before.get("package", "")
        target = self.selected_game_package
        if not package or not target or package == target or self._is_launcher_package(package):
            return False
        system_flow = package == "android" or package.startswith(("com.android.", "com.google.android.")) and package.rsplit(".", 1)[-1] in {"permissioncontroller", "packageinstaller", "documentsui", "systemui", "settings"}
        if system_flow:
            before["ui_flow"] = {"kind": "system_dialog", "return_package": target}
            return False
        now = time.monotonic()
        if now >= self._failed_game_launches.get(target, 0.0):
            try:
                with self.action_lock:
                    self._authorized(generation, cancel)
                    self.android.launch_package(target, cancel)
                self._launch_failures.pop(target, None)
                self._failed_game_launches.pop(target, None)
                self.log("game_foreground_restored", from_package=package, game=target)
            except Cancelled:
                raise
            except Exception as exc:
                self._launch_failures[target] += 1
                self._failed_game_launches[target] = now + self.tuning.retry("restore:" + target, self._launch_failures[target])
                self.log("game_foreground_restore_failed", from_package=package, game=target, error=str(exc))
        self._heartbeat("restore_game")
        cancel.wait(self.tuning.interval("context"))
        return True

    def start(self, recovery=False):
        with self.lifecycle:
            if self.shutdown.is_set() or self.stopping or not self.ready_event.is_set() or not all(self._readiness.values()) or self._pending_installs:
                return False
            if self.desired_running:
                return True
            recovering_game = self.selected_game_package if recovery and self.resume_requested else ""
        if recovering_game:
            foreground = recovering_game
        else:
            try:
                foreground = self._foreground_game()
            except Cancelled:
                return False
            except Exception as exc:
                self.log("game_selection_probe_failed", error=str(exc))
                self.status("尚未确认已打开的游戏，请等待设备识别完成后再点击启动：" + str(exc)[:CONTROL_STATUS_CHARACTERS])
                return False
            if not foreground:
                self.status("请先在安卓画面中打开已安装的游戏，再点击启动")
                return False
            self._select_game_package(foreground, explicit=True)
        with self.lifecycle:
            if self.shutdown.is_set() or self.stopping or not self.ready_event.is_set() or not all(self._readiness.values()) or self._pending_installs:
                return False
            if self.desired_running:
                return True
            if not self.selected_game_package or self.selected_game_package != foreground:
                self.status("目标游戏已经变化，请打开游戏后重新启动")
                return False
            self.run_latch.allow()
            self.desired_running = True
            self.resume_requested = False
            self.run_started_at = time.monotonic()
            self._episode_id = uuid.uuid4().hex
            self._terminal_seen = None
            self._terminal_candidate = None
            self._unverified_result_reviews = 0
            self.generation += 1
            generation = self.generation
            self._manual_epoch += 1
            self._manual_cancel.set()
            self._manual_frames.clear()
            self._manual_demo_active.clear()
            self._fast_pointers.clear()
            self._fast_generation = generation
            self._fast_wake.set()
            cancel = threading.Event()
            self.run_cancel = cancel
            self._persist_run_intent(True)
            self.worker = threading.Thread(target=self._run, args=(generation, cancel), daemon=True, name="GameAI-" + str(generation))
            self.worker.start()
        self.events.put(("running", True))
        self.status("Agent 已接管本程序游戏视图 · 点击结束恢复手动操作")
        return True

    def _authorized(self, generation, cancel):
        check_cancel(cancel)
        check_cancel(self.shutdown)
        with self.lifecycle:
            if not self.desired_running or self.generation != generation:
                raise Cancelled("接管已结束")

    def stop(self):
        with self.lifecycle:
            if self.stopping or not (self.desired_running or self.resume_requested):
                return
            self.run_latch.stop()
            self.desired_running = False
            self.resume_requested = False
            self.generation += 1
            generation = self.generation
            self._manual_epoch += 1
            self._manual_cancel.set()
            self._fast_pointers.clear()
            self._fast_generation = None
            self._fast_wake.set()
            cancel = self.run_cancel
            worker = self.worker
            if cancel is not None:
                cancel.set()
            self.stopping = True
            self._persist_run_intent(False)
        with self.frame_available:
            self.frame_available.notify_all()
        with self._fast_delivery:
            self._fast_delivery.notify_all()
        self.status("正在取消 AI 操作并释放触点")
        self.log("stop_requested", generation=generation)
        def finish():
            try:
                self.ai.cancel_request()
                for attempt in range(CONTROL_INITIAL_RECOVERY_FAILURES):
                    if self.shutdown.is_set():
                        return
                    if self._complete_stop(generation, worker):
                        return
                    if self.shutdown.wait(self.tuning.interval("input")):
                        return
                with self.lifecycle:
                    if generation == self.generation:
                        self._pending_stop_release = (generation, worker)
                self.status("已取消 AI 操作，正在恢复触控通道以安全交还手动权限")
                self._request_recovery("android", "停止操作后触控通道尚未确认释放")
            except Exception as exc:
                self.log("stop_release_error", generation=generation, error=str(exc))
                with self.lifecycle:
                    if generation == self.generation:
                        self._pending_stop_release = (generation, worker)
                self._request_recovery("android", exc)
        self._job(finish, "ReleaseGameControl")

    def _complete_stop(self, generation, worker):
        with self.lifecycle:
            if generation != self.generation or self.desired_running:
                return False
        if not self.action_lock.acquire(timeout=max(RUNTIME_BOOTSTRAP_CONSOLE_TIMEOUT_SECONDS, self.tuning.deadline("input"))):
            return False
        try:
            with self.lifecycle:
                if generation != self.generation or self.desired_running:
                    return False
            release_failure = None
            if self.android.alive():
                try:
                    self.android.release_touches()
                except Exception as exc:
                    release_failure = exc
                    self.log("touch_release_error", error=str(exc))
            else:
                try:
                    self.android.release_touches()
                except Exception as exc:
                    self.log("offline_touch_release_pending", error=str(exc))
                self._request_recovery("android", "Agent 已停止；设备离线，重新验证触控通道后恢复手动操作")
                return False
            if release_failure is not None:
                self._request_recovery("android", release_failure)
                return False
            if worker is not None and worker.is_alive() and worker is not threading.current_thread():
                worker.join(timeout=self.tuning.interval("input"))
            with self.lifecycle:
                if generation != self.generation or self.desired_running:
                    return False
                self.stopping = False
                self._manual_cancel = threading.Event()
                self._pending_stop_release = None
                self.run_cancel = None
                if worker is not None and worker.is_alive():
                    self._jobs.add(worker)
                self.worker = None
        finally:
            self.action_lock.release()
        self.events.put(("running", False))
        if not self.shutdown.is_set():
            self.status("Agent 已停止 · 本程序游戏视图已恢复手动操作" if self.manual_authorized() else "Agent 已停止 · 设备连接不可用，后台尝试恢复")
        return True

    def _publish_frame(self, png, started_at=None, finished_at=None):
        frame_dimensions(png)
        finished = time.monotonic() if finished_at is None else float(finished_at)
        started = finished if started_at is None else float(started_at)
        if not math.isfinite(started) or not math.isfinite(finished) or started > finished:
            raise ValueError("截图采集时间无效")
        if finished > started:
            self.tuning.observe("capture", finished - started)
        with self.frame_available:
            if started < self.frame_start_time:
                return None
            if png != self.frame:
                self.frame = png
                self.frame_number += 1
            self.frame_start_time = started
            self.frame_time = finished
            self.capture_id += 1
            self.frame_available.notify_all()
            return self.capture_id

    def _snapshot(self, cancel, fresh=False, fresh_nodes=False, fresh_since=None):
        check_cancel(cancel)
        try:
            with self.frame_lock:
                png, started, finished, capture_id = self.frame, self.frame_start_time, self.frame_time, self.capture_id
                context = dict(self.context)
            if fresh_nodes:
                self._heartbeat("observe_nodes")
                requested = time.monotonic()
                before_context = self.android.game_context(cancel, fresh=True)
                node_snapshot = self.android.ui_snapshot(cancel, fresh=True)
                after_context = self.android.game_context(cancel, fresh=True)
                context = dict(after_context)
                context["context_at"] = requested
                if all(before_context.get(key) == after_context.get(key) for key in ("package", "activity")):
                    context.update(node_snapshot)
                else:
                    context.update(nodes=[], nodes_started_at=0.0, nodes_at=0.0)
                self.tuning.observe("accessibility", time.monotonic() - requested)
                with self.frame_lock:
                    if requested >= self.context.get("context_at", 0):
                        self.context = dict(context)
                fresh = True
            if fresh and not fresh_nodes and type(fresh_since) in (int, float) and math.isfinite(fresh_since) and started >= fresh_since and time.monotonic() - finished <= self.tuning.interval("capture", 1 / CONTROL_FRAME_BOOTSTRAP_HZ):
                fresh = False
            if fresh or png is None or time.monotonic() - finished > self.tuning.deadline("capture", 1 / CONTROL_FRAME_BOOTSTRAP_HZ):
                started = time.monotonic()
                png = self.android.screenshot(cancel)
                finished = time.monotonic()
                capture_id = self._publish_frame(png, started, finished)
                if capture_id is None:
                    with self.frame_lock:
                        png, started, finished, capture_id = self.frame, self.frame_start_time, self.frame_time, self.capture_id
            observation = game_observation(png, context, finished)
            observation["capture_started_at"] = started
            observation["capture_finished_at"] = finished
            observation["frame_id"] = capture_id
            observation["latency"] = self.tuning.snapshot()
            observation["perception"] = self.perception.state()
            observation["task_state"] = dict((self.last_plan or {}).get("task_state") or {})
            observation["previous_phase"] = str((self.last_plan or {}).get("phase", "unknown"))
            with self.lifecycle:
                observation["active_touches"] = [self._interpolated_pointer(item, time.monotonic()) for item in self._fast_pointers.values()] if self.desired_running else []
            return observation, png
        except Cancelled:
            raise
        except Exception as exc:
            component = "capture" if self.android.alive() else "android"
            raise ComponentFailure(component, exc) from exc

    def _snapshot_after(self, cancel, submitted_at, before_png=None, max_wait=None, fresh_nodes=False):
        tolerance = max(self.tuning.deadline("capture"), self.tuning.interval("capture") * AI_TERMINAL_CONFIRMATION_FRAMES) if max_wait is None else max(0.0, float(max_wait))
        deadline = max(time.monotonic(), submitted_at) + tolerance
        checked = 0
        first_capture = None
        first_result = None
        while True:
            check_cancel(cancel)
            check_cancel(self.shutdown)
            with self.frame_available:
                captured_after_action = self.frame_start_time >= submitted_at and (first_capture is None or self.frame_start_time > first_capture)
                remaining = deadline - time.monotonic()
                if not captured_after_action and remaining > 0:
                    self.frame_available.wait(min(self.tuning.interval("input"), remaining))
                    continue
            observation, png = self._snapshot(cancel, fresh=not captured_after_action, fresh_nodes=fresh_nodes)
            captured = observation["capture_started_at"]
            if captured < submitted_at or first_capture is not None and captured <= first_capture:
                if time.monotonic() >= deadline:
                    if first_result is not None:
                        return first_result
                    raise ComponentFailure("capture", "动作后独立截图尚未产生")
                continue
            checked += 1
            observation["post_action_frames"] = checked
            if before_png is None or png != before_png:
                return observation, png
            observation["post_action_visual_pending"] = True
            if checked >= AI_TERMINAL_CONFIRMATION_FRAMES or time.monotonic() >= deadline:
                return observation, png
            first_capture = captured
            first_result = (observation, png)
            interval = min(self.tuning.interval("capture"), max(0.0, deadline - time.monotonic()))
            if interval:
                cancel.wait(interval)

    def _frames(self):
        failures = 0
        while not self.shutdown.is_set():
            if not self.android_ready:
                self.shutdown.wait(self.tuning.interval("capture", 1 / CONTROL_FRAME_BOOTSTRAP_HZ))
                continue
            started = time.monotonic()
            try:
                png = self.android.screenshot(self.shutdown)
                captured = time.monotonic()
                self._publish_frame(png, started, captured)
                if self.desired_running:
                    self.perception.update(png, captured, self.tuning.interval("perception", self.tuning.estimate("capture")))
                    self.tuning.observe("perception", time.monotonic() - captured)
                self.capture_seconds = captured - started
                if not self.desired_running and self.ready_event.is_set() and captured - self._last_passive_analysis >= self.tuning.deadline("context"):
                    self._last_passive_analysis = captured
                    with self.frame_lock:
                        preview_context = dict(self.context)
                    try:
                        identity = (preview_context.get("package"), frame_dimensions(png))
                        previous_samples = self._passive_samples if self._passive_identity == identity else None
                        preview = local_agent_passive_scene(png, preview_context, previous_samples)
                        self._passive_samples = preview.pop("samples")
                        self._passive_identity = identity
                        self.events.put(("scene", preview))
                    except Exception as exc:
                        self.log("passive_scene_error", error=str(exc))
                elif self.desired_running:
                    self._passive_samples = None
                    self._passive_identity = None
                failures = 0
            except Cancelled:
                break
            except Exception as exc:
                failures += 1
                self.log("capture_error", count=failures, error=str(exc))
                if failures >= CONTROL_INITIAL_RECOVERY_FAILURES:
                    self._request_recovery("android", exc)
                    failures = 0
            elapsed = time.monotonic() - started
            interval = self.tuning.interval("capture", 1 / CONTROL_FRAME_BOOTSTRAP_HZ)
            if self.desired_running:
                motion = self.perception.state()
                magnitude = float(motion.get("motion") or 0)
                threshold = float(motion.get("adaptive_drift") or CONTROL_INITIAL_MOTION_DRIFT)
                interval = max(elapsed, interval / (1 + magnitude / max(sys.float_info.epsilon, threshold)))
            elif not self.ui_visible:
                interval = max(interval, self.tuning.deadline("context"))
            else:
                interval = max(interval, float(getattr(self, "ui_frame_interval", 0)))
            self.shutdown.wait(max(self.tuning.clock_floor, interval - elapsed))

    def _contexts(self):
        next_accessibility = 0.0
        while not self.shutdown.is_set():
            started = time.monotonic()
            if self.android_ready:
                try:
                    context = self.android.game_context(self.shutdown)
                    context["context_at"] = started
                    self.tuning.observe("context", time.monotonic() - started)
                    if isinstance(context, dict):
                        with self.frame_lock:
                            previous = dict(self.context)
                        same_app = all(previous.get(key) == context.get(key) for key in ("package", "activity"))
                        now = time.monotonic()
                        previous_nodes_at = float(previous.get("nodes_at", 0.0)) if same_app else 0.0
                        node_age_limit = self.tuning.deadline("accessibility") + self.tuning.interval("context")
                        valid_nodes = same_app and now - previous_nodes_at <= node_age_limit
                        context["nodes"] = previous.get("nodes", []) if valid_nodes else []
                        context["nodes_at"] = previous_nodes_at if valid_nodes else 0.0
                        context["nodes_started_at"] = previous.get("nodes_started_at", 0.0) if valid_nodes else 0.0
                        if not same_app:
                            next_accessibility = 0.0
                        if now >= next_accessibility:
                            queried = time.monotonic()
                            try:
                                context.update(self.android.ui_snapshot(self.shutdown))
                                verified_context = self.android.game_context(self.shutdown, fresh=True)
                                if any(context.get(key) != verified_context.get(key) for key in ("package", "activity")):
                                    context = dict(verified_context)
                                    context.update(nodes=[], nodes_started_at=0.0, nodes_at=0.0)
                                    context["context_at"] = time.monotonic()
                                    same_app = False
                            except Cancelled:
                                raise
                            except Exception as exc:
                                self.log("accessibility_unavailable", error=str(exc))
                            finally:
                                self.tuning.observe("accessibility", time.monotonic() - queried)
                                next_accessibility = time.monotonic() + self.tuning.interval("accessibility")
                        with self.frame_lock:
                            if started >= self.context.get("context_at", 0):
                                self.context = context
                        if context.get("package") and context.get("package") != self.last_game_package:
                            try:
                                self._remember_foreground_package(context["package"], self.shutdown)
                            except Cancelled:
                                raise
                            except Exception as exc:
                                self.log("game_foreground_check_error", error=str(exc))
                        if not same_app and previous.get("package") and context.get("package"):
                            with self.lifecycle:
                                if self.desired_running and self._fast_pointers:
                                    self._fast_pointers.clear()
                                    self._fast_update_serial += 1
                                    self._fast_wake.set()
                                    self.log("game_foreground_changed", previous=previous["package"], current=context["package"])
                except Cancelled:
                    return
                except Exception as exc:
                    self.log("context_unavailable", error=str(exc))
            period = max(self.tuning.interval("context"), self.tuning.deadline("capture"))
            self.shutdown.wait(max(self.tuning.clock_floor, period - (time.monotonic() - started)))

    @staticmethod
    def _interpolated_pointer(item, now):
        start, finish = item["start_at"], item["finish_at"]
        ratio = 1.0 if finish <= start else min(1.0, max(0.0, (now - start) / (finish - start)))
        return {"id": item["id"], "x": round(item["x"] + (item["x2"] - item["x"]) * ratio), "y": round(item["y"] + (item["y2"] - item["y"]) * ratio)}

    def _update_fast_control(self, action, generation):
        now = time.monotonic()
        with self.lifecycle:
            if generation != self.generation or not self.desired_running:
                raise Cancelled("接管已结束")
            updated = dict(self._fast_pointers)
            kind = action["kind"]
            if kind in {"touch_begin", "touch_update"}:
                for point in action["pointers"]:
                    identifier = point["id"]
                    previous = updated.get(identifier)
                    start = self._interpolated_pointer(previous, now) if previous and kind == "touch_update" else point
                    duration = max(0.0, float(action.get("ms", 0)) / CONTROL_MILLISECONDS_PER_SECOND)
                    updated[identifier] = {"id": identifier, "x": start["x"], "y": start["y"], "x2": point["x2"], "y2": point["y2"], "start_at": now, "finish_at": now + duration}
            elif kind == "touch_end":
                ids = action.get("ids") or list(updated)
                for identifier in ids:
                    updated.pop(identifier, None)
            elif kind == "touch_release_all":
                updated.clear()
            else:
                raise ValueError("快速控制层收到不支持的动作")
            capacity = self.android.capabilities()
            maximum = int(capacity.get("continuous_touch_slots", capacity.get("touch_slots", 0)))
            if maximum <= 0 and updated:
                raise ValueError("当前设备不支持持续多触点输入；请使用已报告的点击/滑动能力")
            if len(updated) > maximum:
                raise ValueError("设备可同时控制的触点数不足")
            self._fast_pointers = updated
            self._fast_generation = generation
            self._fast_update_serial += 1
            serial = self._fast_update_serial
            self._fast_wake.set()
            return {"submitted": True, "kind": kind, "pointers": len(updated), "serial": serial}

    def _await_fast_control(self, serial, generation, cancel, timeout=None):
        duration = max(RUNTIME_BOOTSTRAP_CONSOLE_TIMEOUT_SECONDS, self.tuning.deadline("input")) if timeout is None else float(timeout)
        deadline = time.monotonic() + duration
        with self._fast_delivery:
            while True:
                self._authorized(generation, cancel)
                if self._fast_rejected_serial >= serial:
                    raise GeometryPending(self._fast_rejected_reason)
                if self._fast_applied_serial >= serial:
                    return
                if not self.android_ready or self._reset_android:
                    raise ComponentFailure("android", "实时触控通道正在恢复")
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    raise ComponentFailure("android", "实时触控动作未得到模拟器确认")
                self._fast_delivery.wait(min(self.tuning.interval("input"), remaining))

    def _fast_loop(self):
        last_sent = ()
        last_confirmed = 0.0
        while not self.shutdown.is_set():
            self._fast_wake.clear()
            now = time.monotonic()
            with self.lifecycle:
                authorized = self.desired_running and not self.stopping and self.android_ready and not self._reset_android and self._fast_generation == self.generation
                current = [dict(item) for item in self._fast_pointers.values()] if authorized else []
                generation = self.generation
                cancel = self.run_cancel
                serial = self._fast_update_serial
                pending = serial > self._fast_applied_serial
            points = [self._interpolated_pointer(item, now) for item in current]
            frame = tuple(sorted((item["id"], item["x"], item["y"]) for item in points))
            moving = any(now < item["finish_at"] and (item["x"], item["y"]) != (item["x2"], item["y2"]) for item in current)
            refresh = bool(current) and now - last_confirmed >= self.tuning.deadline("capture") + self.tuning.deadline("input")
            if authorized and (frame != last_sent or pending or refresh):
                try:
                    with self.action_lock:
                        self._authorized(generation, cancel)
                        if self.android_ready and not self._reset_android:
                            input_started = time.monotonic()
                            self.android.touch_frame(points, cancel)
                            self.tuning.observe("input", time.monotonic() - input_started)
                            last_sent = frame
                            last_confirmed = time.monotonic()
                            with self._fast_delivery:
                                if self.generation == generation and self.desired_running:
                                    self._fast_applied_serial = max(self._fast_applied_serial, serial)
                                    self._fast_delivery.notify_all()
                except Cancelled:
                    last_sent = ()
                except GeometryPending as exc:
                    last_sent = ()
                    with self._fast_delivery:
                        if self.generation == generation:
                            self._fast_rejected_serial = max(self._fast_rejected_serial, serial)
                            self._fast_rejected_reason = str(exc)
                            self._fast_pointers.clear()
                            self._fast_update_serial += 1
                            self._fast_delivery.notify_all()
                            self._fast_wake.set()
                    self.log("fast_touch_geometry_changed", error=str(exc), serial=serial)
                except Exception as exc:
                    last_sent = ()
                    self.log("fast_touch_failed", error=str(exc))
                    self._request_recovery("android", exc, generation)
            elif not authorized:
                last_sent = ()
            period = self.android.input_interval() if moving else self.tuning.interval("input") if current else self.tuning.deadline("capture")
            self._fast_wake.wait(max(self.tuning.clock_floor, period))

    def _record_result(self, history, plan, package, observation):
        signal = plan.get("reward_signal", {})
        if not isinstance(signal, dict):
            return True
        outcome = signal.get("outcome", "unknown")
        candidate = (package, outcome)
        frames = signal.get("confirmation_frames", ())
        confirmed = outcome in {"win", "loss"} and plan.get("phase") == "result" and str(signal.get("evidence", "")).strip() and plan.get("outcome_verified") is True and signal.get("verified") is True and isinstance(frames, (list, tuple)) and len(frames) >= AI_TERMINAL_CONFIRMATION_FRAMES and all(type(item) is int and item > 0 for item in frames) and len(set(frames)) == len(frames)
        if confirmed and self._terminal_seen != candidate:
            episodes = [entry for entry in history if entry.get("package") == package and entry.get("episode_id") == self._episode_id]
            try:
                self._heartbeat("storage")
                self.memory.credit(episodes, dict(signal, verified=True), episode_id=self._episode_id)
            except Exception as exc:
                self.log("experience_write_error", error=str(exc))
            self._terminal_seen = candidate
            self._terminal_candidate = None
            self._unverified_result_reviews = 0
            history.clear()
            self._episode_id = uuid.uuid4().hex
        elif not confirmed and plan.get("phase") == "result":
            marker = (package, "result")
            if self._terminal_candidate != marker:
                self._terminal_candidate = marker
                self._unverified_result_reviews = 0
            self._unverified_result_reviews += 1
            if self._unverified_result_reviews < AI_TERMINAL_CONFIRMATION_FRAMES:
                return False
            if self._unverified_result_reviews == AI_TERMINAL_CONFIRMATION_FRAMES:
                self.log("game_result_unverified_continuing", package=package, reviews=self._unverified_result_reviews, evidence=str(signal.get("evidence", "")), verified=False)
        elif plan.get("phase") != "result":
            if plan.get("phase") in {"playing", "menu"}:
                self._terminal_seen = None
            self._terminal_candidate = None
            self._unverified_result_reviews = 0
        return True

    def _plan_current_frame(self, observation, png, history, generation, cancel):
        self._heartbeat("plan")
        started = time.monotonic()
        with self.model_lock:
            self._authorized(generation, cancel)
            plan = self.ai.plan(observation, png, history, cancel)
        self._authorized(generation, cancel)
        self.plan_seconds = time.monotonic() - started
        self.tuning.observe("plan", self.plan_seconds)
        self.ai_decisions += 1
        if not isinstance(plan, dict) or not isinstance(plan.get("actions"), list) or not plan["actions"]:
            raise ValueError("本地策略没有返回可执行的游戏动作")
        conditions = plan.get("preconditions", [])
        if not isinstance(conditions, list) or any(not isinstance(condition, dict) for condition in conditions):
            raise ValueError("动作前提必须是条件列表")
        actions = [normalize_action(action, observation) for action in plan["actions"]]
        requires_nodes = any(condition.get("kind") in {"node_ref", "node_enabled", "node_state", "visible_text"} for condition in conditions)
        return plan, actions, requires_nodes, started

    def _run(self, generation, cancel):
        history = collections.deque(maxlen=CONTROL_HISTORY_CAPACITY)
        invalid_plans = 0
        stale_plans = 0
        idle_repeats = 0
        decision_error = ""
        capture_failures = 0
        try:
            with self.action_lock:
                self._authorized(generation, cancel)
                if self.ready_event.is_set():
                    with self.lifecycle:
                        has_ongoing_touches = bool(self._fast_pointers) and self._fast_generation == generation
                    if not has_ongoing_touches:
                        self.android.release_touches(cancel)
            while True:
                self._authorized(generation, cancel)
                if not self.ready_event.is_set():
                    cancel.wait(self.tuning.interval("input"))
                    continue
                try:
                    self._heartbeat("observe")
                    before, png = self._snapshot(cancel, fresh=stale_plans > 0 or self._terminal_candidate is not None)
                    before["control_feedback"] = {"stale_rejections": stale_plans, "invalid_plans": invalid_plans, "planning_seconds": self.plan_seconds, "capture_seconds": self.capture_seconds}
                    if decision_error:
                        before["summary"] += "\nPrevious proposed decision was rejected: " + decision_error
                    package = before.get("package", "")
                    previous_package = (self.last_observation or {}).get("package", "")
                    if package and previous_package and package != previous_package:
                        history.clear()
                        self.last_plan = None
                        self.last_observation = None
                        self._terminal_candidate = None
                        self._unverified_result_reviews = 0
                        self._terminal_seen = None
                        self._episode_id = uuid.uuid4().hex
                        self.perception.clear()
                        self.log("game_context_reset", previous=previous_package, current=package)
                    if self._handle_launcher(before, generation, cancel):
                        idle_repeats = 0
                        continue
                    if self._handle_foreign_app(before, generation, cancel):
                        idle_repeats = 0
                        continue
                    if package and package != self.last_game_package:
                        try:
                            self._remember_foreground_package(package, cancel)
                        except Cancelled:
                            raise
                        except Exception as exc:
                            self.log("game_foreground_check_error", error=str(exc))
                    before["previous_phase"] = (self.last_plan or {}).get("phase", "unknown")
                    old_features = scene_features(self.last_plan or {}, before)
                    try:
                        recalled = self.memory.recall(package, old_features)
                    except Exception as exc:
                        recalled = []
                        self.log("experience_read_error", error=str(exc))
                    visible_history = [{key: value for key, value in item.items() if key not in {"observation", "png"}} for item in history]
                    if recalled:
                        visible_history.append({"prior_strategies": recalled})
                    before["experience"] = summarize_recalled_experience(recalled)
                    plan, actions, requires_nodes, started = self._plan_current_frame(before, png, visible_history, generation, cancel)
                    invalid_plans = 0
                    decision_error = ""
                    self._heartbeat("observe")
                    current, current_png = self._snapshot(cancel, fresh=True, fresh_nodes=requires_nodes or plan.get("phase") == "result", fresh_since=started)
                    if current["size"] != before["size"] or (before["package"] and current["package"] and before["package"] != current["package"]):
                        self.log("plan_environment_changed", before=before["size"], after=current["size"], package=current["package"])
                        continue
                    if not self.ai._preconditions_hold(plan.get("preconditions", []), current):
                        decision_error = "动作前提已发生变化，请基于当前画面重新判断"
                        self.log("plan_precondition_changed", decision_id=plan.get("decision_id"), package=current.get("package"))
                        continue
                    refreshed_node = False
                    if actions:
                        actions[0], refreshed_node = rebind_semantic_action(actions[0], plan.get("preconditions", []), current)
                    age = max(0.0, time.monotonic() - before["timestamp"])
                    initial_sample = visual_samples(png)
                    current_sample = initial_sample if png == current_png else visual_samples(current_png)
                    drift = visual_difference(initial_sample, current_sample)
                    stale = decision_is_stale(age, drift, png, current_png, plan.get("phase", "unknown"), perception=self.perception.state(), actions=actions)
                    if stale and refreshed_node and before.get("activity") == current.get("activity") and before.get("package") == current.get("package"):
                        stale = False
                    replanned = False
                    replan_valid_until = None
                    if stale:
                        stale_plans += 1
                        self.stale_rejections += 1
                        self.log("stale_decision_rejected", age_seconds=round(age, CONTROL_DIAGNOSTIC_PRECISION), visual_drift=drift, attempt=stale_plans, phase=plan.get("phase"))
                        discarded_frame = before.get("frame_id")
                        feedback = dict(before.get("control_feedback", {}), stale_rejections=stale_plans)
                        experience = before.get("experience", "")
                        before, png = dict(current), current_png
                        before.update(control_feedback=feedback, experience=experience)
                        plan, actions, requires_nodes, started = self._plan_current_frame(before, png, visible_history, generation, cancel)
                        current, current_png = before, png
                        refreshed_node = False
                        if requires_nodes or plan.get("phase") == "result":
                            self._heartbeat("observe_nodes")
                            current, current_png = self._snapshot(cancel, fresh=True, fresh_nodes=True, fresh_since=started)
                            if any(current.get(key) != before.get(key) for key in ("size", "package", "activity")) or not GameAI._nodes_fresh(current, started):
                                decision_error = "重规划后的界面证据尚未通过时序与环境检查"
                                self.log("replanned_observation_unverified", planned_frame=before.get("frame_id"), observed_frame=current.get("frame_id"))
                                continue
                        if not self.ai._preconditions_hold(plan.get("preconditions", []), current):
                            decision_error = "最新决策的动作前提已经变化"
                            self.log("replanned_precondition_changed", planned_frame=before.get("frame_id"))
                            continue
                        actions[0], refreshed_node = rebind_semantic_action(actions[0], plan.get("preconditions", []), current)
                        age = max(0.0, time.monotonic() - before["timestamp"])
                        initial_sample = visual_samples(png)
                        current_sample = initial_sample if png == current_png else visual_samples(current_png)
                        drift = visual_difference(initial_sample, current_sample)
                        if not refreshed_node and decision_is_stale(age, drift, png, current_png, plan.get("phase", "unknown"), perception=self.perception.state(), actions=actions):
                            decision_error = "新节点证据与动作所用画面仍不一致"
                            self.log("replanned_frame_unverified", planned_frame=before.get("frame_id"), observed_frame=current.get("frame_id"))
                            continue
                        cadence = max(GameAI._cadence(current), current.get("capture_finished_at", current["timestamp"]) - current.get("capture_started_at", current["timestamp"]))
                        replan_valid_until = current["timestamp"] + self.tuning.deadline("plan", self.plan_seconds) + self.tuning.deadline("input", cadence)
                        plan["replanned_from_frame"] = before.get("frame_id")
                        replanned = True
                        self.log("dynamic_plan_refreshed", discarded_frame=discarded_frame, planned_frame=before.get("frame_id"), verified_frame=current.get("frame_id"), seconds=self.plan_seconds)
                    realtime = self.perception.state()
                    motion = realtime.get("motion")
                    motion_limit = float(realtime.get("adaptive_drift") or CONTROL_INITIAL_MOTION_DRIFT)
                    dynamic = replanned or plan.get("phase") == "playing" and age > self.tuning.deadline("capture") and (drift is not None and drift >= motion_limit or motion is not None and motion >= motion_limit)
                    if dynamic:
                        actions = actions[:1]
                        self.log("dynamic_decision_first_action", age_seconds=round(age, CONTROL_DIAGNOSTIC_PRECISION), visual_drift=drift, current_motion=motion)
                    execution_capacity = 1 if dynamic else plan.get("execution_capacity", len(actions))
                    actions = expand_game_actions(actions, plan.get("phase"), float(plan.get("confidence", 0)), limit=execution_capacity)
                    stale_plans = 0
                    if plan.get("phase") == "result":
                        try:
                            self._heartbeat("judge_result")
                            with self.model_lock:
                                self._authorized(generation, cancel)
                                inspected = self.ai.inspect_outcome(current_png, cancel, observation=current)
                            prior = plan.get("reward_signal", {})
                            previous_outcome = prior.get("outcome") if isinstance(prior, dict) else None
                            if previous_outcome in {"win", "loss"} and inspected["outcome"] != previous_outcome:
                                self.log("game_outcome_disagreement", reported=previous_outcome, observed=inspected["outcome"])
                                inspected = {"outcome": "unknown", "score": None, "health": None, "evidence": ""}
                            plan["reward_signal"] = inspected
                            plan["outcome_verified"] = inspected["outcome"] in {"win", "loss"} and bool(inspected["evidence"])
                        except Cancelled:
                            raise
                        except Exception as exc:
                            self.log("game_outcome_inspection_error", error=str(exc))
                            plan["reward_signal"] = {"outcome": "unknown", "score": None, "health": None, "evidence": ""}
                            plan["outcome_verified"] = False
                    plan["decision_id"] = uuid.uuid4().hex
                    plan["realtime_motion"] = realtime
                    self.last_plan = plan
                    self.last_observation = before
                    self.events.put(("plan", {"game": plan.get("game", ""), "phase": plan.get("phase", ""), "assessment": plan.get("assessment", ""), "expected": plan.get("expected", ""), "confidence": plan.get("confidence", 0), "confidence_kind": plan.get("confidence_kind", "样本支持度"), "seconds": self.plan_seconds, "actions": [stored_action(action) for action in actions], "task_state": plan.get("task_state", {}), "selection": plan.get("policy_evidence", {}), "game_profile": plan.get("game_profile", {}), "adaptive": self.tuning.snapshot(), "scene_graph": plan.get("scene_graph", []), "screen_size": plan.get("screen_size", []), "planned_frame": before.get("frame_id")}))
                    if plan.get("phase") in {"menu", "loading", "result"}:
                        with self.lifecycle:
                            release_needed = bool(self._fast_pointers)
                        if release_needed:
                            with self.action_lock:
                                self._authorized(generation, cancel)
                                release = self._update_fast_control({"kind": "touch_release_all"}, generation)
                            self._await_fast_control(release["serial"], generation, cancel)
                    if not self._record_result(history, plan, package, current):
                        self._heartbeat("confirm_result")
                        continue
                    features = scene_features(plan, before)
                    scene = features["game"] + "/" + features["phase"] + "/" + features["situation"]
                    self.log("game_plan", decision_id=plan["decision_id"], game=plan.get("game"), phase=plan.get("phase"), assessment=plan.get("assessment"), expected=plan.get("expected"), confidence=plan.get("confidence"), signal=plan.get("reward_signal"), actions=[stored_action(action) for action in actions], seconds=round(self.plan_seconds, CONTROL_DIAGNOSTIC_PRECISION), age_seconds=round(age, CONTROL_DIAGNOSTIC_PRECISION), screen_drift=drift)
                    observed_after_state = None
                    last_action_sample = current_sample
                    for index, action in enumerate(actions):
                        self._authorized(generation, cancel)
                        if not self.ready_event.is_set():
                            break
                        observed, observed_png = (dict(current), current_png) if replanned and index == 0 else self._snapshot(cancel, fresh_nodes=requires_nodes)
                        if observed["size"] != before["size"] or (package and observed["package"] and package != observed["package"]):
                            break
                        if not self.ai._preconditions_hold(plan.get("preconditions", []), observed):
                            decision_error = "动作序列的前提不再满足，剩余动作已经撤销"
                            self.scene_interruptions += 1
                            self.log("action_precondition_changed", decision_id=plan["decision_id"], index=index)
                            break
                        action, rebound = rebind_semantic_action(action, plan.get("preconditions", []), observed)
                        if rebound:
                            actions[index] = action
                            policy = plan.get("local_policy")
                            if isinstance(policy, dict):
                                policy["signature"] = AI_action_identity(relative_action(action, observed["size"]))
                        if (plan.get("phase") != "playing" and not rebound) or index > 0:
                            reference_sample = current_sample if plan.get("phase") != "playing" else last_action_sample
                            action_drift = visual_difference(reference_sample, visual_samples(observed_png))
                            if action_drift is not None and action_drift > self.tuning.scene_threshold("scene_drift:" + package):
                                self.scene_interruptions += 1
                                self.log("action_interrupted_by_scene_change", decision_id=plan["decision_id"], index=index, drift=action_drift)
                                break
                        self._heartbeat("act")
                        action_id = uuid.uuid4().hex
                        sent = time.monotonic()
                        with self.action_lock:
                            self._authorized(generation, cancel)
                            if not self.ready_event.is_set():
                                break
                            if replan_valid_until is not None and time.monotonic() > replan_valid_until:
                                self.log("replanned_delivery_expired", planned_frame=before.get("frame_id"), age_seconds=time.monotonic() - current["timestamp"])
                                break
                            if tuple(self.android.screen_size()) != tuple(observed["size"]):
                                self.log("action_geometry_changed", decision_id=plan["decision_id"])
                                break
                            with self.frame_lock:
                                delivery_context = dict(self.context)
                            delivery = dict(observed)
                            if delivery_context.get("context_at", 0) > observed.get("capture_started_at", observed["timestamp"]):
                                for key in ("package", "activity"):
                                    if key in delivery_context:
                                        delivery[key] = delivery_context[key]
                                if delivery_context.get("nodes_at", 0) > observed.get("nodes_at", 0):
                                    delivery.update({key: delivery_context.get(key, [] if key == "nodes" else 0.0) for key in ("nodes", "nodes_started_at", "nodes_at")})
                            with self.lifecycle:
                                delivery["active_touches"] = [self._interpolated_pointer(item, time.monotonic()) for item in self._fast_pointers.values()]
                            if any(delivery.get(key) != observed.get(key) for key in ("package", "activity")) or not self.ai._preconditions_hold(plan.get("preconditions", []), delivery):
                                self.scene_interruptions += 1
                                self.log("delivery_precondition_changed", decision_id=plan["decision_id"], planned_frame=before.get("frame_id"))
                                break
                            action, rebound = rebind_semantic_action(action, plan.get("preconditions", []), delivery)
                            if rebound:
                                actions[index] = action
                                policy = plan.get("local_policy")
                                if isinstance(policy, dict):
                                    policy["signature"] = AI_action_identity(relative_action(action, delivery["size"]))
                            observed = delivery
                            self._authorized(generation, cancel)
                            if action["kind"] in {"touch_begin", "touch_update", "touch_end", "touch_release_all"}:
                                submitted = self._update_fast_control(action, generation)
                            else:
                                if action["kind"] in {"back", "home", "recents", "enter", "keyevent", "type"}:
                                    self._update_fast_control({"kind": "touch_release_all"}, generation)
                                expected_ms = action.get("ms", 0)
                                with self.progress_lock:
                                    self._active_action_until = time.monotonic() + max(0.0, float(expected_ms) / CONTROL_MILLISECONDS_PER_SECOND)
                                try:
                                    try:
                                        submitted = self.android.act(action, cancel)
                                    except Cancelled:
                                        raise
                                    except GeometryPending:
                                        raise
                                    except Exception as exc:
                                        raise ComponentFailure("android", exc) from exc
                                finally:
                                    with self.progress_lock:
                                        self._active_action_until = 0.0
                        self._authorized(generation, cancel)
                        if action["kind"] in {"touch_begin", "touch_update", "touch_end", "touch_release_all"}:
                            self._await_fast_control(submitted["serial"], generation, cancel)
                            submitted["applied"] = True
                        self.completed_steps += 1
                        if action["kind"] == "wait":
                            self.wait_steps += 1
                        elif submitted.get("submitted") and submitted.get("applied", True) and action["kind"] != "touch_release_all":
                            self.input_steps += 1
                        applied_at = time.monotonic()
                        if action["kind"] != "wait":
                            self.tuning.observe("input", applied_at - sent)
                        self._heartbeat("observe_after")
                        after, after_png = self._snapshot_after(cancel, applied_at, before_png=observed_png, fresh_nodes=bool(observed.get("nodes")))
                        observed_after_state = (after.get("package"), after.get("state"))
                        after_sample = visual_samples(after_png)
                        change = 0.0 if observed_png == after_png else visual_difference(visual_samples(observed_png), after_sample)
                        last_action_sample = after_sample
                        if change is not None and plan.get("phase") == "playing":
                            self.tuning.observe("scene_drift:" + package, change)
                        result = {"action_id": action_id, "decision_id": plan["decision_id"], "before_state": observed.get("state"), "after_state": after.get("state"), "before_captured_at": observed["timestamp"], "after_captured_at": after["timestamp"], "before_capture_started_at": observed["capture_started_at"], "after_capture_started_at": after["capture_started_at"], "after_frame_id": after["frame_id"], "action_applied_at": applied_at, "command_submitted": bool(submitted.get("submitted")), "action_applied": bool(submitted.get("applied", submitted.get("submitted"))), "visual_difference": change, "post_action_visual_pending": bool(after.get("post_action_visual_pending")), "post_action_frames": after.get("post_action_frames", 1), "expected": plan.get("expected", ""), "outcome": "unverified", "seconds": round(time.monotonic() - sent, CONTROL_DIAGNOSTIC_PRECISION), "plan_age_seconds": round(sent - before["timestamp"], CONTROL_DIAGNOSTIC_PRECISION), "size": list(before["size"]), "features": features, "expected_effect": dict(plan.get("expected_effect") or {}) if index == 0 else {}, "before_node_states": {AI_node_reference(node): {"selected": node.get("selected") is True, "enabled": node.get("enabled", True) is True, "checked": node.get("checked") is True, "focused": node.get("focused") is True} for node in observed.get("nodes", []) if isinstance(node, dict)}}
                        try:
                            learned = self.ai.observe_transition(observed, after, action, result, plan, before_png=observed_png, after_png=after_png)
                            if isinstance(learned, dict):
                                self.events.put(("learning", learned))
                        except Exception as exc:
                            self.log("local_learning_error", error=str(exc), traceback=traceback.format_exc())
                        episode = {"action_id": action_id, "episode_id": self._episode_id, "package": package, "scene": scene, "features": features, "size": before["size"], "action": stored_action(action), "result": result, "expected": plan.get("expected", "")}
                        if action["kind"] not in {"wait", "touch_release_all"} and package:
                            history.append(episode)
                            try:
                                episode["transition_id"] = self.memory.record(package, scene, observed, action, result, episode_id=self._episode_id)
                            except Exception as exc:
                                self.log("experience_write_error", error=str(exc))
                            if episode.get("transition_id") is not None:
                                try:
                                    effect = observed_action_effect(episode, after)
                                    confirmation = None
                                    if effect is None and result["expected_effect"].get("kind") == "node_state" and GameAI._nodes_fresh(after, applied_at):
                                        self._authorized(generation, cancel)
                                        confirmation, _ = self._snapshot(cancel, fresh=True, fresh_nodes=True)
                                        effect = observed_action_effect(episode, after, confirmation)
                                    if effect is not None and self.memory.feedback(episode, effect, float(plan.get("confidence", 0)), observation=after, confirmation=confirmation):
                                        self.log("action_feedback_learned", fulfilled=effect["fulfilled"], source=effect["source"], evidence=effect["evidence"][:CONTROL_STATUS_CHARACTERS])
                                        self.events.put(("feedback", {"verified": True, "source": "两次独立界面状态未变化" if not effect["fulfilled"] else "界面节点状态变化", "fulfilled": effect["fulfilled"], "evidence": effect["evidence"], "action_id": action_id}))
                                except Cancelled:
                                    raise
                                except Exception as exc:
                                    self.log("feedback_write_error", error=str(exc))
                        self.log("action_executed", number=self.completed_steps, input_steps=self.input_steps, action=stored_action(action), result=result)
                        now = time.monotonic()
                        if index == 0 and (plan.get("phase") != "playing" or now - self._last_capture_saved >= self.tuning.deadline("plan")):
                            self._save_capture(before, png, plan)
                            self._last_capture_saved = now
                        if action["kind"] in {"back", "home", "recents", "type"} or (index < len(actions) - 1 and change is not None and change > self.tuning.scene_threshold("scene_drift:" + package)):
                            break
                    capture_failures = 0
                    self._heartbeat("running")
                    self.events.put(("stats", {"actions": self.input_steps, "decisions": self.ai_decisions, "waits": self.wait_steps, "plan_seconds": self.plan_seconds, "game": str(plan.get("game", "")), "phase": str(plan.get("phase", "")), "motion": realtime.get("motion"), "adaptive": self.tuning.snapshot(), "actions_per_minute": round(self.input_steps * CONTROL_SECONDS_PER_MINUTE / max(1.0, time.monotonic() - self.run_started_at), 1) if self.run_started_at else 0.0}))
                    if len(actions) == 1 and actions[0]["kind"] == "wait" and observed_after_state == (before.get("package"), before.get("state")):
                        idle_repeats += 1
                        self._heartbeat("idle")
                        deadline = time.monotonic() + min(self.tuning.retry("idle:" + package, idle_repeats), self.tuning.deadline("capture") + self.tuning.deadline("plan"))
                        with self.frame_available:
                            last_number = self.frame_number
                        while True:
                            self._authorized(generation, cancel)
                            with self.frame_available:
                                if self.frame_number != last_number:
                                    break
                                remaining = deadline - time.monotonic()
                                if remaining <= 0:
                                    break
                                self.frame_available.wait(min(self.tuning.interval("input"), remaining))
                    else:
                        idle_repeats = 0
                except Cancelled:
                    raise
                except GeometryPending as exc:
                    self._authorized(generation, cancel)
                    stale_plans += 1
                    with self.lifecycle:
                        self._fast_pointers.clear()
                        self._fast_update_serial += 1
                        self._fast_wake.set()
                    self.log("game_geometry_transition", error=str(exc))
                    self.status("游戏画面方向正在变化，正在重新获取坐标")
                    cancel.wait(self.tuning.interval("capture"))
                except (ValueError, TypeError, KeyError, OverflowError) as exc:
                    self._authorized(generation, cancel)
                    with self.progress_lock:
                        error_phase = self.progress_phase
                    if error_phase.startswith("observe"):
                        self._request_recovery("android", exc, generation)
                    else:
                        invalid_plans += 1
                        decision_error = str(exc)[:CONTROL_STATUS_CHARACTERS]
                        self.log("plan_retry", count=invalid_plans, error=str(exc))
                        if invalid_plans >= CONTROL_INITIAL_INVALID_PLANS:
                            self._request_recovery("ai", "连续收到无效决策：" + decision_error, generation)
                            invalid_plans = 0
                        else:
                            self.status("正在重新观察游戏画面并修正决策")
                    cancel.wait(self.tuning.interval("input"))
                except ComponentFailure as exc:
                    self._authorized(generation, cancel)
                    if exc.component == "capture":
                        capture_failures += 1
                        self.log("capture_retry", count=capture_failures, error=str(exc))
                        if capture_failures < CONTROL_INITIAL_RECOVERY_FAILURES and self.android.alive():
                            cancel.wait(self.tuning.interval("capture"))
                            continue
                    component = "ai" if exc.component in {"ai", "ai_assets"} else "android"
                    self._request_recovery(component, exc, generation)
                    cancel.wait(self.tuning.interval("input"))
                except Exception as exc:
                    self._authorized(generation, cancel)
                    phase = self.progress_phase
                    component = "ai" if phase.startswith("plan") else "android" if phase in {"act", "observe"} else "ai"
                    if component == "android":
                        with self.action_lock:
                            self._authorized(generation, cancel)
                            with contextlib.suppress(Exception):
                                self.android.release_touches()
                    self._request_recovery(component, exc, generation)
                    cancel.wait(self.tuning.interval("input"))
        except Cancelled:
            pass
        except Exception as exc:
            self.log("worker_error", error=str(exc), traceback=traceback.format_exc())
            with self.lifecycle:
                current = self.desired_running and self.generation == generation and not cancel.is_set() and not self.shutdown.is_set()
            if current:
                self._request_recovery("android", exc, generation)
        finally:
            with self.action_lock:
                with self.lifecycle:
                    current = self.generation == generation
                    preserve = current and self.desired_running and not cancel.is_set() and not self._reset_android and self.android_ready and bool(self._fast_pointers) and self._fast_generation == generation
                    if current and not preserve:
                        self._fast_pointers.clear()
                        self._fast_wake.set()
                if current and not preserve:
                    with contextlib.suppress(Exception):
                        self.android.release_touches()
            with self.lifecycle:
                self._jobs.discard(threading.current_thread())
                restart = self.desired_running and self.generation == generation and not cancel.is_set() and not self.shutdown.is_set() and self.worker is threading.current_thread()
                if restart:
                    self.worker = threading.Thread(target=self._run, args=(generation, cancel), daemon=True, name="GameAI-Recovered-" + str(generation))
                    self.worker.start()

    def _save_capture(self, observation, png, plan):
        try:
            folder = safe_workspace_file(self.root, self.root / "state" / "captures")
            folder.mkdir(parents=True, exist_ok=True)
            interval = max(self.tuning.clock_floor, self.tuning.estimate("plan", CONTROL_MODEL_BOOTSTRAP_SECONDS))
            count = max(1, math.ceil(CONTROL_CAPTURE_HISTORY_SECONDS / interval))
            free = shutil.disk_usage(folder).free
            count = min(count, max(1, free // max(1, len(png)) // self.tuning.capacity))
            name = str(time.time_ns())
            temporary = safe_workspace_file(self.root, folder / (name + ".tmp"))
            temporary.write_bytes(png)
            os.replace(temporary, safe_workspace_file(self.root, folder / (name + ".png")))
            atomic_json(safe_workspace_file(self.root, folder / (name + ".json")), {"time": utc_now(), "decision_id": plan.get("decision_id"), "observation": observation, "game": plan.get("game"), "phase": plan.get("phase"), "assessment": plan.get("assessment"), "expected": plan.get("expected"), "reward_signal": plan.get("reward_signal")})
            captures = sorted((path for path in folder.glob("*.png") if not path_is_link(path)), key=lambda path: path.stat().st_mtime_ns)
            for old in captures[:-count]:
                old.unlink()
                with contextlib.suppress(OSError):
                    safe_workspace_file(self.root, old.with_suffix(".json")).unlink()
        except Exception as exc:
            self.log("capture_storage_error", error=str(exc))

    def manual(self, action, request_id=None):
        with self.lifecycle:
            if not self.manual_authorized():
                return False
            epoch = self._manual_epoch
            cancel = self._manual_cancel
        try:
            self._manual_queue.put_nowait((epoch, dict(action), request_id, cancel))
            return True
        except queue.Full:
            return False

    def manual_touch(self, points):
        with self.lifecycle:
            if not self.manual_authorized():
                return False
            frame = (self._manual_epoch, [dict(point) for point in points], self._manual_cancel)
            identifiers = {point.get("id", 0) for point in points}
            if self._manual_frames and self._manual_frames[-1][0] == self._manual_epoch and {point.get("id", 0) for point in self._manual_frames[-1][1]} == identifiers:
                self._manual_frames[-1] = frame
            else:
                self._manual_frames.append(frame)
            return True

    def _manual_gesture_samples(self, points):
        now = time.monotonic()
        active = {int(point.get("id", 0)): point for point in points if isinstance(point, dict)}
        with self.frame_lock:
            png, context, timestamp = self.frame, dict(self.context), self.frame_time
        capabilities = self.android.capabilities()
        finished = []
        with self.lifecycle:
            for identifier, item in list(self._manual_demo_active.items()):
                if identifier in active:
                    point = active[identifier]
                    item["last"] = (point["x"], point["y"])
                    continue
                self._manual_demo_active.pop(identifier, None)
                if not item.get("png") or not item.get("package"):
                    continue
                start, end = item["begin"], item["last"]
                size = item["size"]
                displacement = math.hypot(end[0] - start[0], end[1] - start[1]) / max(1, math.hypot(*size))
                duration = max(1, math.ceil((now - item["started"]) * AI_MILLISECONDS_PER_SECOND))
                if displacement >= LOCAL_AGENT_MANUAL_DRAG_FRACTION:
                    action = {"kind": "swipe", "x": start[0], "y": start[1], "x2": end[0], "y2": end[1], "ms": duration}
                elif duration >= capabilities.get("long_press_ms", AI_ANDROID_LONG_PRESS_INITIAL_MS):
                    action = {"kind": "long_press", "x": start[0], "y": start[1], "ms": duration}
                else:
                    action = {"kind": "tap", "x": start[0], "y": start[1], "ms": duration}
                if item["package"] == (self.last_game_package or item["package"]):
                    finished.append((item["observation"], item["png"], action))
            for identifier, point in active.items():
                if identifier in self._manual_demo_active or png is None:
                    continue
                package = str(context.get("package") or "")
                if not package or self._is_launcher_package(package) or package.startswith(("android", "com.android.", "com.google.android.")):
                    continue
                size = frame_dimensions(png)
                observation = game_observation(png, context, timestamp)
                observation["capabilities"] = capabilities
                observation["previous_phase"] = (self.last_plan or {}).get("phase", "unknown")
                observation["capture_started_at"] = self.frame_start_time
                self._manual_demo_active[identifier] = {"begin": (point["x"], point["y"]), "last": (point["x"], point["y"]), "started": now, "png": png, "package": package, "size": size, "observation": observation}
        return finished

    def _remember_manual_gestures(self, demonstrations):
        for observation, png, action in demonstrations:
            def learn(before=observation, picture=png, gesture=action):
                with self.model_lock:
                    saved = self.ai.remember_demonstration(before, picture, gesture)
                if saved.get("recorded"):
                    self.events.put(("demonstration", {"kind": gesture["kind"], "game": saved["package"], "demonstrations": saved["demonstrations"]}))
            self._job(learn, "LearnManualGameGesture", background=True)

    def _manual_loop(self):
        while not self.shutdown.is_set():
            pending = None
            with self.lifecycle:
                if self._manual_frames:
                    pending = self._manual_frames.popleft()
            if pending is not None:
                epoch, points, manual_cancel = pending
                try:
                    with self.action_lock:
                        with self.lifecycle:
                            allowed = self.manual_authorized() and self._manual_epoch == epoch
                        if allowed:
                            self.android.touch_frame(points, manual_cancel)
                            demonstrations = self._manual_gesture_samples(points)
                        else:
                            demonstrations = []
                    if demonstrations:
                        self._remember_manual_gestures(demonstrations)
                except Cancelled:
                    if self.shutdown.is_set():
                        return
                except GeometryPending as exc:
                    with self.lifecycle:
                        self._manual_frames.clear()
                    self.log("manual_geometry_transition", error=str(exc))
                    self.status("画面方向正在变化，请在新画面显示后继续操作")
                except Exception as exc:
                    self.log("manual_touch_error", error=str(exc))
                    self._request_recovery("android", exc)
            try:
                epoch, action, request_id, manual_cancel = self._manual_queue.get(timeout=self.android.input_interval())
            except queue.Empty:
                continue
            success = False
            try:
                with self.action_lock:
                    with self.lifecycle:
                        allowed = self.manual_authorized() and epoch == self._manual_epoch
                    if allowed:
                        self.android.release_touches(manual_cancel)
                        observation = {"size": self.android.screen_size(), "capabilities": self.android.capabilities()}
                        if action.get("target"):
                            first_context = self.android.game_context(manual_cancel, fresh=True)
                            ui_state = self.android.ui_snapshot(manual_cancel, fresh=True)
                            latest_context = self.android.game_context(manual_cancel, fresh=True)
                            if any(first_context.get(key) != latest_context.get(key) for key in ("package", "activity")):
                                raise ValueError("控件所在的游戏画面已变化，请刷新后重新点击")
                            if any(action.get("target_" + key) and action["target_" + key] != latest_context.get(key) for key in ("package", "activity")):
                                raise ValueError("当前游戏已不是智能按钮对应的画面")
                            observation["nodes"] = AI_disambiguate_nodes(ui_state["nodes"])
                        chosen = normalize_action(action, observation)
                        demonstration = None
                        if action.get("target") and latest_context.get("package"):
                            with self.frame_lock:
                                prior_picture = self.frame
                                captured_at = self.frame_time
                            if prior_picture is not None and frame_dimensions(prior_picture) == tuple(observation["size"]):
                                context = dict(latest_context)
                                context.update(nodes=observation["nodes"], capabilities=observation["capabilities"])
                                demonstration = (game_observation(prior_picture, context, captured_at), prior_picture, chosen)
                        self.android.act(chosen, manual_cancel)
                        success = True
                        if demonstration is not None:
                            self._remember_manual_gestures([demonstration])
            except Cancelled:
                if self.shutdown.is_set():
                    return
            except GeometryPending as exc:
                self.log("manual_geometry_transition", error=str(exc))
                self.status("画面方向正在变化，请在新画面显示后继续操作")
            except Exception as exc:
                self.log("manual_input_error", error=str(exc))
                self.status("安卓输入未完成：" + str(exc))
            finally:
                self._manual_queue.task_done()
                if request_id is not None:
                    self.events.put(("manual_text_result", {"request_id": request_id, "submitted": success}))

    def can_install(self):
        with self.lifecycle:
            return not (self.shutdown.is_set() or self.desired_running or self.resume_requested or self.stopping)

    def install(self, path):
        if not self.can_install():
            return False
        try:
            files = selected_apk_files(path)
            fingerprint = [{"size": file.stat().st_size, "mtime_ns": file.stat().st_mtime_ns} for file in files]
        except (OSError, TypeError, ValueError) as exc:
            self.status("请选择有效的 APK 文件：" + str(exc)[:CONTROL_STATUS_CHARACTERS])
            return False
        names = [str(file.resolve()) for file in files]
        with self.lifecycle:
            if not self.can_install():
                return False
            if any(item.get("source_paths", item.get("paths", [item.get("path")])) == names for item in self._pending_installs):
                self.status("这些 APK 已在安装队列中")
                return True
            batch_id = uuid.uuid4().hex
            self._pending_installs.append({"id": batch_id, "paths": names, "source_paths": names, "files": fingerprint, "attempts": 0})
            self._manual_epoch += 1
            self._manual_cancel.set()
            self._manual_cancel = threading.Event()
            self._manual_frames.clear()
            self._manual_demo_active.clear()
            self.ready_event.clear()
        self._save_pending_installs()
        self._job(lambda: self._cache_pending_apks(batch_id), "CacheImportedAPK", background=True)
        self.preparation_wake.set()
        self.log("apk_queued", names=[file.name for file in files])
        self.status("已加入安装队列，后台保存到工作文件夹并在安卓就绪后安装：" + ", ".join(file.name for file in files))
        return True

    def _phase_stall_seconds(self, phase, age):
        key = "plan" if phase.startswith("plan") or phase in {"judge_result", "confirm_result"} else "input" if phase == "act" else "accessibility" if phase == "observe_nodes" else "storage" if phase == "storage" else "capture"
        with self.tuning.lock:
            pressure = self.tuning.pressure
        fallback = AI_MEMORY_BUSY_SECONDS if phase == "storage" else RUNTIME_BOOTSTRAP_COMMAND_TIMEOUT_SECONDS
        budget = max(fallback, self.tuning.deadline(key, fallback) * (1 + pressure))
        now = time.monotonic()
        if phase in {"plan", "judge_result", "confirm_result"}:
            request_until = self.ai.active_request_deadline()
            if request_until is not None:
                budget = max(budget, request_until - (now - age) + self.tuning.deadline("input"))
        if phase == "act":
            with self.progress_lock:
                action_until = self._active_action_until
            if action_until:
                budget = max(budget, action_until - (now - age) + self.tuning.deadline("input"))
        return budget

    def _watchdog(self):
        while not self.shutdown.is_set():
            try:
                period = max(self.tuning.deadline("capture"), math.sqrt(self.tuning.estimate("plan", CONTROL_MODEL_BOOTSTRAP_SECONDS) * self.tuning.estimate("input")))
                if self.shutdown.wait(period):
                    return
                self._watchdog_cycle(period)
            except Exception as exc:
                self.log("runtime_monitor_error", error=str(exc), traceback=traceback.format_exc())
                if self.shutdown.wait(CONTROL_TIMER_BOOTSTRAP_SECONDS):
                    return

    def _watchdog_cycle(self, period):
        with self.lifecycle:
            for name, target, label in (("log_thread", self._write_logs, "BlackBoxWriter"), ("preparation_thread", self._prepare_forever, "AutomaticPreparation"), ("frame_thread", self._frames, "AndroidScreen"), ("context_thread", self._contexts, "AndroidContext"), ("manual_thread", self._manual_loop, "ManualAndroidInput"), ("fast_thread", self._fast_loop, "RealtimeTouchControl")):
                thread = getattr(self, name)
                if thread.ident is not None and not thread.is_alive() and not self.shutdown.is_set():
                    replacement = threading.Thread(target=target, daemon=True, name=label)
                    setattr(self, name, replacement)
                    replacement.start()
                    self.log("runtime_thread_restarted", thread=label)
        if self.ready_event.is_set():
            if not self._runtime_alive():
                self._request_recovery("android", "安卓进程已退出")
            elif not self.ai.alive():
                self._request_recovery("ai", "本地学习器尚未就绪")
        with self.lifecycle:
            running, worker, generation, cancel = self.desired_running, self.worker, self.generation, self.run_cancel
            pending_stop = self._pending_stop_release
        if pending_stop is not None:
            self._complete_stop(*pending_stop)
        if running and (worker is None or not worker.is_alive()) and cancel is not None and not cancel.is_set():
            with self.lifecycle:
                if self.desired_running and generation == self.generation and self.worker is worker:
                    self.worker = threading.Thread(target=self._run, args=(generation, cancel), daemon=True, name="GameAI-Recover-" + str(generation))
                    self.worker.start()
        with self.progress_lock:
            phase, age = self.worker_progress_phase, time.monotonic() - self.worker_progress_at
        if running and worker is not None and worker.is_alive() and phase in CONTROL_MONITORED_WORK_PHASES and age > self._phase_stall_seconds(phase, age):
            component = "android" if phase in {"observe", "observe_after", "observe_stale", "observe_nodes", "act"} else "ai"
            if component == "ai":
                self.ai.cancel_request()
            self._request_recovery(component, "工作线程在 " + phase + " 阶段超过预期时长仍无进展")
        if self._intent_dirty:
            with self.lifecycle:
                self._persist_run_intent(self.desired_running or self.resume_requested)
        self._update_resources()
        total_mb, free_mb = system_memory_mb()
        variability = self.tuning.estimate("memory_variation_mb", 0, CONTROL_LATENCY_QUANTILE)
        protected_mb = protected_desktop_memory_mb(total_mb, variability)
        critical = free_mb < protected_mb * CONTROL_MEMORY_CRITICAL_FRACTION
        level = int(free_mb < protected_mb) + int(critical)
        if level != self._memory_pressure:
            self._memory_pressure = level
            self.log("desktop_memory_pressure", level=level, available_mb=free_mb, protected_mb=protected_mb)
            if critical:
                self.status("Windows 内存紧张，正在根据实际开销调整采样与后台资源")
        maintenance_period = max(self.tuning.deadline("plan"), period * self.tuning.capacity)
        with self.lifecycle:
            maintenance_due = not self._maintenance_active and time.monotonic() - self._last_memory_check >= maintenance_period
            if maintenance_due:
                self._last_memory_check = time.monotonic()
                self._maintenance_active = True
        if maintenance_due:
            def maintain():
                try:
                    self.memory.maintain()
                    policy_storage = self.ai.maintain()
                    if isinstance(policy_storage, dict) and policy_storage.get("archived"):
                        self.log("local_policy_storage_maintained", **policy_storage)
                    self.tuning.save()
                except Exception as exc:
                    self.log("storage_maintenance_error", error=str(exc))
                finally:
                    with self.lifecycle:
                        self._maintenance_active = False
            self._job(maintain, "MaintainExperience", background=True)

    def _update_resources(self):
        try:
            sample = self.desktop_load.sample()
            available = sample["free_mb"]
            if self._previous_available_mb is not None:
                self.tuning.observe("memory_variation_mb", abs(available - self._previous_available_mb))
            self._previous_available_mb = available
            variability = self.tuning.estimate("memory_variation_mb", 0, CONTROL_LATENCY_QUANTILE)
            reserve = protected_desktop_memory_mb(sample["total_mb"], variability)
            memory_pressure = max(0.0, (reserve - available) / max(1, reserve))
            cpu = sample.get("cpu_percent")
            capacity = max(1, os.cpu_count() or 1)
            cpu_share = max(CONTROL_DESKTOP_CORE_FRACTION, 1 / capacity)
            busy = sample.get("other_app_active") and isinstance(cpu, (int, float))
            cpu_pressure = max(0.0, (float(cpu) / CONTROL_PERCENT_SCALE - (1 - cpu_share)) / cpu_share) if busy else 0.0
            refresh = max(1.0, float(getattr(self.android, "_refresh_hz", CONTROL_FRAME_BOOTSTRAP_HZ)))
            ui_pressure = max(0.0, self.tuning.estimate("ui_poll", 0.0) * refresh - 1) if self.ui_visible else 0.0
            with self.tuning.lock:
                self.tuning.pressure = max(memory_pressure, cpu_pressure, ui_pressure)
            self._background_pressure = self.tuning.pressure > 0
            for name in ("ui_render_seconds", "ui_poll_seconds"):
                value = getattr(self, name, None)
                if isinstance(value, (int, float)):
                    self.tuning.observe(name.removesuffix("_seconds"), value)
            sample.update(yielding=self._background_pressure, model=self.ai.model_name, backend=self.ai.backend, android_mb=self.android.memory_mb, ai_threads=1, ready_seconds=self.ready_seconds, protected_mb=reserve, adaptive=self.tuning.snapshot(), readiness=self.readiness_checks())
            self.resource_sample = sample
            for job in (getattr(self.android, "_emulator_job", None), getattr(self.ai, "_process_job", None)):
                if job is not None:
                    job.set_background_policy(self._background_pressure)
            self.events.put(("resources", sample))
        except Exception as exc:
            self.log("resource_monitor_error", error=str(exc))

    def enable_supervision(self):
        if self.supervision_enabled or self.shutdown.is_set():
            return
        self.supervision_enabled = True
        self._write_supervisor_state()
        self.supervisor_thread = threading.Thread(target=self._supervisor_pulse, daemon=True, name="SupervisorPulse")
        self.supervisor_thread.start()
        if not self.supervised_child:
            self._launch_supervisor()

    def _launch_supervisor(self):
        try:
            folder = self.root / "logs"
            folder.mkdir(exist_ok=True)
            with (folder / "supervisor-output.log").open("ab", buffering=0) as output:
                program = self.supervisor_program_path if self.supervisor_program_path.is_file() and not path_is_link(self.supervisor_program_path) else pathlib.Path(__file__).resolve()
                self.supervisor_process_handle = subprocess.Popen([sys.executable, str(program), "--watchdog", str(self.root), str(os.getpid())], stdin=subprocess.DEVNULL, stdout=output, stderr=subprocess.STDOUT, cwd=str(self.root), creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0), shell=False)
        except Exception as exc:
            self.log("supervisor_error", error=str(exc))

    def _write_supervisor_state(self):
        if not self.supervision_enabled:
            return
        with self.progress_lock:
            if self.desired_running:
                phase = self.worker_progress_phase
                age = time.monotonic() - self.worker_progress_at
            else:
                phase = self.progress_phase
                age = time.monotonic() - self.last_progress
        active = phase in CONTROL_MONITORED_WORK_PHASES
        expected = self._phase_stall_seconds(phase, age) if active else None
        with self.lifecycle:
            payload = {"pid": os.getpid(), "token": process_token(os.getpid()), "heartbeat": time.time(), "progress_age_seconds": age, "expected_progress_seconds": expected, "phase": phase, "acceleration": getattr(self.android, "acceleration", None), "desired_running": bool(self.desired_running or self.resume_requested), "intent_revision": self.intent_revision, "closing": self.shutdown.is_set()}
        atomic_json(self.supervisor_state_path, payload)

    def _supervisor_pulse(self):
        while not self.shutdown.wait(CONTROL_SUPERVISOR_HEARTBEAT_SECONDS):
            try:
                self._write_supervisor_state()
                if not self.supervised_child and (self.supervisor_process_handle is None or self.supervisor_process_handle.poll() is not None):
                    self._launch_supervisor()
            except Exception as exc:
                self.log("supervisor_error", error=str(exc))

    def export(self):
        with self.lifecycle:
            if self.exporting or self.shutdown.is_set():
                return
            self.exporting = True
        def work():
            staging = None
            partial = None
            try:
                self.status("正在生成桌面黑匣子")
                export_errors = []
                flush = threading.Event()
                try:
                    self.logs.put(("__flush__", flush), timeout=self.tuning.deadline("log"))
                    flushed_until = time.monotonic() + self.tuning.deadline("log") + self.tuning.deadline("input")
                    while not flush.is_set() and time.monotonic() < flushed_until:
                        check_cancel(self.shutdown)
                        flush.wait(min(RUNTIME_CANCEL_POLL_SECONDS, max(0.0, flushed_until - time.monotonic())))
                    if not flush.is_set():
                        export_errors.append("诊断日志未在期限内全部写入")
                except queue.Full:
                    export_errors.append("诊断日志队列暂时已满")
                folder = self.root / "exports"
                check_cancel(self.shutdown)
                folder.mkdir(exist_ok=True)
                staging = pathlib.Path(tempfile.mkdtemp(prefix="blackbox_", dir=folder))
                payload = staging / "payload"
                payload.mkdir()
                try:
                    self.memory.backup(payload / "game_experience.sqlite3", self.shutdown)
                except Cancelled:
                    raise
                except Exception as exc:
                    export_errors.append("游戏经验备份失败：" + str(exc))
                try:
                    self.ai.backup(payload / "local_policy.sqlite3", self.shutdown)
                except Cancelled:
                    raise
                except Exception as exc:
                    export_errors.append("本地策略备份失败：" + str(exc))
                with self.frame_lock:
                    frame = self.frame
                    context = dict(self.context)
                    frame_time = self.frame_time
                if frame:
                    (payload / "android_screen.png").write_bytes(frame)
                try:
                    android_diagnostics = self.android.diagnostics(self.shutdown)
                except Cancelled:
                    raise
                except Exception as exc:
                    android_diagnostics = {"error": str(exc)}
                    export_errors.append("安卓诊断失败：" + str(exc))
                atomic_json(payload / "diagnostics.json", {"application": APP_NAME, "version": APP_VERSION, "time": utc_now(), "python": platform.python_version(), "system": platform.platform(), "cpu_count": os.cpu_count(), "memory_mb": physical_memory_mb(), "available_memory_mb": available_memory_mb(), "state": self.operation_state(), "actions": self.input_steps, "total_actions": self.completed_steps, "wait_actions": self.wait_steps, "ai_decisions": self.ai_decisions, "recoveries": self.recoveries, "stale_rejections": self.stale_rejections, "scene_interruptions": self.scene_interruptions, "realtime_perception": self.perception.state(), "ui_events_dropped": self.events.dropped, "context": context, "last_frame_age_seconds": time.monotonic() - frame_time if frame_time else None, "planning_seconds": self.plan_seconds, "capture_seconds": self.capture_seconds, "model": getattr(self.ai, "model_name", ""), "backend": getattr(self.ai, "backend", ""), "ai_verified": bool(self.ai._validated and self.ai.alive()), "ai_last_error": self.ai._last_engine_error, "learning": self.ai.learning_stats(), "environment_error": self.environment_error, "android": android_diagnostics, "resources": getattr(self, "resource_budget", {}), "resource_sample": self.resource_sample, "adaptive_control": self.tuning.snapshot(), "runtime_measurements": self.android.measurements.snapshot(), "startup_seconds": self.ready_seconds, "startup_stages": self._startup_diagnostics(), "last_plan": {key: ([stored_action(item) for item in value] if key == "actions" else value) for key, value in (self.last_plan or {}).items()}, "last_observation": self.last_observation, "supervisor": read_json(self.supervisor_state_path, {}), "export_errors": export_errors})
                try:
                    recent_issues = self.memory.diagnostic_events()
                except Exception as exc:
                    recent_issues = []
                    export_errors.append("问题摘要读取失败：" + str(exc))
                timings = sorted(float(value) for value in self.ai.timings if isinstance(value, (int, float)) and math.isfinite(value))
                overview = {"version": APP_VERSION, "generated_at": utc_now(), "operation_state": self.operation_state(), "android_ready": self.android_ready, "ai_healthy": bool(self.ai.alive() and self.ai._healthy), "game_package": context.get("package", ""), "last_game_package": self.last_game_package, "selected_game_package": self.selected_game_package, "android_acceleration": self.android.acceleration, "android_api_level": self.android.device_api_level, "android_image": self.android.IMAGE_PACKAGE, "model": self.ai.model_name, "ai_backend": self.ai.backend, "completed_actions": self.input_steps, "total_actions": self.completed_steps, "wait_actions": self.wait_steps, "ai_decisions": self.ai_decisions, "recoveries": self.recoveries, "stale_rejections": self.stale_rejections, "scene_interruptions": self.scene_interruptions, "realtime_perception": self.perception.state(), "ui_events_dropped": self.events.dropped, "startup_seconds": self.ready_seconds, "startup_stages": self._startup_diagnostics(), "last_capture_seconds": self.capture_seconds, "last_decision_seconds": self.plan_seconds, "decision_samples": len(timings), "decision_median_seconds": statistics.median(timings) if timings else None, "decision_p95_seconds": timings[max(0, math.ceil(CONTROL_LATENCY_QUANTILE * len(timings)) - 1)] if timings else None, "recent_issues": recent_issues}
                atomic_json(payload / "overview.json", overview)
                support = self.android.state_paths() + [self.run_intent_path, self.supervisor_state_path]
                for source in (self.root / "logs").glob("*"):
                    check_cancel(self.shutdown)
                    if source.is_file():
                        support.append(source)
                for index, source in enumerate(support):
                    check_cancel(self.shutdown)
                    source = pathlib.Path(source)
                    try:
                        source.resolve().relative_to(self.root)
                    except ValueError:
                        continue
                    if source.is_file() and not path_is_link(source):
                        try:
                            with source.open("rb") as handle:
                                handle.seek(max(0, source.stat().st_size - CONTROL_ARCHIVE_TAIL_BYTES))
                                (payload / (str(index) + "_" + source.name)).write_bytes(handle.read(CONTROL_ARCHIVE_TAIL_BYTES))
                        except OSError as exc:
                            export_errors.append("日志读取失败：" + source.name + "：" + str(exc))
                for relative in ("state/captures", "data/archives", "data/policy-archives"):
                    check_cancel(self.shutdown)
                    source = self.root / relative
                    if source.is_dir() and not path_is_link(source):
                        destination = payload / source.name
                        destination.mkdir(exist_ok=True)
                        for item in source.iterdir():
                            check_cancel(self.shutdown)
                            if item.is_file() and not path_is_link(item) and item.suffix in {".png", ".json", ".gz"}:
                                try:
                                    with item.open("rb") as source_file, (destination / item.name).open("wb") as target_file:
                                        self._copy_export_stream(source_file, target_file)
                                except OSError as exc:
                                    export_errors.append("历史文件读取失败：" + item.name + "：" + str(exc))
                source_program = self.supervisor_program_path if self.supervisor_program_path.is_file() and not path_is_link(self.supervisor_program_path) else pathlib.Path(__file__).resolve()
                with source_program.open("rb") as source_file, (payload / "program.py").open("wb") as target_file:
                    self._copy_export_stream(source_file, target_file)
                if export_errors:
                    atomic_json(payload / "export_errors.json", export_errors)
                    diagnostics = read_json(payload / "diagnostics.json", {})
                    if isinstance(diagnostics, dict):
                        diagnostics["export_errors"] = export_errors
                        atomic_json(payload / "diagnostics.json", diagnostics)
                entries = [item for item in payload.rglob("*") if item.is_file()]
                atomic_json(payload / "manifest.json", {"time": utc_now(), "complete": not bool(export_errors), "error_count": len(export_errors), "files": [{"path": item.relative_to(payload).as_posix(), "bytes": item.stat().st_size, "sha256": hash_file(item, "sha256", self.shutdown)} for item in entries]})
                archive_path = staging / "blackbox.zip"
                with zipfile.ZipFile(archive_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=zlib.Z_BEST_SPEED if self._background_pressure else None, allowZip64=True) as archive:
                    for item in payload.rglob("*"):
                        check_cancel(self.shutdown)
                        if item.is_file():
                            with item.open("rb") as source_file, archive.open(item.relative_to(payload).as_posix(), "w", force_zip64=True) as target_file:
                                self._copy_export_stream(source_file, target_file)
                with zipfile.ZipFile(archive_path) as archive:
                    manifest = json.loads(archive.read("manifest.json"))
                    files = {item["path"]: item for item in manifest["files"]}
                    entries_in_archive = {item.filename for item in archive.infolist() if not item.is_dir()}
                    if entries_in_archive != set(files) | {"manifest.json"}:
                        raise OSError("黑匣子压缩包内容与清单不一致")
                    for item in archive.infolist():
                        if item.is_dir():
                            continue
                        digest = hashlib.sha256()
                        length = 0
                        with archive.open(item) as source_file:
                            while True:
                                check_cancel(self.shutdown)
                                block = source_file.read(CONTROL_ARCHIVE_COPY_BYTES)
                                if not block:
                                    break
                                digest.update(block)
                                length += len(block)
                        if item.filename != "manifest.json" and (length != files[item.filename]["bytes"] or digest.hexdigest() != files[item.filename]["sha256"]):
                            raise OSError("黑匣子压缩包复核失败：" + item.filename)
                desktop = desktop_directory()
                desktop.mkdir(parents=True, exist_ok=True)
                name = "AndroidAI_BlackBox_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S_%f") + ".zip"
                destination = desktop / name
                partial = desktop / (name + ".part")
                if shutil.disk_usage(desktop).free < archive_path.stat().st_size + max(CONTROL_ARCHIVE_COPY_BYTES, math.ceil(archive_path.stat().st_size / self.tuning.capacity)):
                    raise OSError("桌面所在磁盘空间不足")
                with archive_path.open("rb") as source, partial.open("xb") as target:
                    self._copy_export_stream(source, target)
                    target.flush()
                    os.fsync(target.fileno())
                if hash_file(partial, "sha256", self.shutdown) != hash_file(archive_path, "sha256", self.shutdown):
                    raise OSError("黑匣子复制校验失败")
                os.replace(partial, destination)
                self.events.put(("exported", {"path": str(destination), "complete": not bool(export_errors), "errors": export_errors}))
                self.status(("黑匣子完整保存到桌面 · " if not export_errors else "黑匣子部分保存到桌面，存在 " + str(len(export_errors)) + " 项缺失 · ") + name + " · 请注意隐私")
                self.log("blackbox_saved", file=str(destination), complete=not bool(export_errors), errors=export_errors)
            finally:
                if partial is not None:
                    with contextlib.suppress(OSError):
                        partial.unlink()
                if staging is not None:
                    shutil.rmtree(staging, ignore_errors=True)
                with self.lifecycle:
                    self.exporting = False
        self._job(work, "BlackBoxExport", background=True)

    def _copy_export_stream(self, source, target):
        while True:
            check_cancel(self.shutdown)
            block = source.read(CONTROL_ARCHIVE_COPY_BYTES)
            if not block:
                return
            check_cancel(self.shutdown)
            target.write(block)

    def close(self):
        with self.lifecycle:
            if self.shutdown.is_set():
                return
            self.run_latch.stop()
            self.desired_running = False
            self.resume_requested = False
            self.generation += 1
            self._manual_epoch += 1
            self._manual_cancel.set()
            self._fast_pointers.clear()
            self._fast_generation = None
            self._fast_wake.set()
            self.stopping = True
            if self.run_cancel is not None:
                self.run_cancel.set()
            self._persist_run_intent(False)
            self.shutdown.set()
            self.ready_event.clear()
            self._readiness = dict.fromkeys(self._readiness, False)
            self.preparation_wake.set()
        with contextlib.suppress(Exception):
            self._write_supervisor_state()
        with contextlib.suppress(Exception):
            self.ai.cancel_request()
        with contextlib.suppress(Exception):
            self.android.release_touches()
        with contextlib.suppress(Exception):
            self.ai.stop()
        with contextlib.suppress(Exception):
            self.android.close()
        threads = [self.worker, self.preparation_thread, self.frame_thread, self.context_thread, self.manual_thread, self.fast_thread, self.watchdog_thread, self.supervisor_thread]
        close_deadline = time.monotonic() + self.tuning.deadline("shutdown", CONTROL_SHUTDOWN_GRACE_SECONDS)
        for thread in threads:
            if thread is not None and thread is not threading.current_thread() and thread.ident is not None:
                thread.join(timeout=max(0.0, close_deadline - time.monotonic()))
        with self.lifecycle:
            jobs = list(self._jobs)
        for thread in jobs:
            if thread is not threading.current_thread():
                thread.join(timeout=max(0.0, close_deadline - time.monotonic()))
        with contextlib.suppress(Exception):
            self.ai.stop()
        with contextlib.suppress(Exception):
            self.android.close()
        with contextlib.suppress(Exception):
            self.tuning.save()
        self.log("session_closed")
        with contextlib.suppress(queue.Full):
            self.logs.put(None, timeout=1)
        if self.log_thread.ident is not None:
            self.log_thread.join(timeout=max(0.0, close_deadline - time.monotonic()))
        live = [thread.name for thread in threads + jobs if thread is not None and thread.is_alive()]
        if not live and not self.log_thread.is_alive():
            self.memory.close()
        self.run_latch.close()
        self.workspace_lock.close()

    def _cache_apks(self, files, cancel=None):
        cancel = cancel or self.shutdown
        folder = safe_workspace_file(self.root, self.root / "imports")
        folder.mkdir(parents=True, exist_ok=True)
        cached = []
        for source in files:
            check_cancel(cancel)
            digest = hash_file(source, "sha256", cancel)
            destination = safe_workspace_file(self.root, folder / digest / source.name)
            destination.parent.mkdir(exist_ok=True)
            if source.resolve() == destination or destination.is_file() and hash_file(destination, "sha256", cancel) == digest:
                cached.append(destination)
                continue
            required = source.stat().st_size
            if shutil.disk_usage(folder).free <= required:
                raise OSError("工作文件夹空间不足以保存导入的 APK")
            temporary = safe_workspace_file(self.root, destination.with_suffix(".part"))
            try:
                with source.open("rb") as reader, temporary.open("wb") as writer:
                    while True:
                        check_cancel(cancel)
                        block = reader.read(CONTROL_ARCHIVE_COPY_BYTES)
                        if not block:
                            break
                        writer.write(block)
                    writer.flush()
                    os.fsync(writer.fileno())
                if hash_file(temporary, "sha256", cancel) != digest:
                    raise OSError("导入的 APK 在复制期间发生变化")
                safe_workspace_file(self.root, destination)
                os.replace(temporary, destination)
                cached.append(destination)
            finally:
                with contextlib.suppress(OSError):
                    temporary.unlink()
        return cached

    def _cache_pending_apks(self, batch_id):
        with self._apk_cache_lock:
            with self.lifecycle:
                pending = next((dict(item) for item in self._pending_installs if item.get("id") == batch_id), None)
            if pending is None or self.shutdown.is_set():
                return
            files = [Path(path) for path in pending.get("paths", ())]
            try:
                sources = selected_apk_files(files)
                expected = pending.get("files", ())
                if len(sources) != len(expected):
                    raise ValueError("待缓存 APK 数量已改变")
                for source, record in zip(sources, expected):
                    details = source.stat()
                    if details.st_size != record.get("size") or details.st_mtime_ns != record.get("mtime_ns"):
                        raise ValueError("原始 APK 已改变，无法安全缓存")
                copies = self._cache_apks(sources, self.shutdown)
                fingerprints = [{"size": path.stat().st_size, "mtime_ns": path.stat().st_mtime_ns} for path in copies]
                with self.lifecycle:
                    for item in self._pending_installs:
                        if item.get("id") == batch_id:
                            item.update(paths=[str(path) for path in copies], files=fingerprints, cached=True)
                            break
                self._save_pending_installs()
                self.status("APK 已安全缓存到工作文件夹：" + ", ".join(path.name for path in copies))
                self.preparation_wake.set()
            except Cancelled:
                return
            except Exception as exc:
                self.log("apk_cache_error", batch=batch_id, error=str(exc))
                self.status("APK 暂未完成缓存，安装准备时会重试：" + str(exc)[:CONTROL_STATUS_CHARACTERS])

    def _remember_install(self, files):
        saved = self.memory.get("installed_apks", [])
        saved = [item for item in saved if isinstance(item, dict) and isinstance(item.get("paths"), list)] if isinstance(saved, list) else []
        groups = {}
        for file in files:
            info = apk_package_info(file)
            groups.setdefault(info["package"], []).append((file, info))
        for package, items in groups.items():
            names = [str(file) for file, info in sorted(items, key=lambda item: (bool(item[1]["split"]), item[1]["split"]))]
            saved = [item for item in saved if item["paths"] != names]
            saved.append({"package": package, "paths": names, "image": self.android.IMAGE_PACKAGE, "at": utc_now()})
        self.memory.set("installed_apks", saved)


UI_MILLISECONDS_PER_SECOND = 1000


UI_BYTES_PER_KIB = 1024


UI_BYTES_PER_MIB = UI_BYTES_PER_KIB * UI_BYTES_PER_KIB


UI_MIB_PER_GIB = 1024


UI_SECONDS_PER_MINUTE = 60


UI_READINESS_CHECK_LABELS = {"capture": "截图解码", "input": "输入通道", "decision": "真实决策"}


UI_PREPARATION_LABELS = {"android_assets": "本机安卓组件", "ai_assets": "本地学习数据", "resource_plan": "设备资源分配", "android_boot": "设备连接与真实截图", "ai_load": "本地学习器初始化", "ai_visual_verify": "真实截图解码", "input_verify": "输入通道检查", "ai_decision_verify": "真实动作决策检查", "game_restore": "导入安装与游戏恢复"}


UI_PREPARATION_STATES = {"working": "进行中", "complete": "已通过", "failed": "尚未通过", "blocked": "本机条件不满足"}


UI_PERCENT_SCALE = 100


UI_RECT_EDGE_COUNT = 2


UI_RGB_CHANNELS = 3


UI_RGB_RED_CHANNEL = 0


UI_RGB_GREEN_CHANNEL = 1


UI_RGB_BLUE_CHANNEL = 2


UI_RGB_MAX = 255


UI_BITMAP_ROW_ALIGNMENT = 4


UI_POINTS_PER_INCH = 72


UI_DEFAULT_REFRESH_HZ = 60


UI_EVENT_RESPONSE_SECONDS = 0.05


UI_BACKGROUND_EVENT_SECONDS = 0.2


UI_INITIAL_WINDOW_SHARE = 0.875


UI_TITLE_FONT_SCALE = 1.25


UI_PROGRESS_BAR_HEIGHT_DIVISOR = 4


UI_MOUSE_LEFT = 1


UI_MOUSE_RIGHT = 3


UI_MOUSE_WHEEL_DELTA = 120


UI_WM_DROPFILES = 0x0233


UI_WM_COPYDATA = 0x004A


UI_WM_COPYGLOBALDATA = 0x0049


UI_GWLP_WNDPROC = -4


UI_MSGFLT_ALLOW = 1


UI_MSGFLT_RESET = 0


UI_DROP_FILE_COUNT_QUERY = ctypes.c_uint(-1).value


UI_MONITOR_DEFAULTTONEAREST = 2


UI_VREFRESH = 116


UI_GDIPLUS_VERSION = 1


UI_PIXEL_FORMAT_24BPP_RGB = 0x21808


UI_INTERPOLATION_HIGH_QUALITY_BILINEAR = 6


UI_COM_RELEASE_INDEX = 2


UI_THREAD_PRIORITY_BELOW_NORMAL = -1


UI_STATE_LABELS = {"PREPARING": "本机环境检测中", "READY": "全部就绪", "RUNNING": "Agent 接管中", "RECOVERING": "设备自动恢复中", "STOPPING": "正在释放控制", "BLOCKED": "环境尚未就绪", "UNAVAILABLE": "环境不可用", "CLOSED": "正在退出"}


UI_PHASE_LABELS = {"menu": "菜单", "playing": "游戏中", "result": "结算候选", "loading": "加载中", "unknown": "状态待识别", "exploring": "探索中", "exploration": "探索中"}


UI_ACTION_LABELS = {"tap": "点击", "swipe": "滑动", "long_press": "长按", "touch_begin": "按住触点", "touch_update": "移动触点", "touch_end": "释放触点", "touch_release_all": "释放全部触点", "touch": "多点触控", "wait": "观察画面", "type": "输入文字", "keyevent": "按键", "back": "返回", "home": "主页", "recents": "最近应用"}


UI_COLORS = {"background": "#101827", "surface": "#172337", "screen": "#050a13", "border": "#34465f", "text": "#f0f5fc", "muted": "#aab9ce", "accent": "#8ec5ff", "start": "#16784a", "stop": "#b92b49", "export": "#235cab", "progress": "#52caa4", "warning": "#ffc9b4", "vision": "#f4c56e", "ui_control": "#67d8bd", "next_action": "#fb7185", "hypothesis": "#b89cff", "learned_control": "#5ea7ff"}


class UI_WindowEnvironment:
    def __init__(self, window):
        self.window = window
        self.user32 = None
        self.gdi32 = None
        if os.name == "nt":
            try:
                class Rect(ctypes.Structure):
                    _fields_ = [("left", ctypes.c_long), ("top", ctypes.c_long), ("right", ctypes.c_long), ("bottom", ctypes.c_long)]
                class MonitorInfo(ctypes.Structure):
                    _fields_ = [("size", ctypes.c_uint32), ("monitor", Rect), ("work", Rect), ("flags", ctypes.c_uint32)]
                self.monitor_type = MonitorInfo
                self.user32 = ctypes.WinDLL("user32", use_last_error=True)
                self.gdi32 = ctypes.WinDLL("gdi32", use_last_error=True)
                self.user32.GetDpiForWindow.argtypes = [ctypes.c_void_p]
                self.user32.GetDpiForWindow.restype = ctypes.c_uint
                self.user32.MonitorFromWindow.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
                self.user32.MonitorFromWindow.restype = ctypes.c_void_p
                self.user32.GetMonitorInfoW.argtypes = [ctypes.c_void_p, ctypes.POINTER(MonitorInfo)]
                self.user32.GetMonitorInfoW.restype = ctypes.c_int
                self.user32.GetDC.argtypes = [ctypes.c_void_p]
                self.user32.GetDC.restype = ctypes.c_void_p
                self.user32.ReleaseDC.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
                self.user32.ReleaseDC.restype = ctypes.c_int
                self.gdi32.GetDeviceCaps.argtypes = [ctypes.c_void_p, ctypes.c_int]
                self.gdi32.GetDeviceCaps.restype = ctypes.c_int
            except (AttributeError, OSError):
                self.user32 = None
                self.gdi32 = None

    def dpi(self):
        if self.user32 is not None:
            result = self.user32.GetDpiForWindow(self.window.winfo_id())
            if result:
                return float(result)
        return float(self.window.winfo_fpixels("1i"))

    def work_area(self):
        if self.user32 is not None:
            monitor = self.user32.MonitorFromWindow(self.window.winfo_id(), UI_MONITOR_DEFAULTTONEAREST)
            info = self.monitor_type()
            info.size = ctypes.sizeof(info)
            if monitor and self.user32.GetMonitorInfoW(monitor, ctypes.byref(info)):
                work = info.work
                return work.left, work.top, work.right - work.left, work.bottom - work.top
        return 0, 0, self.window.winfo_screenwidth(), self.window.winfo_screenheight()

    def refresh_rate(self):
        if self.user32 is not None and self.gdi32 is not None:
            hwnd = self.window.winfo_id()
            dc = self.user32.GetDC(hwnd)
            if dc:
                try:
                    rate = self.gdi32.GetDeviceCaps(dc, UI_VREFRESH)
                    if rate > 1:
                        return rate
                finally:
                    self.user32.ReleaseDC(hwnd, dc)
        return UI_DEFAULT_REFRESH_HZ


class UI_AdaptiveCadence:
    def __init__(self, refresh_rate):
        self.refresh_rate = max(1, float(refresh_rate))
        self.samples = {}
        self.cpu_percent = None
        self.yielding = False
        self.last_capture = None

    @property
    def refresh_period(self):
        return 1 / self.refresh_rate

    def observe(self, kind, seconds):
        if not isinstance(seconds, (int, float)) or not math.isfinite(seconds) or seconds <= 0:
            return
        capacity = max(1, math.ceil(self.refresh_rate))
        values = self.samples.get(kind)
        if values is None or values.maxlen != capacity:
            values = collections.deque(values or (), maxlen=capacity)
            self.samples[kind] = values
        values.append(float(seconds))

    def typical(self, kind, fallback=None):
        values = sorted(self.samples.get(kind, ()))
        if not values:
            return self.refresh_period if fallback is None else fallback
        middle = len(values) // UI_RECT_EDGE_COUNT
        return values[middle] if len(values) % UI_RECT_EDGE_COUNT else (values[middle - 1] + values[middle]) / UI_RECT_EDGE_COUNT

    def spread(self, kind):
        values = self.samples.get(kind, ())
        if not values:
            return 0.0
        typical = self.typical(kind)
        return math.sqrt(sum((value - typical) ** UI_RECT_EDGE_COUNT for value in values) / len(values))

    def capture(self, captured):
        if isinstance(captured, (int, float)) and math.isfinite(captured) and captured > 0:
            if self.last_capture is not None and captured > self.last_capture:
                self.observe("capture", captured - self.last_capture)
            if self.last_capture is None or captured >= self.last_capture:
                self.last_capture = captured

    def resources(self, value):
        cpu = value.get("cpu_percent")
        self.cpu_percent = max(0.0, min(UI_PERCENT_SCALE, float(cpu))) if isinstance(cpu, (int, float)) and math.isfinite(cpu) else None
        self.yielding = bool(value.get("yielding"))

    def available_share(self):
        processors = max(1, os.cpu_count() or 1)
        spare = max(1, processors - 1) if self.cpu_percent is None else max(0.0, processors * (1 - self.cpu_percent / UI_PERCENT_SCALE))
        share = spare / (1 + spare)
        if self.yielding:
            share /= 1 + processors
        return max(self.refresh_period / (UI_BACKGROUND_EVENT_SECONDS + self.refresh_period), share)

    def frame_interval(self):
        render = self.typical("render", 0.0) + self.typical("paint", 0.0)
        return max(self.refresh_period, self.typical("capture"), render / self.available_share())

    def stale_after(self, capture_seconds=None):
        latency = capture_seconds if isinstance(capture_seconds, (int, float)) and math.isfinite(capture_seconds) and capture_seconds > 0 else 0.0
        return max(self.frame_interval(), self.typical("capture"), latency) + self.spread("capture") + max(self.refresh_period, latency)

    def poll_delay(self, visible, pending=False):
        response = UI_EVENT_RESPONSE_SECONDS if visible else UI_BACKGROUND_EVENT_SECONDS
        target = self.refresh_period if pending else min(response, self.frame_interval()) if visible else response
        cost = self.typical("poll", 0.0) / self.available_share()
        return max(1, math.ceil(max(self.refresh_period, min(response, max(target, cost))) * UI_MILLISECONDS_PER_SECOND))


class UI_WindowsImageScaler:
    def __init__(self):
        if os.name != "nt":
            raise OSError("当前系统不提供 Windows 原生图像缩放")
        class StartupInput(ctypes.Structure):
            _fields_ = [("version", ctypes.c_uint32), ("callback", ctypes.c_void_p), ("suppress_background", ctypes.c_int), ("suppress_codecs", ctypes.c_int)]
        self.gdiplus = ctypes.WinDLL("gdiplus", use_last_error=True)
        self.shlwapi = ctypes.WinDLL("shlwapi", use_last_error=True)
        specifications = {
            "GdiplusStartup": ([ctypes.POINTER(ctypes.c_size_t), ctypes.POINTER(StartupInput), ctypes.c_void_p], ctypes.c_int),
            "GdiplusShutdown": ([ctypes.c_size_t], None),
            "GdipCreateBitmapFromStream": ([ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p)], ctypes.c_int),
            "GdipCreateBitmapFromScan0": ([ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p)], ctypes.c_int),
            "GdipGetImageGraphicsContext": ([ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p)], ctypes.c_int),
            "GdipSetInterpolationMode": ([ctypes.c_void_p, ctypes.c_int], ctypes.c_int),
            "GdipDrawImageRectI": ([ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int], ctypes.c_int),
            "GdipDeleteGraphics": ([ctypes.c_void_p], ctypes.c_int),
            "GdipDisposeImage": ([ctypes.c_void_p], ctypes.c_int),
        }
        for name, (arguments, result) in specifications.items():
            function = getattr(self.gdiplus, name)
            function.argtypes = arguments
            function.restype = result
        self.shlwapi.SHCreateMemStream.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
        self.shlwapi.SHCreateMemStream.restype = ctypes.c_void_p
        self.token = ctypes.c_size_t()
        code = self.gdiplus.GdiplusStartup(ctypes.byref(self.token), ctypes.byref(StartupInput(UI_GDIPLUS_VERSION, None, 0, 0)), None)
        if code or not self.token.value:
            raise OSError("Windows 图像引擎初始化失败：" + str(code))

    @staticmethod
    def ppm_from_bgr(pixels, width, height, stride):
        row_bytes = width * UI_RGB_CHANNELS
        if width < 1 or height < 1 or abs(stride) < row_bytes or len(pixels) < abs(stride) * height:
            raise ValueError("原生图像缓冲区尺寸无效")
        if stride == row_bytes:
            bgr = pixels[:row_bytes * height]
        else:
            row_order = range(height) if stride > 0 else range(height - 1, -1, -1)
            bgr = b"".join(pixels[row * abs(stride):row * abs(stride) + row_bytes] for row in row_order)
        rgb = bytearray(len(bgr))
        rgb[UI_RGB_RED_CHANNEL::UI_RGB_CHANNELS] = bgr[UI_RGB_BLUE_CHANNEL::UI_RGB_CHANNELS]
        rgb[UI_RGB_GREEN_CHANNEL::UI_RGB_CHANNELS] = bgr[UI_RGB_GREEN_CHANNEL::UI_RGB_CHANNELS]
        rgb[UI_RGB_BLUE_CHANNEL::UI_RGB_CHANNELS] = bgr[UI_RGB_RED_CHANNEL::UI_RGB_CHANNELS]
        return (f"P6\n{width} {height}\n{UI_RGB_MAX}\n").encode("ascii") + rgb

    def scale(self, png, target):
        width, height = target
        stride = ((width * UI_RGB_CHANNELS + UI_BITMAP_ROW_ALIGNMENT - 1) // UI_BITMAP_ROW_ALIGNMENT) * UI_BITMAP_ROW_ALIGNMENT
        pixels = ctypes.create_string_buffer(stride * height)
        contents = ctypes.create_string_buffer(png)
        stream = self.shlwapi.SHCreateMemStream(ctypes.cast(contents, ctypes.c_void_p), len(png))
        if not stream:
            raise OSError("无法读取安卓截图")
        source, destination, graphics = ctypes.c_void_p(), ctypes.c_void_p(), ctypes.c_void_p()
        try:
            operations = (
                lambda: self.gdiplus.GdipCreateBitmapFromStream(stream, ctypes.byref(source)),
                lambda: self.gdiplus.GdipCreateBitmapFromScan0(width, height, stride, UI_PIXEL_FORMAT_24BPP_RGB, ctypes.cast(pixels, ctypes.c_void_p), ctypes.byref(destination)),
                lambda: self.gdiplus.GdipGetImageGraphicsContext(destination, ctypes.byref(graphics)),
                lambda: self.gdiplus.GdipSetInterpolationMode(graphics, UI_INTERPOLATION_HIGH_QUALITY_BILINEAR),
                lambda: self.gdiplus.GdipDrawImageRectI(graphics, source, 0, 0, width, height),
            )
            for operation in operations:
                code = operation()
                if code:
                    raise OSError("Windows 图像缩放失败：" + str(code))
            return self.ppm_from_bgr(pixels.raw, width, height, stride)
        finally:
            if graphics.value:
                self.gdiplus.GdipDeleteGraphics(graphics)
            if destination.value:
                self.gdiplus.GdipDisposeImage(destination)
            if source.value:
                self.gdiplus.GdipDisposeImage(source)
            interface = ctypes.cast(stream, ctypes.POINTER(ctypes.POINTER(ctypes.c_void_p)))
            release = ctypes.WINFUNCTYPE(ctypes.c_ulong, ctypes.c_void_p)(interface.contents[UI_COM_RELEASE_INDEX])
            release(stream)

    def close(self):
        if self.token.value:
            self.gdiplus.GdiplusShutdown(self.token)
            self.token.value = 0


class UI_FrameRenderer:
    def __init__(self, log):
        self.log = log
        self.condition = threading.Condition()
        self.pending = None
        self.result = None
        self.closed = False
        self.thread = threading.Thread(target=self._run, daemon=True, name="AdaptiveGameDisplay")
        self.thread.start()

    def submit(self, png, number, captured, source_size, target_size, capture_started, geometry):
        request = {"png": png, "number": number, "captured": captured, "source_size": source_size, "target_size": target_size, "capture_started": capture_started, "geometry": dict(geometry)}
        with self.condition:
            if self.closed:
                return False
            self.pending = request
            self.condition.notify()
            return True

    def take(self):
        with self.condition:
            result = self.result
            self.result = None
            return result

    def discard_pending(self):
        with self.condition:
            self.pending = None

    def _run(self):
        scaler = None
        native_error = None
        if os.name == "nt":
            try:
                kernel = ctypes.WinDLL("kernel32", use_last_error=True)
                kernel.GetCurrentThread.restype = ctypes.c_void_p
                kernel.SetThreadPriority.argtypes = [ctypes.c_void_p, ctypes.c_int]
                kernel.SetThreadPriority.restype = ctypes.c_int
                kernel.SetThreadPriority(kernel.GetCurrentThread(), UI_THREAD_PRIORITY_BELOW_NORMAL)
            except (AttributeError, OSError):
                pass
            try:
                scaler = UI_WindowsImageScaler()
            except Exception as exc:
                native_error = str(exc)
                self.log("ui_native_scaler_unavailable", error=native_error)
        try:
            while True:
                with self.condition:
                    while self.pending is None and not self.closed:
                        self.condition.wait()
                    if self.closed:
                        return
                    request = self.pending
                    self.pending = None
                started = time.monotonic()
                result = {key: value for key, value in request.items() if key != "png"}
                result["format"] = "png"
                result["data"] = request["png"]
                if scaler is not None:
                    try:
                        result["data"] = scaler.scale(request["png"], request["target_size"])
                        result["format"] = "ppm"
                        native_error = None
                    except Exception as exc:
                        error = str(exc)
                        if error != native_error:
                            self.log("ui_native_scaler_error", error=error)
                        native_error = error
                result["seconds"] = time.monotonic() - started
                with self.condition:
                    if self.closed:
                        return
                    self.result = result
        finally:
            if scaler is not None:
                scaler.close()

    def close(self):
        with self.condition:
            self.closed = True
            self.pending = None
            self.result = None
            self.condition.notify_all()


class WindowsFileDrop:
    def __init__(self, window, target, callback):
        if os.name != "nt":
            raise OSError("仅支持 Windows 文件拖入")
        self.window = window
        self.callback = callback
        self.user32 = ctypes.WinDLL("user32", use_last_error=True)
        self.shell32 = ctypes.WinDLL("shell32", use_last_error=True)
        self._old_procs = {}
        self._proc_type = ctypes.WINFUNCTYPE(ctypes.c_ssize_t, ctypes.c_void_p, ctypes.c_uint, ctypes.c_size_t, ctypes.c_ssize_t)
        self._proc = self._proc_type(self._window_proc)
        self._proc_address = ctypes.cast(self._proc, ctypes.c_void_p).value
        self.user32.GetParent.argtypes = [ctypes.c_void_p]
        self.user32.GetParent.restype = ctypes.c_void_p
        self.user32.IsWindow.argtypes = [ctypes.c_void_p]
        self.user32.IsWindow.restype = ctypes.c_int
        self.user32.GetWindowLongPtrW.argtypes = [ctypes.c_void_p, ctypes.c_int]
        self.user32.GetWindowLongPtrW.restype = ctypes.c_void_p
        self.user32.SetWindowLongPtrW.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]
        self.user32.SetWindowLongPtrW.restype = ctypes.c_void_p
        self.user32.CallWindowProcW.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint, ctypes.c_size_t, ctypes.c_ssize_t]
        self.user32.CallWindowProcW.restype = ctypes.c_ssize_t
        self.shell32.DragAcceptFiles.argtypes = [ctypes.c_void_p, ctypes.c_int]
        self.shell32.DragAcceptFiles.restype = None
        self.shell32.DragQueryFileW.argtypes = [ctypes.c_void_p, ctypes.c_uint, ctypes.c_wchar_p, ctypes.c_uint]
        self.shell32.DragQueryFileW.restype = ctypes.c_uint
        self.shell32.DragFinish.argtypes = [ctypes.c_void_p]
        self.shell32.DragFinish.restype = None
        self._allow_message = getattr(self.user32, "ChangeWindowMessageFilterEx", None)
        if self._allow_message is not None:
            self._allow_message.argtypes = [ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint, ctypes.c_void_p]
            self._allow_message.restype = ctypes.c_int
        top = int(window.winfo_id())
        outer = int(self.user32.GetParent(top) or 0)
        canvas = int(target.winfo_id())
        try:
            for hwnd in dict.fromkeys((top, outer, canvas)):
                if not hwnd:
                    continue
                previous = self.user32.GetWindowLongPtrW(hwnd, UI_GWLP_WNDPROC)
                if not previous:
                    raise ctypes.WinError(ctypes.get_last_error())
                self._old_procs[hwnd] = previous
                updated = self.user32.SetWindowLongPtrW(hwnd, UI_GWLP_WNDPROC, self._proc_address)
                if not updated:
                    raise ctypes.WinError(ctypes.get_last_error())
                self.shell32.DragAcceptFiles(hwnd, 1)
                if self._allow_message is not None:
                    for message in (UI_WM_DROPFILES, UI_WM_COPYDATA, UI_WM_COPYGLOBALDATA):
                        self._allow_message(hwnd, message, UI_MSGFLT_ALLOW, None)
        except BaseException:
            self.close()
            raise

    def _window_proc(self, hwnd, message, wparam, lparam):
        if message == UI_WM_DROPFILES:
            files = []
            try:
                count = self.shell32.DragQueryFileW(wparam, UI_DROP_FILE_COUNT_QUERY, None, 0)
                for index in range(count):
                    length = self.shell32.DragQueryFileW(wparam, index, None, 0)
                    buffer = ctypes.create_unicode_buffer(length + 1)
                    self.shell32.DragQueryFileW(wparam, index, buffer, length + 1)
                    files.append(buffer.value)
            except Exception:
                files = []
            finally:
                self.shell32.DragFinish(wparam)
            if files:
                with contextlib.suppress(Exception):
                    self.window.after_idle(self.callback, tuple(files))
            return 0
        previous = self._old_procs.get(int(hwnd or 0))
        if previous:
            return self.user32.CallWindowProcW(previous, hwnd, message, wparam, lparam)
        return 0

    def close(self):
        for hwnd, previous in list(self._old_procs.items()):
            if self.user32.IsWindow(hwnd) and self.user32.GetWindowLongPtrW(hwnd, UI_GWLP_WNDPROC) == self._proc_address:
                self.shell32.DragAcceptFiles(hwnd, 0)
                self.user32.SetWindowLongPtrW(hwnd, UI_GWLP_WNDPROC, previous)
                if self._allow_message is not None:
                    for message in (UI_WM_DROPFILES, UI_WM_COPYDATA, UI_WM_COPYGLOBALDATA):
                        self._allow_message(hwnd, message, UI_MSGFLT_RESET, None)
        self._old_procs.clear()


UI_OVERLAY_LABEL_LIMIT = math.isqrt(AI_LABEL_FIELD_LIMIT)
UI_SMART_BUTTON_LABEL_LIMIT = AI_LABEL_FIELD_LIMIT // (AI_RGB_CHANNELS * AI_SPATIAL_DIMENSIONS)


UI_ACTION_SOURCE_LABELS = {
    "offline_game_layout": "离线游戏类型与触控布局假设",
    "accessibility_target": "安卓可访问控件",
    "accessibility_long_press": "安卓可访问长按控件",
    "accessibility_scroll": "安卓可访问滚动区域",
    "visual_region": "局部颜色/边缘区域",
    "visual_control_hold": "画面下方触控区域猜测",
    "visual_control_touch": "画面下方持续触控猜测",
    "visual_drag": "截图方位探索",
    "visual_exploration": "截图坐标探索",
    "visual_hold": "截图长按探索",
    "keyboard_gameplay": "方向键探索",
    "continuous_control_probe": "连续触控探索",
    "held_control_update": "更新已按住的触控方向",
    "held_control_observation": "保持当前触控并观察",
    "held_control_release": "释放持续触控",
    "simultaneous_control_probe": "多点触控探索",
    "loading_observation": "等待游戏加载",
    "observation": "等待获取可靠画面",
    "unknown_observation": "等待未知界面更新",
    "learned_control": "已执行动作记忆",
    "navigation_recovery": "菜单返回候选",
    "human_demonstration": "用户此前亲手操作的示教记录",
    "learned_affordance": "当前游戏跨画面已学控制热区",
    "opponent_turn_observation": "检测到对方回合，持续观测游戏",
}


UI_REWARD_SOURCE_LABELS = {"unknown": "尚未识别", "unavailable": "无可验证游戏奖励", "none": "无可验证游戏奖励", "intrinsic": "状态探索", "exploration": "状态探索", "score": "可核对成绩变化", "score_delta": "可核对成绩变化", "fresh_accessibility_score_delta": "新采集的可访问成绩变化", "fresh_accessibility_unavailable": "未取得新鲜界面证据", "distinct_fresh_accessibility_results": "不同时间采集的终局界面证据", "awaiting_distinct_fresh_accessibility_results": "等待第二份独立终局界面证据", "health": "可核对生命值变化", "terminal": "界面终局证据", "terminal_text": "界面终局文字", "visible_text": "可见界面文字", "accessibility": "可访问界面节点", "node_state": "界面节点状态变化"}


UI_LEARNING_MODE_LABELS = {"exploration": "探索未充分尝试的动作", "exploring": "探索未充分尝试的动作", "exploitation": "使用已有经验", "exploit": "使用已有经验", "ucb": "比较经验价值与探索加成", "ucb1": "比较经验价值与探索加成", "model_based": "依据已学状态转移规划", "planning": "依据已学状态转移规划", "learning": "在线学习", "reward_learning": "依据可验证奖励学习", "recovery": "恢复可用操作", "unknown_goal": "目标未知，收集状态变化"}


class Application:
    def __init__(self, window, root, supervised=False):
        from tkinter import font as tkfont
        self.window = window
        self.events = UIEventQueue()
        self.controller = Controller(root, self.events, supervised=supervised)
        self.closing = False
        self.photo = None
        self.scale = (1.0, 1.0)
        self.image_size = (1, 1)
        self.source_size = (1, 1)
        self.display_size = (1, 1)
        self.offset = (0, 0)
        self.last_frame_number = -1
        self.display_captured = 0.0
        self.display_capture_started = 0.0
        self.display_geometry = None
        self._input_geometry_changed_at = 0.0
        self._last_input_geometry = None
        self.last_render_key = None
        self.last_render_submit = 0.0
        self.points = {}
        self.manual_text_request = None
        self._poll_after = None
        self._layout_after = None
        self._flow_layouts = {}
        self._button_states = {}
        self._panel_layout = None
        self._dpi = None
        self._render_error = None
        self.preparation_stage = ""
        self._preparation_error = ""
        self._readiness_key = None
        self.progress_items = {}
        self._learning_values = {}
        self._learning_game = ""
        self._smart_overlay_enabled = True
        self._smart_plan = {}
        self._smart_overlay_signature = None
        self._smart_controls_signature = None
        self._smart_control_widgets = []
        self.scene_var = tk.StringVar(master=window, value="等待屏幕视觉区域和可访问控件")
        self.hover_var = tk.StringVar(master=window, value="将鼠标移到画面中的标注区域，可查看识别依据")
        self.status_var = tk.StringVar(master=window, value="正在检测本机游戏环境与本地学习器")
        self.state_var = tk.StringVar(master=window, value=UI_STATE_LABELS["PREPARING"])
        self.readiness_var = tk.StringVar(master=window, value="正在检测本机环境；截图、输入通道与实际决策全部通过后就绪")
        self.metrics_var = tk.StringVar(master=window, value="等待运行数据")
        self.input_var = tk.StringVar(master=window)
        self.resource_var = tk.StringVar(master=window, value="正在检测可用资源")
        self.insight_var = tk.StringVar(master=window, value="等待真实游戏画面；目标尚未识别")
        self.feedback_var = tk.StringVar(master=window, value="尚未获得本次游戏的结果反馈")
        self.learning_var = tk.StringVar(master=window, value="本机经验会随实际交互更新；尚无本次运行的学习记录")
        self.font = tkfont.nametofont("TkDefaultFont", root=window).copy()
        self.bold_font = self.font.copy()
        self.bold_font.configure(weight="bold")
        self.title_font = self.bold_font.copy()
        self.base_font_size = int(self.font.cget("size"))
        self.environment = UI_WindowEnvironment(window)
        self.base_font_dpi = self.environment.dpi()
        self.cadence = UI_AdaptiveCadence(self.environment.refresh_rate())
        self._measure_fonts()
        self.window.title(APP_NAME + " " + APP_VERSION)
        self.window.configure(bg=UI_COLORS["background"])
        self.window.protocol("WM_DELETE_WINDOW", self.close)
        self._build()
        self.window.update_idletasks()
        self._initial_geometry()
        self.renderer = UI_FrameRenderer(self.controller.log)
        self.file_drop = None
        if os.name == "nt":
            try:
                self.file_drop = WindowsFileDrop(self.window, self.canvas, self.dropped_files)
            except Exception as exc:
                self.controller.log("windows_drag_drop_unavailable", error=str(exc))
                self.status_var.set("文件拖入暂不可用，可点击安装 APK：" + str(exc))
        self.window.bind("<Configure>", self._window_resized, add="+")
        supervision = getattr(self.controller, "enable_supervision", None)
        if callable(supervision):
            supervision()
        self._queue_layout()
        self._poll_after = self.window.after_idle(self.poll)

    def _measure_fonts(self):
        dpi = self.environment.dpi()
        if dpi != self._dpi:
            self.window.tk.call("tk", "scaling", dpi / UI_POINTS_PER_INCH)
            size = self.base_font_size if self.base_font_size > 0 else -max(1, round(abs(self.base_font_size) * dpi / self.base_font_dpi))
            self.font.configure(size=size)
            self.bold_font.configure(size=size)
            title_size = max(1, round(abs(size) * UI_TITLE_FONT_SCALE))
            self.title_font.configure(size=title_size if self.base_font_size > 0 else -title_size)
            self._dpi = dpi
        self.line_height = max(1, self.font.metrics("linespace"))
        self.pad = max(1, math.ceil(self.line_height / UI_RECT_EDGE_COUNT))
        self.outer_pad = self.pad * UI_RECT_EDGE_COUNT
        self.glyph_width = max(1, self.font.measure("M"))

    def _button(self, parent, text, command, color=None):
        background = color or UI_COLORS["border"]
        return tk.Button(parent, text=text, command=command, bg=background, fg=UI_COLORS["text"], activebackground=background, activeforeground=UI_COLORS["text"], disabledforeground=UI_COLORS["muted"], relief="flat", borderwidth=0, font=self.font, padx=self.glyph_width, pady=self.pad, cursor="hand2")

    def _label(self, parent, variable=None, text="", color=None, bold=False):
        options = {"textvariable": variable} if variable is not None else {"text": text}
        return tk.Label(parent, **options, bg=parent.cget("bg"), fg=color or UI_COLORS["text"], font=self.bold_font if bold else self.font, anchor="w", justify="left", borderwidth=0)

    def _build(self):
        self.shell = tk.Frame(self.window, bg=UI_COLORS["background"])
        self.shell.pack(fill="both", expand=True, padx=self.outer_pad, pady=self.pad)
        self.rows = {name: index for index, name in enumerate(("header", "toolbar", "content", "manual", "footer"))}
        self.shell.columnconfigure(0, weight=1)
        self.shell.rowconfigure(self.rows["content"], weight=1)
        self.header = tk.Frame(self.shell, bg=UI_COLORS["background"])
        self.header.grid(row=self.rows["header"], column=0, sticky="ew")
        self.title_label = self._label(self.header, text=APP_NAME)
        self.title_label.configure(font=self.title_font)
        self.state_label = self._label(self.header, self.state_var, color=UI_COLORS["accent"])
        self.folder_button = self._button(self.header, "工作文件夹", self.open_folder)
        self.header_widgets = (self.title_label, self.state_label, self.folder_button)
        self.toolbar = tk.Frame(self.shell, bg=UI_COLORS["background"])
        self.toolbar.grid(row=self.rows["toolbar"], column=0, sticky="ew")
        self.green = self._button(self.toolbar, "启动", self.start, UI_COLORS["start"])
        self.red = self._button(self.toolbar, "结束", self.stop, UI_COLORS["stop"])
        self.blue = self._button(self.toolbar, "黑匣子", self.export_blackbox, UI_COLORS["export"])
        self.overlay_button = self._button(self.toolbar, "智能标注：开", self.toggle_smart_overlay)
        self.green.configure(state="disabled")
        self.red.configure(state="disabled")
        self.metrics_label = self._label(self.toolbar, self.metrics_var, color=UI_COLORS["muted"])
        self.toolbar_widgets = (self.green, self.red, self.blue, self.overlay_button, self.metrics_label)
        self.content = tk.Frame(self.shell, bg=UI_COLORS["background"])
        self.content.grid(row=self.rows["content"], column=0, sticky="nsew", pady=(0, self.pad))
        self.content.bind("<Configure>", lambda event: self._queue_layout())
        self.canvas = tk.Canvas(self.content, bg=UI_COLORS["screen"], highlightthickness=1, highlightbackground=UI_COLORS["border"], takefocus=True, width=1, height=1)
        self.image_item = self.canvas.create_image(0, 0, anchor="nw")
        self.stale_item = self.canvas.create_text(self.pad, self.pad, anchor="nw", fill=UI_COLORS["warning"], font=self.bold_font, state="hidden")
        self.canvas.create_text(0, 0, text="正在检测本机游戏环境\n截图、控制通道和本地学习器通过检查后可启动", fill=UI_COLORS["muted"], font=self.font, justify="center", tags="placeholder")
        self.canvas.bind("<Configure>", self.canvas_resized)
        for button, identifier in ((UI_MOUSE_LEFT, 0), (UI_MOUSE_RIGHT, 1)):
            self.canvas.bind(f"<ButtonPress-{button}>", lambda event, value=identifier: self.screen_down(event, value))
            self.canvas.bind(f"<B{button}-Motion>", lambda event, value=identifier: self.screen_move(event, value))
            self.window.bind(f"<ButtonRelease-{button}>", lambda event, value=identifier: self.screen_up(event, value), add="+")
        self.canvas.bind("<FocusOut>", self.release_manual)
        self.canvas.bind("<Motion>", self._show_hover_hint)
        self.canvas.bind("<Leave>", self._clear_hover_hint)
        self.canvas.bind("<KeyPress>", self.key_press)
        self.inspector = tk.Frame(self.content, bg=UI_COLORS["surface"])
        self.inspector.columnconfigure(0, weight=1)
        self.inspector.rowconfigure(0, weight=1)
        self.inspector_canvas = tk.Canvas(self.inspector, bg=UI_COLORS["surface"], highlightthickness=0, borderwidth=0, width=1, height=1, takefocus=True)
        self.inspector_canvas.grid(row=0, column=0, sticky="nsew")
        self.inspector_scroll = tk.Scrollbar(self.inspector, orient="vertical", command=self.inspector_canvas.yview)
        self.inspector_scroll.grid(row=0, column=1, sticky="ns")
        self.inspector_canvas.configure(yscrollcommand=self.inspector_scroll.set)
        self.inspector_body = tk.Frame(self.inspector_canvas, bg=UI_COLORS["surface"])
        self.inspector_window = self.inspector_canvas.create_window(0, 0, anchor="nw", window=self.inspector_body)
        self.inspector_canvas.bind("<Configure>", self._inspector_resized)
        self.inspector_body.bind("<Configure>", self._inspector_content_changed)
        self.panel_labels = []
        self.panel_headings = []
        for title, variable, color in (("运行状态", self.status_var, UI_COLORS["text"]), ("环境与控制权", self.readiness_var, UI_COLORS["accent"]), ("资源与速度", self.resource_var, UI_COLORS["muted"]), ("智能视觉地图", self.scene_var, UI_COLORS["ui_control"]), ("指向区域解释", self.hover_var, UI_COLORS["hypothesis"]), ("观察与动作选择", self.insight_var, UI_COLORS["text"]), ("可验证结果", self.feedback_var, UI_COLORS["accent"]), ("本地学习记录", self.learning_var, UI_COLORS["muted"])):
            heading = self._label(self.inspector_body, text=title, color=UI_COLORS["accent"], bold=True)
            heading.pack(fill="x", padx=self.pad, pady=(self.pad, 0))
            self.panel_headings.append(heading)
            label = self._label(self.inspector_body, variable, color=color)
            label.pack(fill="x", padx=self.pad, pady=(self.pad, self.pad))
            self.panel_labels.append(label)
            if variable is self.scene_var:
                self.smart_controls_frame = tk.Frame(self.inspector_body, bg=UI_COLORS["surface"])
                self.smart_controls_frame.pack(fill="x", padx=self.pad, pady=(0, self.pad))
            if variable is self.resource_var:
                self.resource_label = label
        self.progress_area = tk.Frame(self.inspector_body, bg=UI_COLORS["surface"])
        self.progress_caption = self._label(self.progress_area, color=UI_COLORS["accent"])
        self.progress_caption.pack(fill="x", pady=(0, self.pad))
        self.progress_track = tk.Frame(self.progress_area, height=max(1, self.line_height // UI_PROGRESS_BAR_HEIGHT_DIVISOR), bg=UI_COLORS["border"])
        self.progress_track.pack(fill="x")
        self.progress_track.pack_propagate(False)
        self.progress_fill = tk.Frame(self.progress_track, bg=UI_COLORS["progress"])
        self.progress_fill.place(x=0, y=0, relheight=1, relwidth=0)
        for widget in (self.inspector_canvas, self.inspector_body, self.progress_caption, *self.inspector_body.winfo_children()):
            widget.bind("<MouseWheel>", self._inspector_wheel)
        self.manual_area = tk.Frame(self.shell, bg=UI_COLORS["background"])
        self.manual_area.grid(row=self.rows["manual"], column=0, sticky="ew")
        self.navigation = tk.Frame(self.manual_area, bg=UI_COLORS["background"])
        self.manual_widgets = []
        for label, action in (("返回", "back"), ("主页", "home"), ("最近应用", "recents")):
            button = self._button(self.navigation, label, lambda value=action: self.controller.manual({"kind": value}))
            self.manual_widgets.append(button)
        self.install_button = self._button(self.navigation, "安装 APK / 拖入", self.install_apk)
        self.navigation_widgets = tuple(self.manual_widgets) + (self.install_button,)
        self.text_row = tk.Frame(self.manual_area, bg=UI_COLORS["background"])
        self.text_row.columnconfigure(0, weight=1)
        self.input_entry = tk.Entry(self.text_row, textvariable=self.input_var, bg=UI_COLORS["surface"], fg=UI_COLORS["text"], disabledbackground=UI_COLORS["surface"], disabledforeground=UI_COLORS["muted"], insertbackground=UI_COLORS["text"], relief="flat", font=self.font, width=len("请输入游戏文字"))
        self.input_entry.grid(row=0, column=0, sticky="ew", ipady=self.pad, pady=(0, self.pad))
        self.input_entry.bind("<Return>", lambda event: self.type_text())
        self.input_button = self._button(self.text_row, "输入", self.type_text)
        self.input_button.grid(row=0, column=1, sticky="ew", padx=(self.pad, 0), pady=(0, self.pad))
        self.manual_widgets.extend((self.input_entry, self.input_button))
        self.footer = tk.Frame(self.shell, bg=UI_COLORS["background"])
        self.footer.grid(row=self.rows["footer"], column=0, sticky="ew")
        self.footer_label = self._label(self.footer, text="本地 AI 决策 · 首次安装安卓环境需联网 · APK 支持拖入 · 结束即交还游戏控制权", color=UI_COLORS["muted"])
        self.license_link = self._label(self.footer, text="能力说明", color=UI_COLORS["accent"])
        self.license_link.configure(cursor="hand2")
        self.license_link.bind("<Button-1>", lambda event: self.open_licenses())
        self.footer_widgets = (self.footer_label, self.license_link)
        for widget in self.manual_widgets:
            widget.configure(state="disabled")

    def _initial_geometry(self):
        left, top, work_width, work_height = self.environment.work_area()
        margin = self.outer_pad * UI_RECT_EDGE_COUNT
        width = max(1, min(work_width - margin, round(work_width * UI_INITIAL_WINDOW_SHARE)))
        height = max(1, min(work_height - margin, round(work_height * UI_INITIAL_WINDOW_SHARE)))
        x = left + (work_width - width) // UI_RECT_EDGE_COUNT
        y = top + (work_height - height) // UI_RECT_EDGE_COUNT
        self.window.geometry(f"{width}x{height}{x:+d}{y:+d}")
        self._set_minimum_size(work_width, work_height)

    def _set_minimum_size(self, work_width, work_height):
        minimum_width = sum(widget.winfo_reqwidth() for widget in (self.green, self.red, self.blue)) + self.pad * len(self.toolbar_widgets) + self.outer_pad * UI_RECT_EDGE_COUNT
        controls = (self.header, self.toolbar, self.manual_area, self.footer)
        minimum_height = sum(max(self.line_height, widget.winfo_reqheight()) for widget in controls) + self.line_height * len(self.rows)
        self.window.minsize(min(work_width, minimum_width), min(work_height, minimum_height))

    def _window_resized(self, event):
        if event.widget is self.window:
            self._queue_layout()

    def _queue_layout(self):
        if not self.closing and self._layout_after is None:
            self._layout_after = self.window.after_idle(self._layout)

    def _flow(self, container, widgets, width):
        width = max(1, int(width))
        positions = []
        top, used, row_height = 0, 0, 0
        for widget in widgets:
            needed = min(width, max(1, widget.winfo_reqwidth()))
            if used and used + needed > width:
                top += row_height + self.pad
                used = 0
                row_height = 0
            height = max(1, widget.winfo_reqheight())
            positions.append((widget, used, top, needed, height))
            used += needed + self.pad
            row_height = max(row_height, height)
        total_height = top + row_height + self.pad
        signature = (width, total_height, tuple((str(widget), x, y, item_width, item_height) for widget, x, y, item_width, item_height in positions))
        if self._flow_layouts.get(container) != signature:
            container.configure(width=width, height=total_height)
            for widget, x, y, item_width, item_height in positions:
                widget.place(x=x, y=y, width=item_width, height=item_height)
            self._flow_layouts[container] = signature

    @staticmethod
    def fit_size(source, bounds):
        source_width, source_height = source
        width, height = bounds
        if min(source_width, source_height, width, height) < 1:
            return 1, 1
        ratio = min(1.0, width / source_width, height / source_height)
        return max(1, int(source_width * ratio)), max(1, int(source_height * ratio))

    def _layout(self):
        self._layout_after = None
        if self.closing:
            return
        previous_dpi = self._dpi
        self._measure_fonts()
        if previous_dpi != self._dpi:
            self.cadence.refresh_rate = self.environment.refresh_rate()
            self.shell.pack_configure(padx=self.outer_pad, pady=self.pad)
            self.content.grid_configure(pady=(0, self.pad))
            for widget in (self.folder_button, self.green, self.red, self.blue, self.install_button, self.input_button, *self.manual_widgets):
                if isinstance(widget, tk.Button):
                    widget.configure(padx=self.glyph_width, pady=self.pad)
            self.input_entry.grid_configure(ipady=self.pad, pady=(0, self.pad))
            self.input_button.grid_configure(padx=(self.pad, 0), pady=(0, self.pad))
            for label in self.panel_labels:
                label.pack_configure(padx=self.pad, pady=(self.pad, self.pad))
            for heading in self.panel_headings:
                heading.pack_configure(padx=self.pad, pady=(self.pad, 0))
            self.progress_caption.pack_configure(pady=(0, self.pad))
            self.progress_track.configure(height=max(1, self.line_height // UI_PROGRESS_BAR_HEIGHT_DIVISOR))
            if self.progress_area.winfo_manager():
                self.progress_area.pack_configure(padx=self.pad, pady=(0, self.pad))
            self._flow_layouts.clear()
        width = max(1, self.window.winfo_width() - self.outer_pad * UI_RECT_EDGE_COUNT)
        for label in (self.title_label, self.metrics_label, self.footer_label):
            label.configure(wraplength=max(1, width - self.pad))
        self._flow(self.header, self.header_widgets, width)
        self._flow(self.toolbar, self.toolbar_widgets, width)
        self._flow(self.footer, self.footer_widgets, width)
        navigation_width = sum(widget.winfo_reqwidth() + self.pad for widget in self.navigation_widgets)
        text_width = self.font.measure("请输入游戏文字") + self.input_button.winfo_reqwidth() + self.pad
        inline = navigation_width + text_width <= width
        self.manual_area.columnconfigure(0, weight=0 if inline else 1)
        self.manual_area.columnconfigure(1, weight=1 if inline else 0)
        self.navigation.grid(row=0, column=0, sticky="ew")
        self.text_row.grid(row=0 if inline else 1, column=1 if inline else 0, sticky="ew")
        self._flow(self.navigation, self.navigation_widgets, navigation_width if inline else width)
        self._layout_panel()
        _, _, work_width, work_height = self.environment.work_area()
        self._set_minimum_size(work_width, work_height)

    def _layout_panel(self):
        width = max(1, self.content.winfo_width())
        height = max(1, self.content.winfo_height())
        panel_width = self.font.measure("正在根据当前设备调整学习与操作") + self.outer_pad + self.inspector_scroll.winfo_reqwidth()
        panel_height = sum(self.font.metrics("linespace") for _ in self.panel_labels) + self.outer_pad * UI_RECT_EDGE_COUNT
        source = self.source_size if self.source_size != (1, 1) else (width, height)
        side_bounds = (max(1, width - panel_width - self.pad), height)
        stacked_bounds = (width, max(1, height - panel_height - self.pad))
        side_size = self.fit_size(source, side_bounds)
        stacked_size = self.fit_size(source, stacked_bounds)
        beside = width >= panel_width + self.font.measure("安卓游戏画面") and math.prod(side_size) >= math.prod(stacked_size)
        layout = (beside, panel_width, panel_height, self.pad)
        if self._panel_layout == layout:
            return
        self._panel_layout = layout
        self.content.rowconfigure(0, weight=1)
        self.content.rowconfigure(1, weight=0, minsize=0 if beside else panel_height)
        self.content.columnconfigure(0, weight=1)
        self.content.columnconfigure(1, weight=0, minsize=panel_width if beside else 0)
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.inspector.grid(row=0 if beside else 1, column=1 if beside else 0, sticky="nsew", padx=(self.pad, 0) if beside else 0, pady=0 if beside else (self.pad, 0))
        self.inspector.configure(width=panel_width, height=panel_height)
        self.inspector.grid_propagate(False)
        self.last_render_key = None

    def _inspector_resized(self, event):
        self.inspector_canvas.itemconfigure(self.inspector_window, width=max(1, event.width))
        wrap = max(1, event.width - self.pad * UI_RECT_EDGE_COUNT)
        for label in self.panel_labels + [self.progress_caption]:
            label.configure(wraplength=wrap)

    def _inspector_content_changed(self, event):
        self.inspector_canvas.configure(scrollregion=self.inspector_canvas.bbox("all"))

    def _inspector_wheel(self, event):
        if event.delta:
            steps = -int(math.copysign(max(1, abs(event.delta) // UI_MOUSE_WHEEL_DELTA), event.delta))
            self.inspector_canvas.yview_scroll(steps, "units")
        return "break"

    def _set_button_state(self, widget, enabled):
        state = "normal" if enabled else "disabled"
        if self._button_states.get(widget) != state:
            widget.configure(state=state)
            self._button_states[widget] = state

    def _display_readiness(self, state, checks):
        ready = self.controller.ready_seconds
        elapsed = max(0.0, time.monotonic() - self.controller._startup_clock)
        capabilities = self._input_capabilities()
        reason = next((str(value) for value in (getattr(self.controller, "environment_error", ""), getattr(self.controller, "blocked_reason", ""), getattr(self.controller, "preparation_error", ""), self._preparation_error) if value), "")
        profile = self.controller._startup_diagnostics()
        stage_signature = tuple((name, value.get("state"), value.get("seconds"), str(value.get("error", ""))) for name, value in profile.items() if isinstance(value, dict))
        runtime = self.controller.android
        device = (runtime.serial, runtime.owned, capabilities.get("input_backend"))
        check_signature = tuple((name, checks.get(name) is True) for name in UI_READINESS_CHECK_LABELS)
        key = (state, math.floor(elapsed) if ready is None or state in {"PREPARING", "RECOVERING", "BLOCKED", "UNAVAILABLE"} else ready, reason, stage_signature, check_signature, device, capabilities.get("touch_slots"), capabilities.get("buffered_manual_gestures"))
        if key == self._readiness_key:
            return
        self._readiness_key = key
        if ready is None:
            lines = [f"检测与准备已用 {elapsed:.1f} 秒"]
        else:
            lines = [f"首次完整就绪 {ready:.1f} 秒"]
        if runtime.serial:
            scope = "本程序独立模拟器" if runtime.owned else "已连接本地模拟器"
            lines.append("目标设备：" + scope + " · " + str(runtime.serial))
        backend = capabilities.get("input_backend")
        if backend:
            mode = {"emulator_console": "模拟器连续多点触控", "adb_motionevent": "系统连续单指触控", "adb_gesture": "系统单指手势", "unavailable": "等待设备输入通道"}.get(backend, str(backend))
            lines.append("输入方式：" + mode)
        lines.append(" · ".join(label + ("已通过" if checks.get(name) is True else "待验证") for name, label in UI_READINESS_CHECK_LABELS.items()))
        for stage in dict.fromkeys((*UI_PREPARATION_LABELS, *profile)):
            value = profile.get(stage, {})
            if not isinstance(value, dict):
                continue
            if state not in {"PREPARING", "RECOVERING", "BLOCKED", "UNAVAILABLE"} and not value:
                continue
            status = UI_PREPARATION_STATES.get(value.get("state"), "等待依赖")
            seconds = value.get("seconds")
            if value.get("state") == "working" and type(value.get("started_seconds")) in (int, float):
                seconds = max(0.0, elapsed - value["started_seconds"])
            suffix = f" · {seconds:.1f} 秒" if type(seconds) in (int, float) and math.isfinite(seconds) else ""
            lines.append(UI_PREPARATION_LABELS.get(stage, stage) + "：" + status + suffix)
            if value.get("error"):
                lines.append(str(value["error"]))
        if state in {"PREPARING", "RECOVERING", "BLOCKED", "UNAVAILABLE"}:
            if reason:
                lines.append("尚未就绪的原因：" + reason)
            if state == "RECOVERING":
                lines.append("接管请求仍有效；正在恢复设备连接，可点击结束")
            elif state in {"BLOCKED", "UNAVAILABLE"}:
                lines.append("后台继续检查本机环境，条件满足后自动完成准备")
        elif state == "READY":
            if all(checks.get(name) is True for name in UI_READINESS_CHECK_LABELS):
                lines.append("本程序游戏视图：用户可操作")
            if capabilities.get("buffered_manual_gestures"):
                lines.append("当前设备手势在鼠标松开后发送")
            slots = capabilities.get("touch_slots")
            if type(slots) is int and slots > 0:
                lines.append("当前设备可用触点：" + str(slots))
        elif state == "RUNNING":
            lines.append("本程序游戏视图：Agent 接管，手动输入已禁用")
            if getattr(self.controller.android, "_external", False):
                lines.append("当前复用外部模拟器；其原生窗口的鼠标键盘输入不属于本程序控制范围")
            lines.append("桌面其他应用保持可用；点击结束交还游戏控制权")
        elif state == "STOPPING":
            lines.append("正在取消决策并释放触点，完成后恢复本程序手动输入")
        self.readiness_var.set("\n".join(lines))
        if self.photo is None and state in {"PREPARING", "BLOCKED", "UNAVAILABLE"}:
            message = "正在检测本机游戏环境" if not reason else "本机游戏环境尚未就绪\n" + reason
            self.canvas.itemconfigure("placeholder", text=message, state="normal")

    def _sync_controls(self):
        state = self.controller.operation_state()
        label = UI_STATE_LABELS.get(state, state)
        checks = self.controller.readiness_checks()
        self._display_readiness(state, checks)
        if self.state_var.get() != label:
            self.state_var.set(label)
            self.state_label.configure(fg=UI_COLORS["warning"] if state in {"RECOVERING", "BLOCKED", "UNAVAILABLE"} else UI_COLORS["accent"])
            self._queue_layout()
        self._set_button_state(self.green, state == "READY" and all(checks.get(name) is True for name in UI_READINESS_CHECK_LABELS) and not bool(getattr(self.controller, "_pending_installs", None)))
        self._set_button_state(self.red, state != "STOPPING" and bool(self.controller.desired_running or self.controller.resume_requested))
        self._set_button_state(self.blue, state != "CLOSED" and not self.controller.exporting)
        self._set_button_state(self.folder_button, state != "CLOSED")
        self._set_button_state(self.overlay_button, state != "CLOSED")
        self._set_button_state(self.install_button, self.controller.can_install())
        manual = self.controller.manual_authorized()
        for widget in self.manual_widgets:
            self._set_button_state(widget, manual and (widget is not self.input_button or self.manual_text_request is None))
        for widget in self._smart_control_widgets:
            self._set_button_state(widget, manual)
        if not manual:
            self.points.clear()
        return state

    def start(self):
        self.release_manual()
        self.controller.start()
        self._sync_controls()

    def stop(self):
        self.controller.stop()
        self._sync_controls()

    def export_blackbox(self):
        self.controller.export()
        self._sync_controls()

    def open_folder(self):
        try:
            os.startfile(str(self.controller.root))
        except Exception as exc:
            self.status_var.set(str(exc))

    def open_licenses(self):
        messagebox.showinfo("通用游戏 Agent · 能力说明", "程序使用本机截图、像素区域检测与可访问界面生成动作、对照结果并更新本地经验，不下载或调用外部 AI 模型。\n\n只有可验证的界面成绩或胜负信息才记为外部奖励；未识别目标时显示探索状态。探索反馈、动作置信信息均不代表游戏胜率。\n\nAPK 需要 Android 运行环境；本程序优先复用本机组件，缺失时通过 HTTPS 自动下载官方模拟器、ADB 和系统镜像，并执行 SHA 校验。首次下载需要网络、足够的磁盘空间；模拟器还依赖 Windows 虚拟化支持。Google 官方 Android SDK 受其软件许可条款约束。环境不可用时会显示真实原因，启动按钮保持禁用。\n\n接管范围是本程序游戏视图，桌面其他应用保持可用。黑匣子包含运行日志、学习记录和游戏截图。\n\n该实现提供通用交互与在线学习，未验证任意游戏达到或超过职业玩家水平。", parent=self.window)

    def dropped_files(self, paths):
        if not self.controller.can_install():
            self.status_var.set("Agent 接管期间不能安装游戏，点击结束后可导入")
            return
        try:
            files = selected_apk_files(paths)
        except (OSError, TypeError, ValueError) as exc:
            self.status_var.set("拖入的文件必须是 APK：" + str(exc))
            return
        self.release_manual()
        if self.controller.install(files):
            self.status_var.set("已接收 APK；本机环境可用后自动安装：" + "、".join(file.name for file in files))
        self._sync_controls()

    def install_apk(self):
        if not self.controller.can_install():
            return
        self.release_manual()
        paths = filedialog.askopenfilenames(parent=self.window, title="选择游戏 APK（多个独立应用或完整拆分包）", filetypes=[("Android 游戏安装包", "*.apk")])
        if paths:
            self.dropped_files(paths)

    def type_text(self):
        text = self.input_var.get()
        if not text or self.manual_text_request is not None:
            return "break"
        request_id = uuid.uuid4().hex
        if self.controller.manual({"kind": "type", "text": text}, request_id):
            self.manual_text_request = (request_id, text)
            self._sync_controls()
        return "break"

    def canvas_resized(self, event):
        self.last_render_key = None
        self.canvas.coords("placeholder", event.width // UI_RECT_EDGE_COUNT, event.height // UI_RECT_EDGE_COUNT)
        self.canvas.itemconfigure("placeholder", width=max(1, event.width - self.outer_pad))
        self.canvas.coords(self.stale_item, self.pad, self.pad)
        self.canvas.itemconfigure(self.stale_item, width=max(1, event.width - self.outer_pad))

    def _screen_point(self, event):
        local_x, local_y = event.x - self.offset[0], event.y - self.offset[1]
        if not (0 <= local_x < self.display_size[0] and 0 <= local_y < self.display_size[1]):
            return None
        width, height = self.image_size
        return min(width - 1, int(local_x * self.scale[0])), min(height - 1, int(local_y * self.scale[1]))

    def _input_geometry(self):
        runtime = self.controller.android
        with runtime._geometry_lock:
            return {"serial": runtime.serial, "size": tuple(runtime.screen_size()), "rotation": runtime._display_rotation, "generation": runtime._geometry_changes, "pending": bool(runtime._input_backend == "emulator_console" and runtime._geometry_dirty)}

    def _manual_frame_issue(self):
        if self.photo is None:
            return "正在等待首幅游戏画面"
        geometry = self._input_geometry()
        if geometry != self.display_geometry or geometry["pending"] or tuple(self.image_size) != geometry["size"] or self.display_capture_started < self._input_geometry_changed_at:
            return "设备或画面方向已变化，等待新截图后恢复坐标输入"
        if self.display_captured <= 0 or time.monotonic() - self.display_captured > self.cadence.stale_after(self.controller.capture_seconds):
            return "显示画面正在更新，等待新截图后恢复坐标输入"
        return ""

    def _input_capabilities(self):
        runtime = getattr(self.controller, "android", None)
        reader = getattr(runtime, "capabilities", None)
        if callable(reader):
            try:
                value = reader()
                return value if isinstance(value, dict) else {}
            except (AttributeError, TypeError, ValueError, RuntimeError):
                return {}
        return {}

    def screen_down(self, event, identifier=0):
        if not self.controller.manual_authorized() or self.photo is None:
            return "break"
        issue = self._manual_frame_issue()
        if issue:
            self.release_manual()
            self.status_var.set(issue)
            return "break"
        slots = self._input_capabilities().get("touch_slots")
        if type(slots) is int and (identifier >= slots or identifier not in self.points and len(self.points) >= slots):
            self.status_var.set("当前设备可用触点：" + str(slots))
            return "break"
        point = self._screen_point(event)
        if point is None:
            return "break"
        self.canvas.focus_set()
        self.points[identifier] = {"id": identifier, "x": point[0], "y": point[1]}
        self.controller.manual_touch(list(self.points.values()))
        return "break"

    def screen_move(self, event, identifier=0):
        if identifier not in self.points or not self.controller.manual_authorized():
            return "break"
        issue = self._manual_frame_issue()
        if issue:
            self.release_manual()
            self.status_var.set(issue)
            return "break"
        point = self._screen_point(event)
        if point is not None:
            self.points[identifier] = {"id": identifier, "x": point[0], "y": point[1]}
            self.controller.manual_touch(list(self.points.values()))
        return "break"

    def screen_up(self, event, identifier=0):
        if identifier in self.points:
            self.points.pop(identifier, None)
            self.controller.manual_touch(list(self.points.values()))

    def release_manual(self, event=None):
        if self.points:
            self.points.clear()
            self.controller.manual_touch([])

    def key_press(self, event):
        if not self.controller.manual_authorized():
            return "break"
        keys = {"Up": "DPAD_UP", "Down": "DPAD_DOWN", "Left": "DPAD_LEFT", "Right": "DPAD_RIGHT", "Return": "ENTER", "space": "SPACE", "Escape": "BACK", "BackSpace": "DEL", "Tab": "TAB"}
        key = keys.get(event.keysym)
        if key is None and len(event.keysym) == 1 and event.keysym.isascii() and event.keysym.isalnum():
            key = event.keysym.upper()
        if key is not None:
            self.controller.manual({"kind": "keyevent", "text": "KEYCODE_" + key})
            return "break"

    def _show_progress(self):
        if not self.progress_area.winfo_manager():
            self.progress_area.pack(before=self.resource_label, fill="x", padx=self.pad, pady=(0, self.pad))

    def update_progress(self, value):
        self._show_progress()
        state = str(value.get("state", ""))
        stages = {"discover": "本机检测", "extract": "本地解压", "verify": "校验", "install": "安装", "boot": "启动设备", "copy": "保存导入文件", "prepare": "准备", "learning": "初始化学习器"}
        stage = stages.get(str(value.get("stage", "")), "本地准备")
        name = str(value.get("name", ""))
        current = max(0, int(value.get("current", 0)))
        total = max(0, int(value.get("total", 0)))
        now = time.monotonic()
        identity = (stage, name)
        previous = self.progress_items.get(identity, {})
        rate = value.get("bytes_per_second", 0.0)
        rate = float(rate) if isinstance(rate, (int, float)) and math.isfinite(rate) and rate > 0 else 0.0
        delta = now - previous.get("updated", now)
        if not rate and state == "working" and previous and current >= previous["current"] and delta > 0:
            rate = (current - previous["current"]) / delta
            previous_delta = previous.get("interval", 0.0)
            if previous.get("rate", 0.0) > 0 and previous_delta > 0:
                rate = (previous["rate"] * previous_delta + rate * delta) / (previous_delta + delta)
        if state in {"retrying", "failed", "verifying"} or current < previous.get("current", 0):
            rate = 0.0
        if state == "complete" and total:
            current = total
        self.progress_items = {key: item for key, item in self.progress_items.items() if item["state"] in {"working", "verifying", "retrying"} or key == identity}
        self.progress_items[identity] = {"current": current, "total": total, "updated": now, "state": state, "rate": rate, "interval": delta}
        active = [item for item in self.progress_items.values() if item["state"] in {"working", "verifying", "retrying"}]
        ratio = min(1.0, current / total) if total else 0.0
        prefix = self.preparation_stage + "\n" if self.preparation_stage else ""
        if len(active) > 1:
            known = [item for item in active if item["total"]]
            amount = sum(min(item["current"], item["total"]) for item in known)
            overall = sum(item["total"] for item in known)
            ratio = amount / overall if overall else 0.0
            speed = sum(item["rate"] for item in active if item["state"] == "working")
            caption = f"并行准备 {len(active)} 项"
            if overall:
                caption += f" · 已知大小 {amount / UI_BYTES_PER_MIB:.1f} / {overall / UI_BYTES_PER_MIB:.1f} MiB"
            if speed:
                caption += f" · {speed / UI_BYTES_PER_MIB:.2f} MiB/s"
            caption += "\n" + name
        elif state == "verifying":
            caption = "正在校验 " + name
        elif state == "retrying":
            caption = "正在重新检测本机环境\n" + name
        elif state == "failed":
            caption = "当前文件准备失败，正在自动恢复\n" + name
        elif state == "complete":
            caption = "已完成" + stage + "\n" + name
            ratio = 1.0
        elif total:
            caption = f"{name}\n{stage} {ratio:.1%} · {current / UI_BYTES_PER_MIB:.1f} / {total / UI_BYTES_PER_MIB:.1f} MiB"
            if rate:
                caption += f" · {rate / UI_BYTES_PER_MIB:.2f} MiB/s"
                remaining = max(0.0, (total - current) / rate)
                caption += f" · 约 {math.ceil(remaining)} 秒" if remaining < UI_SECONDS_PER_MINUTE else f" · 约 {math.ceil(remaining / UI_SECONDS_PER_MINUTE)} 分钟"
        else:
            caption = f"正在{stage} {name}"
            if current:
                caption += f"\n已处理 {current / UI_BYTES_PER_MIB:.1f} MiB"
        self.progress_caption.configure(text=prefix + caption)
        self.progress_fill.place_configure(relwidth=ratio)

    def _display_resources(self, value):
        self.cadence.resources(value)
        lines = []
        cpu = value.get("cpu_percent")
        if isinstance(cpu, (int, float)) and math.isfinite(cpu):
            lines.append(f"整机 CPU {cpu:.0f}%")
        free = value.get("free_mb")
        if isinstance(free, (int, float)) and math.isfinite(free):
            lines.append(f"可用内存 {free / UI_MIB_PER_GIB:.1f} GiB")
        lines.append("本地决策：单个 CPU 执行通道")
        allocated = value.get("android_mb")
        if type(allocated) in (int, float) and math.isfinite(allocated) and allocated > 0:
            lines.append(f"安卓分配 {allocated / UI_MIB_PER_GIB:.1f} GiB")
        runtime = self.controller.android
        if runtime.owned:
            renderer = {"host": "主机图形", "auto": "自动", "software": "软件"}.get(runtime.gpu_mode, runtime.gpu_mode)
            lines.append("模拟器图形配置：" + str(renderer))
        elif runtime.serial:
            lines.append("图形与内存沿用已连接模拟器")
        if value.get("yielding"):
            lines.append("正在让出资源给其他应用")
        ready = value.get("ready_seconds")
        lines.append(f"准备耗时 {ready:.1f}s" if isinstance(ready, (int, float)) and math.isfinite(ready) else f"自动准备已用 {time.monotonic() - self.controller._startup_clock:.0f}s")
        adaptive = value.get("adaptive")
        if isinstance(adaptive, dict):
            capture, inference = adaptive.get("capture_seconds"), adaptive.get("plan_seconds")
            if isinstance(capture, (int, float)) and math.isfinite(capture):
                lines.append(f"截图 {capture:.2f}s")
            if isinstance(inference, (int, float)) and math.isfinite(inference):
                lines.append(f"决策 {inference:.2f}s")
        if self.cadence.samples.get("paint"):
            lines.append(f"显示 {self.cadence.typical('paint') * UI_MILLISECONDS_PER_SECOND:.0f}ms · 随负载调整刷新")
        self.resource_var.set(" · ".join(lines))

    def _update_smart_controls(self, scene):
        choices = []
        for item in scene if isinstance(scene, list) else ():
            if not isinstance(item, dict) or item.get("source") != "accessibility" or item.get("enabled") is False:
                continue
            reference = str(item.get("node_ref", ""))
            if not reference or any(old[0] == reference for old in choices):
                continue
            label = re.sub(r"\s+", " ", str(item.get("label") or "可交互控件")).strip()[:UI_SMART_BUTTON_LABEL_LIMIT]
            choices.append((reference, label, str(item.get("package", "")), str(item.get("activity", ""))))
        signature = tuple(choices)
        if signature == self._smart_controls_signature:
            return
        self._smart_controls_signature = signature
        for widget in self.smart_controls_frame.winfo_children():
            widget.destroy()
        self._smart_control_widgets.clear()
        for reference, label, package, activity in choices:
            widget = self._button(self.smart_controls_frame, "原生按钮 · " + label, lambda value=reference, game=package, window=activity: self.controller.manual({"kind": "tap", "target": value, "target_package": game, "target_activity": window}))
            widget.pack(fill="x", pady=(0, self.pad))
            widget.bind("<MouseWheel>", self._inspector_wheel)
            self._smart_control_widgets.append(widget)
        if not choices:
            widget = self._label(self.smart_controls_frame, text="当前没有可访问的原生按钮，仍可直接操作游戏画面", color=UI_COLORS["muted"])
            widget.pack(fill="x")
            widget.bind("<MouseWheel>", self._inspector_wheel)
        self._queue_layout()

    def _display_plan(self, value):
        self._smart_plan = {"scene_graph": value.get("scene_graph", []), "actions": value.get("actions", []), "screen_size": value.get("screen_size", [])}
        self._update_smart_controls(value.get("scene_graph", []))
        self._smart_overlay_signature = None
        scene = value.get("scene_graph", [])
        if isinstance(scene, list):
            controls = sum(isinstance(item, dict) and item.get("source") == "accessibility" for item in scene)
            learned_controls = sum(isinstance(item, dict) and item.get("source") == "learned_affordance" for item in scene)
            moving = sum(isinstance(item, dict) and item.get("kind") == "motion_target" for item in scene)
            vision = sum(isinstance(item, dict) and item.get("source") in {"local_visual", "local_attention"} for item in scene)
            hypotheses = sum(isinstance(item, dict) and item.get("source") == "layout_hypothesis" for item in scene)
            self.scene_var.set(f"原生控件 {controls} · 跨场景已学热区 {learned_controls} · 视觉候选 {vision} · 运动候选 {moving} · 布局推测 {hypotheses}\n青色：系统控件 · 蓝色：已学触控 · 黄色：画面候选 · 紫色虚线：布局推测 · 红色：下一动作\n已学热区只证明曾有反馈，不代表已理解游戏目标")
        phase = UI_PHASE_LABELS.get(value.get("phase"), str(value.get("phase", "")))
        game = str(value.get("game", ""))
        if game and game != self._learning_game:
            self._learning_game = game
            self._learning_values.clear()
        lines = [" · ".join(item for item in (game, phase) if item)]
        profile = value.get("game_profile")
        if isinstance(profile, dict):
            evidence = {"package_layout_hint": "游戏包名推测", "package_hint_plus_visual_regions": "包名与局部视觉线索", "visual_control_regions": "屏幕区域分布推测", "unclassified_gameplay": "无可靠玩法证据"}.get(profile.get("evidence"), "本地布局推测")
            lines.append("玩法画像（不等于理解规则）：" + str(profile.get("label", "待识别")) + " · " + evidence)
        task = value.get("task_state")
        objective = value.get("objective") or value.get("goal") or (task.get("goal") if isinstance(task, dict) else None)
        if isinstance(objective, dict):
            objective = objective.get("description") or objective.get("goal")
        if objective:
            lines.append("当前目标：" + str(objective))
        else:
            lines.append("目标尚未识别；探索结果与游戏成绩分开记录")
        if isinstance(task, dict):
            turn_labels = {"self": "当前由己方行动", "opponent": "当前由对方行动", "simultaneous": "双方同时行动", "unknown": "行动方待识别"}
            if task.get("turn") in turn_labels:
                lines.append(turn_labels[task["turn"]])
        actions = value.get("actions", [])
        actions = actions if isinstance(actions, list) else []
        description = value.get("assessment")
        if description:
            lines.append("观察依据：" + str(description))
        chosen = "、".join(self._action_summary(action) for action in actions if isinstance(action, dict))
        if chosen:
            lines.append("所选动作：" + chosen)
        if value.get("expected"):
            lines.append("待验证预期：" + str(value["expected"]))
        confidence = value.get("reported_confidence", value.get("confidence"))
        if value.get("confidence_kind") == "action_sample_support" and type(confidence) in (int, float) and math.isfinite(confidence) and 0 <= confidence <= 1:
            lines.append(f"动作样本支持度 {confidence:.0%}（尝试次数形成的统计量）")
        learned = value.get("learned_strategy")
        if isinstance(learned, dict):
            learned = learned.get("description") or learned.get("summary")
        if learned:
            lines.append("经验参考：" + str(learned))
        selection = value.get("selection") or value.get("policy_evidence")
        if isinstance(selection, dict):
            mode = selection.get("mode")
            if mode:
                lines.append("选择方式：" + UI_LEARNING_MODE_LABELS.get(mode, str(mode)))
            action_source = selection.get("action_source")
            if action_source:
                lines.append("动作依据：" + UI_ACTION_SOURCE_LABELS.get(str(action_source), str(action_source)))
            if selection.get("goal_known") is False:
                lines.append("没有已验证的游戏目标信号；当前为探索")
            if selection.get("cross_scene_control_matches"):
                lines.append("跨场景经验：匹配 " + str(selection["cross_scene_control_matches"]) + " 个控制热区；由执行效果更新")
            if local_agent_number(selection.get("recurrent_state_similarity")):
                lines.append("历史画面最高相似度：" + f"{selection['recurrent_state_similarity']:.1%}")
            self._display_learning(selection)
        self.insight_var.set("\n".join(line for line in lines if line))
        learning = value.get("learning")
        if isinstance(learning, dict):
            self._display_learning(learning)
        feedback = value.get("feedback")
        if isinstance(feedback, dict):
            self._display_feedback(feedback)

    @staticmethod
    def _action_summary(action):
        kind = str(action.get("kind", ""))
        label = UI_ACTION_LABELS.get(kind, kind)
        if all(type(action.get(axis)) in (int, float) and math.isfinite(action[axis]) for axis in ("x", "y")):
            label += f" ({action['x']:g}, {action['y']:g})"
            if kind == "swipe" and all(type(action.get(axis)) in (int, float) and math.isfinite(action[axis]) for axis in ("x2", "y2")):
                label += f" → ({action['x2']:g}, {action['y2']:g})"
        pointers = action.get("pointers")
        if isinstance(pointers, list):
            label += " · " + str(len(pointers)) + " 个触点"
        duration = action.get("ms")
        if kind in {"wait", "long_press", "swipe", "touch"} and type(duration) in (int, float) and math.isfinite(duration):
            label += f" · {duration:g} ms"
        return label

    def _display_learning(self, value):
        counts = {"visual_regions": "当前画面局部视觉区域", "visual_effect_samples": "已比较的动作视觉效果", "demonstrations": "该动作的手动示教次数", "motion_targets": "当前画面运动目标", "similar_state_reward_matches": "相似画面的奖励经验", "valid_candidates": "本次有效动作候选", "cross_scene_control_matches": "当前已学热区匹配数", "cross_scene_control_attempts": "当前热区历史操作次数", "affordance_cells": "跨画面已学控制热区", "affordance_trials": "跨场景控制尝试次数", "affordance_effect_samples": "跨场景视觉效果观测", "affordance_reward_samples": "跨场景目标奖励反馈", "affordance_demonstrations": "跨场景人工示教", "matched_observations": "匹配历史观测", "visits": "所选动作尝试次数", "verified_reward_samples": "已验证外部奖励样本", "transition_samples": "状态转移样本", "transitions": "已记录状态转移", "planning_backups": "经验规划更新", "learned_updates": "累计学习更新", "episodes": "已记录回合", "wins": "证据标记为胜利", "losses": "证据标记为失败"}
        measurements = {"visual_effect_value": "选中动作的视觉效果均值", "similar_state_reward_bonus": "相似画面动作价值", "cross_scene_control_bonus": "跨场景控制经验加成", "learned_value": "外部奖励价值估计", "intrinsic_value": "探索价值估计", "uncertainty": "估计不确定性", "exploration_bonus": "探索加成", "ucb": "动作选择分值", "model_error": "转移预测误差"}
        fields = set(counts) | set(measurements) | {"algorithm", "reward_source", "goal_known", "mode"}
        for key in fields:
            if key in value:
                self._learning_values[key] = value[key]
        snapshot = self._learning_values
        lines = []
        if snapshot.get("algorithm"):
            lines.append("算法：" + str(snapshot["algorithm"]))
        for key, label in counts.items():
            number = snapshot.get(key)
            if type(number) is int and number >= 0:
                lines.append(label + "：" + str(number))
        for key, label in measurements.items():
            number = snapshot.get(key)
            if type(number) in (int, float) and math.isfinite(number):
                lines.append(label + f"：{number:g}")
        source = snapshot.get("reward_source")
        if source:
            lines.append("奖励来源：" + UI_REWARD_SOURCE_LABELS.get(str(source), str(source)))
        if snapshot.get("goal_known") is False:
            lines.append("目标未知；以上探索统计不表示游戏得分或胜率")
        elif lines:
            lines.append("统计来自实际交互；价值估计不等于胜率")
        self.learning_var.set("\n".join(lines) if lines else "等待首条真实状态转移与学习记录")

    def _display_feedback(self, value):
        if not isinstance(value, dict):
            self.feedback_var.set(str(value))
            return
        lines = []
        reward = value.get("reward")
        verified = value.get("reward_verified") is True
        visual_effect = value.get("visual_effect")
        if type(visual_effect) in (int, float) and math.isfinite(visual_effect):
            lines.append("动作后视觉变化：" + ("发生可见变化" if visual_effect > 0 else "未发现有效变化") + "（不代表成绩或胜负）")
        local_effect = value.get("local_effect")
        if isinstance(local_effect, dict) and type(local_effect.get("focus_change")) in (int, float) and type(local_effect.get("ambient_change")) in (int, float):
            lines.append("触点周围变化：" + f"{local_effect['focus_change']:.2%}" + " · 其他画面变化：" + f"{local_effect['ambient_change']:.2%}" + "（像素对比，非因果证明）")
        if verified and type(reward) in (int, float) and math.isfinite(reward):
            lines.append(f"已验证外部奖励：{reward:+g}")
        elif "reward" in value or "reward_verified" in value:
            lines.append("本次未验证到游戏成绩或胜负奖励")
        intrinsic = value.get("intrinsic_reward")
        if type(intrinsic) in (int, float) and math.isfinite(intrinsic):
            lines.append(f"探索反馈：{intrinsic:+g}（不作为游戏成绩）")
        if value.get("state_changed") is True:
            lines.append("动作后观察到状态变化")
        elif value.get("state_changed") is False:
            lines.append("动作后尚未观察到状态变化")
        effect = value.get("fulfilled")
        if effect is True or effect is False:
            result = "符合预期" if effect is True else "不符合预期"
            lines.append(("动作效果已匹配证据：" if value.get("verified") is True else "动作效果待验证：") + result)
        outcome = value.get("outcome") or value.get("result") or value.get("assessment")
        if outcome:
            lines.append("观察结果：" + str(outcome))
        evidence = value.get("evidence")
        if evidence:
            if isinstance(evidence, (dict, list)):
                evidence = json.dumps(evidence, ensure_ascii=False)
            lines.append("可核对依据：" + str(evidence))
        source = value.get("reward_source") or value.get("source")
        if source:
            lines.append("来源：" + UI_REWARD_SOURCE_LABELS.get(str(source), str(source)))
        self.feedback_var.set("\n".join(lines) if lines else "本次动作尚未形成可验证反馈")
        self._display_learning(value)

    def _handle_event(self, kind, value):
        if kind in {"status", "notice"}:
            self.status_var.set(str(value))
        elif kind == "progress" and isinstance(value, dict):
            self.update_progress(value)
        elif kind == "milestone":
            self.preparation_stage = f"第 {value['step']}/{value['total']} 阶段：{value['description']}"
            self._show_progress()
            self.progress_caption.configure(text=self.preparation_stage)
            self.progress_fill.place_configure(relwidth=0)
        elif kind == "prepare_retry":
            self._preparation_error = str(value.get("error", ""))
            self._show_progress()
            self.progress_caption.configure(text=f"本机环境自动复查，第 {value['attempt']} 次\n{value['error']}\n{value['delay']:g} 秒后复查")
        elif kind == "prepared":
            self.preparation_stage = ""
            self._preparation_error = ""
            self._readiness_key = None
            self.progress_items.clear()
            self.progress_area.pack_forget()
        elif kind in {"environment", "blocked"}:
            reason = value.get("reason") or value.get("error") if isinstance(value, dict) else value
            if reason:
                self._preparation_error = str(reason)
                self.status_var.set(str(reason))
            self._readiness_key = None
        elif kind == "install_result":
            names = "、".join(str(item) for item in value.get("files", []))
            self.insight_var.set("已安装：" + names + "\n环境就绪后可点击启动" if value.get("ok") else "安装失败：" + names + "\n" + str(value.get("error", "")))
        elif kind == "resources":
            self._display_resources(value)
        elif kind == "plan":
            self._display_plan(value)
            self._draw_smart_overlay()
        elif kind == "scene" and isinstance(value, dict) and not (self.controller.desired_running or self.controller.resume_requested):
            self._smart_plan = {"scene_graph": value.get("scene_graph", []), "actions": [], "screen_size": value.get("screen_size", [])}
            self._update_smart_controls(value.get("scene_graph", []))
            self._smart_overlay_signature = None
            profile = value.get("game_profile", {})
            label = profile.get("label", "未知玩法") if isinstance(profile, dict) else "未知玩法"
            self.scene_var.set("已检测控件 " + str(value.get("controls", 0)) + " · 视觉区域 " + str(value.get("visual_regions", 0)) + " · 玩法线索 " + str(label) + "\n当前仅展示画面证据；点击启动后由 Agent 自主决策")
            self._draw_smart_overlay()
        elif kind == "running" and value is False:
            self._smart_plan = {}
            self._update_smart_controls([])
            self._smart_overlay_signature = None
            self.canvas.delete("smart_overlay")
            self.scene_var.set("Agent 已停止 · 标注将随下次自动决策更新")
        elif kind == "demonstration" and isinstance(value, dict):
            self.status_var.set("已自动记住手动操作：" + UI_ACTION_LABELS.get(value.get("kind"), str(value.get("kind", ""))) + " · " + str(value.get("game", "")))
        elif kind == "feedback":
            self._display_feedback(value)
        elif kind == "learning" and isinstance(value, dict):
            if any(key in value for key in ("reward", "reward_verified", "intrinsic_reward", "state_changed")):
                self._display_feedback(value)
            else:
                self._display_learning(value)
        elif kind == "stats":
            seconds = value.get("plan_seconds")
            detail = "输入 " + str(value.get("actions", 0)) + " · 判断 " + str(value.get("decisions", 0)) + " · 观察 " + str(value.get("waits", 0))
            if isinstance(seconds, (int, float)) and math.isfinite(seconds):
                detail += f" · 决策 {seconds:.1f}s"
            self.metrics_var.set(detail)
            learning = value.get("learning")
            if isinstance(learning, dict):
                self._display_learning(learning)
            self._queue_layout()
        elif kind == "manual_text_result":
            pending = self.manual_text_request
            if pending is not None and pending[0] == value.get("request_id"):
                if value.get("submitted") and self.input_var.get() == pending[1]:
                    self.input_var.set("")
                self.manual_text_request = None
        elif kind == "exported":
            if isinstance(value, dict):
                missing = value.get("errors", [])
                self.status_var.set(("黑匣子完整保存：" if value.get("complete") else "黑匣子已保存但有 " + str(len(missing)) + " 项数据缺失：") + str(value.get("path", "")))
                if missing:
                    self.insight_var.set("黑匣子缺失项目：\n" + "\n".join(str(item) for item in missing))
            else:
                self.status_var.set("黑匣子已保存：" + str(value))

    def _drain_events(self):
        deadline = time.monotonic() + self.cadence.refresh_period
        latest = {}
        ordered = []
        sequence = 0
        while True:
            try:
                kind, value = self.events.get_nowait()
            except queue.Empty:
                break
            identity = (kind, value.get("stage"), value.get("name")) if kind == "progress" and isinstance(value, dict) else kind
            if kind in {"status", "notice", "resources", "stats", "plan", "scene", "feedback", "progress", "learning", "environment"}:
                latest[identity] = (sequence, (kind, value))
            else:
                ordered.append((sequence, (kind, value)))
            sequence += 1
            if time.monotonic() >= deadline:
                break
        ordered.extend(latest.values())
        ordered.sort(key=lambda item: item[0])
        for _, event in ordered:
            try:
                self._handle_event(*event)
            except (ValueError, TypeError, KeyError, OverflowError, tk.TclError) as exc:
                self.controller.log("ui_event_error", event_kind=str(event[0]), error=str(exc))

    def _viewport(self):
        border = self.canvas.winfo_pixels(self.canvas.cget("highlightthickness")) + self.canvas.winfo_pixels(self.canvas.cget("borderwidth"))
        width = max(1, self.canvas.winfo_width() - border * UI_RECT_EDGE_COUNT)
        height = max(1, self.canvas.winfo_height() - border * UI_RECT_EDGE_COUNT)
        return border, width, height

    def toggle_smart_overlay(self):
        self._smart_overlay_enabled = not self._smart_overlay_enabled
        self.overlay_button.configure(text="智能标注：开" if self._smart_overlay_enabled else "智能标注：关")
        self._smart_overlay_signature = None
        self._draw_smart_overlay()

    def _clear_hover_hint(self, event=None):
        self.hover_var.set("将鼠标移到画面中的标注区域，可查看识别依据")

    def _show_hover_hint(self, event):
        if not self._smart_overlay_enabled or self.photo is None:
            self._clear_hover_hint()
            return
        x = (event.x - self.offset[0]) * self.scale[0]
        y = (event.y - self.offset[1]) * self.scale[1]
        scene = self._smart_plan.get("scene_graph", [])
        matches = [item for item in scene if isinstance(item, dict) and isinstance(item.get("bounds"), (list, tuple)) and len(item["bounds"]) == AI_BOUNDING_BOX_COMPONENTS and item["bounds"][0] <= x <= item["bounds"][AI_SPATIAL_DIMENSIONS] and item["bounds"][1] <= y <= item["bounds"][AI_BOUNDING_BOX_COMPONENTS - 1]]
        if not matches:
            self._clear_hover_hint()
            return
        item = min(matches, key=lambda node: (node["bounds"][AI_SPATIAL_DIMENSIONS] - node["bounds"][0]) * (node["bounds"][AI_BOUNDING_BOX_COMPONENTS - 1] - node["bounds"][1]))
        evidence = {"accessibility": "安卓原生可访问控件", "local_visual": "截图颜色与运动区域，语义未验证", "layout_hypothesis": "仅根据常见游戏触控布局推测", "local_attention": "多尺度图像纹理/运动分析，语义尚未识别", "learned_affordance": "本游戏历史操作与变化的离线统计"}.get(item.get("source"), "未经语义确认")
        title = str(item.get("label") or item.get("kind") or "视觉区域")
        self.hover_var.set(title + "\n识别依据：" + evidence)

    def _draw_smart_overlay(self):
        signature = (self._smart_overlay_enabled, self._smart_plan.get("screen_size"), self.display_size, self.offset, self.last_frame_number)
        if signature == self._smart_overlay_signature:
            return
        self._smart_overlay_signature = signature
        self.canvas.delete("smart_overlay")
        if not self._smart_overlay_enabled or self.photo is None or list(self.image_size) != self._smart_plan.get("screen_size"):
            return
        scale_x, scale_y = self.scale
        offset_x, offset_y = self.offset
        for item in self._smart_plan.get("scene_graph", [])[:LOCAL_AGENT_SMART_OVERLAY_LIMIT]:
            if not isinstance(item, dict) or not isinstance(item.get("bounds"), list) or len(item["bounds"]) != AI_BOUNDING_BOX_COMPONENTS:
                continue
            left, top, right, bottom = item["bounds"]
            source = item.get("source")
            color = UI_COLORS["ui_control"] if source == "accessibility" else UI_COLORS["hypothesis"] if source == "layout_hypothesis" else UI_COLORS["learned_control"] if source == "learned_affordance" else UI_COLORS["vision"]
            style = {"dash": (AI_SPATIAL_DIMENSIONS, AI_SPATIAL_DIMENSIONS)} if source == "layout_hypothesis" else {}
            self.canvas.create_rectangle(offset_x + left / scale_x, offset_y + top / scale_y, offset_x + right / scale_x, offset_y + bottom / scale_y, outline=color, width=1, tags="smart_overlay", **style)
            if source in {"accessibility", "layout_hypothesis", "learned_affordance"} and item.get("label"):
                self.canvas.create_text(offset_x + left / scale_x, offset_y + top / scale_y, anchor="sw", text=str(item["label"])[:UI_OVERLAY_LABEL_LIMIT], fill=color, font=self.font, tags="smart_overlay")
        for action in self._smart_plan.get("actions", [])[:AI_SPATIAL_DIMENSIONS]:
            if not isinstance(action, dict):
                continue
            targets = action.get("pointers") if isinstance(action.get("pointers"), list) else [action]
            for point in targets:
                if not isinstance(point, dict) or not all(type(point.get(axis)) in (int, float) and math.isfinite(point[axis]) for axis in ("x", "y")):
                    continue
                x, y = offset_x + point["x"] / scale_x, offset_y + point["y"] / scale_y
                radius = max(1, self.pad / AI_SPATIAL_DIMENSIONS)
                self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=UI_COLORS["next_action"], outline=UI_COLORS["text"], tags="smart_overlay")
                if all(type(point.get(axis)) in (int, float) and math.isfinite(point[axis]) for axis in ("x2", "y2")):
                    next_x, next_y = offset_x + point["x2"] / scale_x, offset_y + point["y2"] / scale_y
                    if (next_x, next_y) != (x, y):
                        self.canvas.create_line(x, y, next_x, next_y, fill=UI_COLORS["next_action"], arrow="last", width=AI_SPATIAL_DIMENSIONS, tags="smart_overlay")
        self.canvas.tag_raise(self.stale_item)

    def _paint(self, result):
        if result["source_size"] != self.source_size or result["geometry"] != self._input_geometry() or result["number"] < self.last_frame_number:
            return False
        border, width, height = self._viewport()
        desired = self.fit_size(result["source_size"], (width, height))
        if result["target_size"] != desired:
            return False
        started = time.monotonic()
        original = tk.PhotoImage(master=self.window, data=result["data"], format=result["format"])
        if result["format"] == "png" and (original.width() > width or original.height() > height):
            divisor = max(1, math.ceil(original.width() / width), math.ceil(original.height() / height))
            self.photo = original.subsample(divisor, divisor)
        else:
            self.photo = original
        self.image_size = result["source_size"]
        self.display_size = (self.photo.width(), self.photo.height())
        self.scale = (self.image_size[0] / self.display_size[0], self.image_size[1] / self.display_size[1])
        self.offset = (border + (width - self.display_size[0]) // UI_RECT_EDGE_COUNT, border + (height - self.display_size[1]) // UI_RECT_EDGE_COUNT)
        self.canvas.itemconfigure(self.image_item, image=self.photo)
        self.canvas.coords(self.image_item, *self.offset)
        self.canvas.itemconfigure("placeholder", state="hidden")
        self.last_frame_number = result["number"]
        self.display_captured = result["captured"]
        self.display_capture_started = result["capture_started"]
        self.display_geometry = dict(result["geometry"])
        self._smart_overlay_signature = None
        self._draw_smart_overlay()
        elapsed = time.monotonic() - started
        self.cadence.observe("paint", elapsed)
        self.cadence.observe("render", result["seconds"])
        self.controller.ui_render_seconds = elapsed + result["seconds"]
        self._render_error = None
        return True

    def _update_frame(self, state):
        with self.controller.frame_lock:
            png = self.controller.frame
            number = self.controller.frame_number
            captured = self.controller.frame_time
            capture_started = self.controller.frame_start_time
        geometry = self._input_geometry()
        if geometry != self._last_input_geometry:
            self._last_input_geometry = dict(geometry)
            self._input_geometry_changed_at = time.monotonic()
            self.last_render_key = None
            self.release_manual()
        self.cadence.capture(captured)
        if png is not None:
            source_size = frame_dimensions(png)
            if source_size != self.source_size:
                self.source_size = source_size
                self._layout_panel()
        if number == self.last_frame_number and geometry == self.display_geometry and capture_started >= self._input_geometry_changed_at:
            self.display_captured = captured
            self.display_capture_started = capture_started
        visible_capture = self.display_captured if self.photo is not None else captured
        age = max(0.0, time.monotonic() - visible_capture) if visible_capture else 0.0
        capture_seconds = getattr(self.controller, "capture_seconds", None)
        geometry_pending = self.photo is not None and (self.display_geometry != geometry or geometry["pending"] or self.display_capture_started < self._input_geometry_changed_at)
        if geometry_pending:
            self.canvas.itemconfigure(self.stale_item, state="normal", text="画面方向或设备正在更新 · 等待匹配的新截图")
            self.canvas.tag_raise(self.stale_item)
        elif png is not None and age > self.cadence.stale_after(capture_seconds):
            suffix = "正在恢复连接" if state == "RECOVERING" else "等待下一次采集"
            self.canvas.itemconfigure(self.stale_item, state="normal", text=f"画面距今 {age:.1f}s · {suffix}")
            self.canvas.tag_raise(self.stale_item)
        else:
            self.canvas.itemconfigure(self.stale_item, state="hidden")
        result = self.renderer.take()
        if not self.controller.ui_visible:
            self.renderer.discard_pending()
            self.last_render_key = None
            return
        if result is not None:
            try:
                if not self._paint(result):
                    self.last_render_key = None
            except (tk.TclError, ValueError, OverflowError) as exc:
                error = str(exc)
                if error != self._render_error:
                    self.controller.log("ui_frame_error", error=error)
                self._render_error = error
                self.last_render_key = None
                self.status_var.set("正在恢复画面显示：" + error)
        if png is None:
            return
        source_size = self.source_size
        _, width, height = self._viewport()
        target = self.fit_size(source_size, (width, height))
        key = (number, target, tuple(geometry.items()))
        now = time.monotonic()
        if key != self.last_render_key and now - self.last_render_submit >= self.cadence.frame_interval():
            if self.renderer.submit(png, number, captured, source_size, target, capture_started, geometry):
                self.last_render_key = key
                self.last_render_submit = now
        self.controller.ui_frame_interval = self.cadence.frame_interval()

    def poll(self):
        self._poll_after = None
        if self.closing:
            return
        started = time.monotonic()
        try:
            self.controller.ui_visible = self.window.state() != "iconic" and bool(self.window.winfo_ismapped())
            self._drain_events()
            state = self._sync_controls()
            self._update_frame(state)
        except (tk.TclError, ValueError, TypeError, OverflowError) as exc:
            self.controller.log("ui_poll_error", error=str(exc))
        finally:
            elapsed = time.monotonic() - started
            self.cadence.observe("poll", elapsed)
            self.controller.ui_poll_seconds = elapsed
            if not self.closing:
                delay = self.cadence.poll_delay(self.controller.ui_visible, self.events.qsize() > 0)
                self._poll_after = self.window.after(delay, self.poll)

    def close(self):
        if self.closing:
            return
        if self.controller.desired_running or self.controller.resume_requested:
            self.status_var.set("Agent 接管请求仍有效，窗口已最小化；点击结束后可关闭")
            self.window.iconify()
            return
        self.release_manual()
        self.closing = True
        for token in (self._poll_after, self._layout_after):
            if token is not None:
                with contextlib.suppress(tk.TclError):
                    self.window.after_cancel(token)
        self.renderer.close()
        if self.file_drop is not None:
            try:
                self.file_drop.close()
            except Exception as exc:
                self.controller.log("windows_drag_drop_close_error", error=str(exc))
            self.file_drop = None
        self.status_var.set("正在释放本程序资源并保存本地经验")
        self.events.close()
        for widget in (self.green, self.red, self.blue, self.folder_button, self.install_button, *self.manual_widgets):
            self._set_button_state(widget, False)
        done = threading.Event()
        def cleanup():
            try:
                self.controller.close()
            finally:
                done.set()
        threading.Thread(target=cleanup, daemon=True, name="ApplicationShutdown").start()
        def finish():
            if done.is_set():
                self.window.destroy()
            else:
                self.window.after(self.cadence.poll_delay(True), finish)
        self.window.after_idle(finish)


def show_startup_error(error, window=None):
    detail = "程序未能启动：\n" + str(error)
    if window is not None:
        try:
            from tkinter import messagebox as startup_messagebox
            startup_messagebox.showerror(APP_NAME, detail, parent=window)
            return
        except Exception:
            pass
    if os.name == "nt":
        try:
            function = ctypes.WinDLL("user32", use_last_error=True).MessageBoxW
            function.argtypes = [ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_uint]
            function.restype = ctypes.c_int
            if function(None, detail, APP_NAME, 0):
                return
        except Exception:
            pass
    if sys.stderr is not None:
        print(detail, file=sys.stderr)


def main():
    global tk, filedialog, messagebox
    window = None
    application = None
    watchdog = len(sys.argv) >= CONTROL_WATCHDOG_ARGUMENTS and sys.argv[1] == "--watchdog"
    try:
        if os.name != "nt" or struct.calcsize("P") != CONTROL_WINDOWS_POINTER_BYTES or platform.machine().casefold() not in {"amd64", "x86_64"}:
            raise RuntimeError("此程序需要 Windows 11 x64 和 64 位 Python")
        if sys.version_info < CONTROL_PYTHON_MIN_VERSION:
            raise RuntimeError("此程序需要 Python " + ".".join(map(str, CONTROL_PYTHON_MIN_VERSION)) + " 或更新版本")
        windows_version = sys.getwindowsversion()
        if windows_version.major < 10 or windows_version.build < RUNTIME_WINDOWS_11_MIN_BUILD:
            raise RuntimeError("此程序需要 Windows 11 x64，当前 Windows 内核版本不符合要求")
        if watchdog:
            supervisor_process(sys.argv[2], int(sys.argv[CONTROL_WATCHDOG_ARGUMENTS - 1]))
            return 0
        try:
            import tkinter as tk
            from tkinter import filedialog, messagebox
        except ImportError as exc:
            raise RuntimeError("当前 Python 缺少 Tcl/Tk 图形界面组件；本程序需要包含 tkinter 的 64 位 CPython") from exc
        try:
            awareness = ctypes.windll.user32.SetProcessDpiAwarenessContext
            awareness.argtypes = [ctypes.c_void_p]
            awareness.restype = ctypes.c_int
            if not awareness(ctypes.c_void_p(CONTROL_DPI_PER_MONITOR_V2)):
                ctypes.windll.shcore.SetProcessDpiAwareness(CONTROL_DPI_PER_MONITOR)
        except (AttributeError, OSError):
            with contextlib.suppress(Exception):
                ctypes.windll.shcore.SetProcessDpiAwareness(CONTROL_DPI_PER_MONITOR)
        supervised = len(sys.argv) >= CONTROL_RESUME_ARGUMENTS and sys.argv[1] == "--resume-root"
        window = tk.Tk()
        window.withdraw()
        if supervised:
            root = pathlib.Path(sys.argv[2]).resolve()
        else:
            folder = filedialog.askdirectory(parent=window, title="选择工作文件夹，保存游戏数据与本地学习记录", mustexist=False)
            if not folder:
                return 0
            root = pathlib.Path(folder) / "AndroidGameAI"
        application = Application.__new__(Application)
        application.__init__(window, root, supervised=supervised)
        if supervised:
            window.iconify()
        else:
            window.deiconify()
        window.mainloop()
        return 0
    except Exception as exc:
        controller = getattr(application, "controller", None)
        recovering = bool(getattr(controller, "desired_running", False) or getattr(controller, "resume_requested", False))
        if recovering:
            with contextlib.suppress(Exception):
                controller.log("ui_process_failure", error=str(exc), traceback=traceback.format_exc(), preserve_run_intent=True)
        elif watchdog:
            if sys.stderr is not None:
                print(str(exc), file=sys.stderr)
        else:
            show_startup_error(exc, window)
        return 1
    finally:
        controller = getattr(application, "controller", None)
        if controller is not None and not controller.shutdown.is_set():
            if getattr(controller, "desired_running", False) or getattr(controller, "resume_requested", False):
                with contextlib.suppress(Exception):
                    controller._write_supervisor_state()
            else:
                with contextlib.suppress(Exception):
                    controller.close()
        if window is not None:
            with contextlib.suppress(Exception):
                window.destroy()


if __name__ == "__main__":
    raise SystemExit(main())
